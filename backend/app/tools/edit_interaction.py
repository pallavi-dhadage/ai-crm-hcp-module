from langchain.tools import tool
from pydantic import BaseModel, Field

class EditInteractionInput(BaseModel):
    interaction_id: int = Field(description="ID of interaction")
    field_to_edit: str = Field(description="Field: notes, summary, type, date, duration, sentiment, follow_up_date")
    new_value: str = Field(description="New value")
    regenerate_summary: bool = Field(False, description="Regenerate AI summary")

def get_interaction_by_id(id_):
    # Dummy
    return {"id": id_, "notes": "old notes"} if id_ == 123 else None

def update_interaction_field(id_, field, value):
    print(f"Updated {field} to {value}")

@tool(args_schema=EditInteractionInput)
def edit_interaction(interaction_id: int, field_to_edit: str, new_value: str, regenerate_summary: bool = False) -> str:
    """Edit a logged HCP interaction."""
    existing = get_interaction_by_id(interaction_id)
    if not existing:
        return f"❌ Interaction {interaction_id} not found."
    editable = ["notes", "summary", "type", "date", "duration", "sentiment", "follow_up_date"]
    if field_to_edit not in editable:
        return f"❌ Invalid field. Choose from {editable}"
    update_interaction_field(interaction_id, field_to_edit, new_value)
    msg = f"✅ Interaction {interaction_id} updated: {field_to_edit} changed."
    if regenerate_summary or field_to_edit == "notes":
        from .log_interaction import llm
        new_summary = llm.invoke(f"Summarize: {new_value}").content.strip()
        update_interaction_field(interaction_id, "ai_summary", new_summary)
        msg += f"\n🔄 Summary regenerated: {new_summary}"
    return msg
