from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import QueryModel
from schemas import QueryCreate, QueryResponse
from services.llm_service import extract_structured_data

router = APIRouter(
    prefix="/queries",
    tags=["queries"]
)

@router.post("", response_model=QueryResponse, status_code=201)
def create_query(query_data: QueryCreate, db: Session = Depends(get_db)):
    # 1. Accept natural language query
    raw_query = query_data.query
    
    # 2 & 3. Send query to LLM and extract structured information
    structured_data = extract_structured_data(raw_query)
    
    # 4. Store the data
    db_query = QueryModel(
        query=raw_query,
        structured_data=structured_data
    )
    db.add(db_query)
    db.commit()
    db.refresh(db_query)
    
    # 5. Return stored object
    return db_query

@router.get("/{query_id}", response_model=QueryResponse)
def get_query(query_id: str, db: Session = Depends(get_db)):
    # Retrieve previously stored query
    db_query = db.query(QueryModel).filter(QueryModel.id == query_id).first()
    if not db_query:
        raise HTTPException(status_code=404, detail="Query not found")
    return db_query
