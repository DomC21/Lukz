"""Security utilities for API protection"""
from typing import Optional
from fastapi import HTTPException, Security
from fastapi.security import APIKeyHeader
import os
import re
from dotenv import load_dotenv

load_dotenv()

API_KEY_HEADER = APIKeyHeader(name="X-API-Key", auto_error=False)

async def verify_api_key(api_key: Optional[str] = Security(API_KEY_HEADER)) -> bool:
    """Verify API key from request header"""
    if not api_key:
        raise HTTPException(
            status_code=401,
            detail="API key is required",
            headers={"WWW-Authenticate": "ApiKey"},
        )
    
    expected_key = os.getenv("API_KEY")
    if not expected_key:
        # If API_KEY is not set in environment, allow all requests
        return True
        
    if api_key != expected_key:
        raise HTTPException(
            status_code=401,
            detail="Invalid API key",
            headers={"WWW-Authenticate": "ApiKey"},
        )
    
    return True

def validate_ticker(ticker: Optional[str]) -> bool:
    """Validate stock ticker format"""
    if not ticker:
        return True
    
    # Must be 1-5 uppercase letters
    if not isinstance(ticker, str):
        return False
    
    if not 1 <= len(ticker) <= 5:
        return False
    
    if not ticker.isalpha() or not ticker.isupper():
        return False
    
    return True

def sanitize_input(value: str) -> str:
    """Sanitize user input to prevent injection attacks"""
    if not value:
        return value
        
    # Remove any non-alphanumeric characters except common punctuation
    sanitized = re.sub(r'[^a-zA-Z0-9\s\-_.,]', '', value)
    
    # Limit length to prevent buffer overflow
    return sanitized[:100]
