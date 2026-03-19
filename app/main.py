import json
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from app.core.graph import compile_graph
from app.api.auth import router as auth_router
import asyncio

app = FastAPI(title="Personal AI Core API")

# Inclui rotas de Autenticação OAuth2
app.include_router(auth_router)

# Compila o grafo globalmente
graph = compile_graph(use_persistence=False) # Simplificado para o setup inicial

@app.websocket("/ws/chat")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    print("WebSocket connected")
    
    try:
        while True:
            # Recebe mensagem do frontend
            data = await websocket.receive_text()
            message_data = json.loads(data)
            user_input = message_data.get("text", "")
            
            if not user_input:
                continue

            # Prepara o estado inicial para o grafo do create_react_agent
            initial_state = {
                "messages": [("user", user_input)]
            }

            # Executa o grafo e faz o stream das respostas
            # Nota: LangGraph suporte nativo a stream de eventos
            async for event in graph.astream_events(initial_state, version="v2"):
                kind = event["event"]
                
                # Stream de tokens (on_chat_model_stream)
                if kind == "on_chat_model_stream":
                    content = event["data"]["chunk"].content
                    
                    if isinstance(content, list):
                        # Às vezes o langchain modela o chunk como lista de dicts
                        text_chunks = [c.get("text", "") for c in content if isinstance(c, dict)]
                        content = "".join(text_chunks)
                    elif not isinstance(content, str):
                        content = str(content)

                    if content:
                        await websocket.send_json({
                            "type": "token",
                            "content": content
                        })
                
                # Início de nó (on_chain_start para nós específicos)
                elif kind == "on_chain_start":
                    node_name = event.get("name")
                    if node_name:
                        await websocket.send_json({
                            "type": "status",
                            "content": f"Iniciando: {node_name}"
                        })

            # Sinaliza fim da resposta
            await websocket.send_json({"type": "end"})

    except WebSocketDisconnect:
        print("WebSocket disconnected")
    except Exception as e:
        print(f"Erro no WebSocket: {e}")
        await websocket.send_json({"type": "error", "content": str(e)})
        await websocket.close()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
