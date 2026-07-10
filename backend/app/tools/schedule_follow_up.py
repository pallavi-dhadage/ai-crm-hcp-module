from langchain.tools import tool
from pydantic import BaseModel, Field

class ScheduleInput(BaseModel):
    hcp_name: str = Field(...)
    follow_up_date: str = Field(...)
    purpose: str = Field(...)
    priority: str = Field("medium")

@tool(args_schema=ScheduleInput)
def schedule_follow_up(hcp_name: str, follow_up_date: str, purpose: str, priority: str = "medium") -> str:
    """Schedule a follow‑up task for an HCP."""
    return f"✅ Follow‑up scheduled for {hcp_name} on {follow_up_date} (priority: {priority})"
