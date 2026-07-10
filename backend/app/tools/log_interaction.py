from dotenv import load_dotenv
load_dotenv()

from langchain.tools import tool
from langchain_groq import ChatGroq
from pydantic import BaseModel, Field
from typing import Optional
import json
import os

llm = ChatGroq(groq_api_key=os.getenv("GROQ_API_KEY"), model_name="gemma2-9b-it", temperature=0.2)

class LogInteractionInput(BaseModel):
    hcp_name: str = Field(description="Full name of the HCP")
    hcp_specialty: Optional[str] = Field(None, description="Medical specialty")
    interaction_type: str = Field(description="Type: call, meeting, email, lunch, conference, other")
    interaction_date: str = Field(description="Date (YYYY-MM-DD)")
    duration_minutes: Optional[int] = Field(None)
    notes: str = Field(description="Raw notes from rep")
    follow_up_date: Optional[str] = Field(None)
    sentiment: Optional[str] = Field(None)

# Dummy save function (replace later with DB)
def save_interaction_to_db(data):
    print("Saving interaction:", data)
    return 123

@tool(args_schema=LogInteractionInput)
def log_interaction(
    hcp_name: str,
    hcp_specialty: Optional[str],
    interaction_type: str,
    interaction_date: str,
    duration_minutes: Optional[int],
    notes: str,
    follow_up_date: Optional[str],
    sentiment: Optional[str]
) -> str:
    """Log an HCP interaction with AI summarization and entity extraction."""
    # Generate summary
    summary_prompt = f"Summarize these HCP interaction notes professionally: {notes}"
    summary = llm.invoke(summary_prompt).content.strip()
    
    # Extract entities
    entity_prompt = f"Extract products, topics, commitments from: {notes}. Return JSON."
    try:
        entities = json.loads(llm.invoke(entity_prompt).content)
    except:
        entities = {"products": [], "topics": [], "commitments": []}
    
    data = {
        "hcp_name": hcp_name,
        "hcp_specialty": hcp_specialty,
        "interaction_type": interaction_type,
        "interaction_date": interaction_date,
        "duration_minutes": duration_minutes,
        "notes": notes,
        "ai_summary": summary,
        "extracted_entities": entities,
        "follow_up_date": follow_up_date,
        "sentiment": sentiment or "neutral",
    }
    id_ = save_interaction_to_db(data)
    return f"✅ Interaction logged (ID: {id_})\nSummary: {summary}"
