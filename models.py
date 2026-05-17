import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime, JSON
from database import Base

class QueryModel(Base):
    __tablename__ = "queries"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()), index=True)
    query = Column(String, nullable=False)
    structured_data = Column(JSON, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
