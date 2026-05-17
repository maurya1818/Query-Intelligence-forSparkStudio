import os
import json
from google import genai
from google.genai import types
from schemas import StructuredData
from fastapi import HTTPException

# Ensure you have GEMINI_API_KEY in your environment
client = genai.Client()

SYSTEM_PROMPT = """You are an information extraction engine.

Extract structured intelligence from user research queries.

Return ONLY valid JSON.

Fields:
- intent
- industry
- geography
- entity_type
- keywords (list of strings)
- filters (list of strings)
- summary
"""

def extract_structured_data(query: str) -> dict:
    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=query,
            config=types.GenerateContentConfig(
                system_instruction=SYSTEM_PROMPT,
                response_mime_type="application/json",
            ),
        )
        
        # Parse the JSON response
        data = json.loads(response.text)
        
        # Validate against our Pydantic model (it will filter/cast types)
        validated_data = StructuredData(**data)
        return validated_data.model_dump()
        
    except json.JSONDecodeError:
        raise HTTPException(status_code=500, detail="LLM returned malformed JSON.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"LLM extraction failed: {str(e)}")
