from fastapi import FastAPI
from dotenv import load_dotenv

# Load environment variables first
load_dotenv()

from database import engine, Base
from routes import queries

# Create all tables in the engine
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Query Intelligence API",
    description="Backend API service that accepts natural language research queries and extracts structured intelligence using an LLM.",
    version="1.0.0"
)

# Include routes
app.include_router(queries.router)

@app.get("/")
def root():
    return {"message": "Welcome to the Query Intelligence API. Use /docs to view the API documentation."}
