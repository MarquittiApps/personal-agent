import json
import ast
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from app.core.graph import compile_graph
from app.api.auth import router as auth_router
import asyncio

app = FastAPI(title="Personal AI Core API")

# Include OAuth2 Authentication routes
app.include_router(auth_router)

# Compile the graph globally
graph = compile_graph(use_persistence=False) # Simplified for initial setup

@app.websocket("/ws/chat")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    print("WebSocket connected")
    
    try:
        while True:
            # Receive message from frontend
            data = await websocket.receive_text()
            message_data = json.loads(data)
            user_input = message_data.get("text", "")
            
            if not user_input:
                continue

            # Prepare initial state for the create_react_agent graph
            initial_state = {
                "messages": [("user", user_input)]
            }

            # Execute the graph and stream responses
            # Note: LangGraph has native support for event streaming
            async for event in graph.astream_events(initial_state, version="v2"):
                kind = event["event"]
                
                # Token streaming (on_chat_model_stream)
                if kind == "on_chat_model_stream":
                    content = event["data"]["chunk"].content
                    
                    if isinstance(content, list):
                        # Sometimes langchain models chunks as a list of dicts
                        text_chunks = [c.get("text", "") for c in content if isinstance(c, dict)]
                        content = "".join(text_chunks)
                    elif not isinstance(content, str):
                        content = str(content)

                    if content:
                        await websocket.send_json({
                            "type": "token",
                            "content": content
                        })
                
                # Node start (on_chain_start for specific nodes)
                elif kind == "on_chain_start":
                    node_name = event.get("name")
                    if node_name:
                        await websocket.send_json({
                            "type": "status",
                            "content": f"Starting: {node_name}"
                        })
                        
                # End of internal node/tool execution
                elif kind == "on_tool_end":
                    if event.get("name") == "update_planning_dashboard":
                        tool_output = event.get("data", {}).get("output")
                        print(f"DEBUG: update_planning_dashboard finished. Type: {type(tool_output)}, Value: {repr(tool_output)}")
                        output_dict = None
                        
                        if isinstance(tool_output, dict):
                            # Ideal case: already a dict
                            output_dict = tool_output
                        else:
                            # Extract content from ToolMessage, if applicable
                            if hasattr(tool_output, "content"):
                                content_str = tool_output.content
                            elif isinstance(tool_output, str):
                                content_str = tool_output
                            else:
                                content_str = str(tool_output)
                            
                            print(f"DEBUG: content_str = {repr(content_str)}")
                            
                            # Try json.loads first (standard JSON with double quotes)
                            try:
                                output_dict = json.loads(content_str)
                            except Exception:
                                try:
                                    # fallback: ast.literal_eval for Python dict with single quotes
                                    output_dict = ast.literal_eval(content_str)
                                except Exception as e:
                                    print(f"DEBUG Error parsing tool output: {e}")
                                    
                        if isinstance(output_dict, dict) and output_dict.get("type") == "DASHBOARD_UPDATE":
                            print(f"DEBUG: Triggering DASHBOARD_UPDATE on WebSocket: {output_dict}")
                            await websocket.send_json(output_dict)
                        else:
                            print(f"DEBUG: Could not emit event. Resolved as: {output_dict}")

            # Signal end of response
            await websocket.send_json({"type": "end"})

    except WebSocketDisconnect:
        print("WebSocket disconnected")
    except Exception as e:
        print(f"WebSocket Error: {e}")
        await websocket.send_json({"type": "error", "content": str(e)})
        await websocket.close()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
