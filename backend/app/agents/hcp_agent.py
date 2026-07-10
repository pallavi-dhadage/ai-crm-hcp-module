from typing import List, Optional, Dict, Any, TypedDict
from langgraph.graph import StateGraph, END
from langgraph.prebuilt import ToolNode, create_react_agent
from langchain_groq import ChatGroq
from langchain_core.messages import BaseMessage, HumanMessage
import os
from dotenv import load_dotenv

load_dotenv()

from app.tools.log_interaction import log_interaction
from app.tools.edit_interaction import edit_interaction
from app.tools.get_hcp_profile import get_hcp_profile
from app.tools.schedule_follow_up import schedule_follow_up
from app.tools.analyze_engagement import analyze_hcp_engagement

# Define state with required keys: messages and remaining_steps
class HCPAgentState(TypedDict):
    messages: List[BaseMessage]
    remaining_steps: int
    current_interaction_id: Optional[int]
    pending_confirmation: Optional[Dict[str, Any]]
    extracted_entities: Optional[Dict[str, Any]]

llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="gemma2-9b-it",
    temperature=0.3
)

tools = [
    log_interaction,
    edit_interaction,
    get_hcp_profile,
    schedule_follow_up,
    analyze_hcp_engagement
]

agent = create_react_agent(
    model=llm,
    tools=tools,
    state_schema=HCPAgentState,
    prompt="""You are an AI sales assistant for a life sciences CRM.
    Help reps log and manage HCP interactions.
    Use the provided tools. Ask for missing info.
    Be concise and professional."""
)

def should_continue(state: HCPAgentState) -> str:
    last = state["messages"][-1]
    if hasattr(last, "tool_calls") and last.tool_calls:
        return "tools"
    return "end"

workflow = StateGraph(HCPAgentState)
workflow.add_node("agent", agent)
workflow.add_node("tools", ToolNode(tools))
workflow.set_entry_point("agent")
workflow.add_conditional_edges("agent", should_continue, {"tools": "tools", "end": END})
workflow.add_edge("tools", "agent")
hcp_graph = workflow.compile()
