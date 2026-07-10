from fastapi import APIRouter

router = APIRouter(prefix="/api/hcp", tags=["hcp"])

@router.get("/{hcp_name}")
async def get_hcp(hcp_name: str):
    return {"message": f"Profile for {hcp_name} (to be implemented)"}
