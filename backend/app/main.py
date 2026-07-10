from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI(title="HCP CRM Agent")

app.add_middleware(
    CORSMiddleware,
    allow_origins=os.getenv("CORS_ORIGINS", "").split(","),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from app.routes import agent, interactions, hcp
app.include_router(agent.router)
app.include_router(interactions.router)
app.include_router(hcp.router)

@app.get("/")
def root():
    return {"message": "HCP CRM Agent API"}

# Create tables (for SQLite) on startup
from app.database.session import engine, Base
@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)
