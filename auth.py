from fastapi import HTTPException, Security
from fastapi.security import APIKeyHeader
from typing import Optional


# Define the header for token ()
api_key_header = APIKeyHeader(name="X-API-KEY", auto_error=False)


# The Token for demonstration
API_KEY = "secret-token"


def get_api_key(api_key: str = Security(api_key_header)):
    if api_key != API_KEY:
        raise HTTPException(
            status_code=403, detail="Could not validate credentials"
        )
    return api_key
