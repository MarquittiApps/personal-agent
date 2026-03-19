import json
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from app.core.graph import compile_graph
import asyncio

app = FastAPI(title="Personal AI Core API")

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

            # Prepara o estado inicial para o grafo
            initial_state = {
                "messages": [user_input],
                "next_action": "start",
                "context": {}
            }

            # Executa o grafo e faz o stream das respostas
            # Nota: LangGraph suporte nativo a stream de eventos
            async for event in graph.astream_events(initial_state, version="v2"):
                kind = event["event"]
                
                # Stream de tokens (on_chat_model_stream)
                if kind == "on_chat_model_stream":
                    content = event["data"]["chunk"].content
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
