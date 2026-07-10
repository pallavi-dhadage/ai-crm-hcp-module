from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
import json
from typing import Optional
from app.agents.hcp_agent import hcp_graph, HCPAgentState
from langchain_core.messages import HumanMessage

router = APIRouter(prefix="/api/agent", tags=["agent"])

class ChatRequest(BaseModel):
    message: str
    thread_id: Optional[str] = None

@router.post("/chat")
async def chat(request: ChatRequest):
    state = {"messages": [HumanMessage(content=request.message)]}
    try:
        result = await hcp_graph.ainvoke(state)
        return {"response": result["messages"][-1].content}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/stream")
async def stream_chat(message: str):
    async def generate():
        state = {"messages": [HumanMessage(content=message)]}
        try:
            async for event in hcp_graph.astream(state):
                for node_name, node_output in event.items():
                    if node_name == "agent":
                        msgs = node_output.get("messages", [])
                        if msgs:
                            last = msgs[-1]
                            if hasattr(last, "content"):
                                yield f"data: {json.dumps({'type':'chunk','content':last.content})}\n\n"
                    elif node_name == "tools":
                        yield f"data: {json.dumps({'type':'tool','content':'Processing...'})}\n\n"
            yield f"data: {json.dumps({'type':'complete','result':'Done'})}\n\n"
        except Exception as e:
            yield f"data: {json.dumps({'type':'error','content':str(e)})}\n\n"
    return StreamingResponse(generate(), media_type="text/event-stream")
