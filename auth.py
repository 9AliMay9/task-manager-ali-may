from fastapi import HTTPException, Security, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import jwt
from jwt import PyJWTError
from typing import List
from config import settings


# HTTP Bearer scheme for extracting Authorization header
bearer_scheme = HTTPBearer(auto_error=False)


# Load secret key and algorithm from config (you should store this in a .env file)
SECRET_KEY = settings.secret_key
ALGORITHM = "HS256"


def verify_jwt(token: str, required_permissions:List[str]) -> dict:
    """
    Decode and verify a JWT token, and check for required permissions.

    - Returns the decoded payload if valid and authorized.
    - Raises 403 if permissions are insufficient.
    - Raises 401 if token is invalid or expired.
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        permissions = payload.get("permissions", [])
        if not all(perm in permissions for perm in required_permissions):
            raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail="Insufficient permissios"
            )
        return payload
    except PyJWTError:
        raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid or expired token",
                headers={"WWW-Authenticate": "Bearer"},
        )


async def get_current_token(
        credentials: HTTPAuthorizationCredentials = Security(bearer_scheme)):
    """
    Extract the JWT token from the Authorization header.
    Raise 401 if no valid credentials are provided.
    """
    if credentials is None:
        raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Not authenticated",
                headers={"WWW-Authenticate": "Bearer"},
        )
    return credentials.credentials


def require_permission(required: List[str]):
    """
    Dependency generator for route protection.

    Use as:
        @Security(require_permission(["read"]))

    It extracts and verifies JWT token and checks if it includes all required permissions.
    """
    async def wrapper(token: str = Security(get_current_token)):
        return verify_jwt(token, required)
    return wrapper
