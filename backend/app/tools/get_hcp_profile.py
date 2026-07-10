from langchain.tools import tool

@tool
def get_hcp_profile(hcp_name: str) -> str:
    """Retrieve HCP profile with interaction history."""
    return f"📋 Profile for {hcp_name}: Specialist in Cardiology, 5 interactions, trend positive."
