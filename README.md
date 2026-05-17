# Query Intelligence API

## Assessment Overview

**What I built:**
- A FastAPI backend service with SQLite persistence via SQLAlchemy.
- A `POST /queries` endpoint that accepts natural language queries and extracts structured intelligence (intent, industry, geography, entity type, and keywords) using the Gemini LLM.
- A `GET /queries/{id}` endpoint to retrieve the stored query data using an auto-generated UUID.
- Clean architecture with strict Pydantic schemas enforcing reliable JSON extraction from the LLM.

**What I'd do differently with more time:**
- **Implement Async Background Tasks:** Currently, the POST request blocks while waiting for the LLM to process the query. With more time, I would offload the Gemini API call to a background worker (like Celery or FastAPI's `BackgroundTasks`) and immediately return a "processing" status to the client. This would prevent potential API timeouts on slow LLM responses.

## Setup Instructions

1. **Clone or download the project** to your local machine.

2. **Create a virtual environment** and activate it:
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables**:
   Open the `.env` file and insert your Gemini API Key:
   ```
   GEMINI_API_KEY=your_gemini_api_key_here
   ```

## How to Run Server

Run the FastAPI application using Uvicorn:

```bash
uvicorn main:app --reload
```

The server will be available at `http://127.0.0.1:8000`.
You can view the interactive API documentation at `http://127.0.0.1:8000/docs`.

## Sample cURL Requests

### Create Query (POST)

```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/queries' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "query": "find battery technology startups in Southeast Asia"
}'
```

### Retrieve Query (GET)

```bash
curl -X 'GET' \
  'http://127.0.0.1:8000/queries/YOUR_UUID_HERE' \
  -H 'accept: application/json'
```

## Architecture Summary

This project uses a clean modular structure to separate concerns:
- `main.py`: Entrypoint initializing the FastAPI app and setting up database tables.
- `database.py`: Handles SQLite database connection using SQLAlchemy.
- `models.py`: Defines the SQLAlchemy database models (e.g., `QueryModel`).
- `schemas.py`: Defines Pydantic schemas for request validation and parsing LLM output.
- `routes/queries.py`: Contains API endpoints for creating and retrieving queries.
- `services/llm_service.py`: Contains the logic to communicate with the Gemini API to extract structured JSON data from natural language queries.


