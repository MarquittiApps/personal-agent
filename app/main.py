import json
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from app.core.graph import compile_graph
from app.api.auth import router as auth_router
from app.api.v1.endpoints.knowledge import router as knowledge_router
import asyncio

app = FastAPI(title="Personal AI Core API")

# Inclui rotas de Autenticação OAuth2
app.include_router(auth_router)
app.include_router(knowledge_router, prefix="/api/v1")

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
                        
                # Fim de execução de nó interno/ferramenta
                elif kind == "on_tool_end":
                    if event.get("name") == "update_planning_dashboard":
                        tool_output = event.get("data", {}).get("output")
                        print(f"DEBUG: update_planning_dashboard terminou. Tipo: {type(tool_output)}, Valor: {repr(tool_output)}")
                        output_dict = None
                        
                        if isinstance(tool_output, dict):
                            # Caso ideal: já é dict
                            output_dict = tool_output
                        else:
                            # Tira o content do ToolMessage, se for um
                            if hasattr(tool_output, "content"):
                                content_str = tool_output.content
                            elif isinstance(tool_output, str):
                                content_str = tool_output
                            else:
                                content_str = str(tool_output)
                            
                            print(f"DEBUG: content_str = {repr(content_str)}")
                            
                            # Tenta json.loads primeiro (JSON padrão com aspas duplas)
                            import json as _json
                            import ast
                            try:
                                output_dict = _json.loads(content_str)
                            except Exception:
                                try:
                                    # fallback: ast.literal_eval para dict Python com aspas simples
                                    output_dict = ast.literal_eval(content_str)
                                except Exception as e:
                                    print(f"DEBUG Error parsing tool output: {e}")
                                    
                        if isinstance(output_dict, dict) and output_dict.get("type") == "DASHBOARD_UPDATE":
                            print(f"DEBUG: Disparando DASHBOARD_UPDATE no WebSocket: {output_dict}")
                            await websocket.send_json(output_dict)
                        else:
                            print(f"DEBUG: Não foi possível emitir o evento. Resolvido como: {output_dict}")

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
