from fastapi import APIRouter

router = APIRouter(prefix="/api/interactions", tags=["interactions"])

@router.post("/")
async def create_interaction():
    return {"message": "Create interaction endpoint (to be implemented)"}
