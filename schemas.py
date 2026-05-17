from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from datetime import datetime

class QueryCreate(BaseModel):
    query: str

class StructuredData(BaseModel):
    intent: Optional[str] = Field(None, description="The user's intent (e.g., startup_search)")
    industry: Optional[str] = Field(None, description="The industry mentioned in the query")
    geography: Optional[str] = Field(None, description="The geographic region mentioned")
    entity_type: Optional[str] = Field(None, description="The type of entity being searched (e.g., startup)")
    keywords: List[str] = Field(default_factory=list, description="Extracted keywords from the query")
    filters: List[str] = Field(default_factory=list, description="Any specific filters or constraints")
    summary: Optional[str] = Field(None, description="A brief summary of what is being requested")

class QueryResponse(BaseModel):
    id: str
    query: str
    structured_data: Dict[str, Any]
    created_at: datetime

    class Config:
        from_attributes = True
