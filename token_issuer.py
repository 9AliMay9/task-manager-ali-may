from fastapi import APIRouter
from datetime import datetime, timedelta
import jwt
from config import settings


router = APIRouter(tags=["Permission"])


# Hardcoded secret key and algorithm for token signing (used only for demo purposes)
SECRET_KEY = settings.secret_key
ALGORITHM = "HS256"


@router.post("/token")
def generate_token(permissions: list[str]):
    """
    Generate a JWT token with the given permissions.
    - Token is valid for 1 hour.
    - For testing/demo purposes only (do not use in production)
    """
    expire = datetime.utcnow() + timedelta(hours=1)
    payload = {
            "permissions": permissions,  # List of granted permissions
            "exp": expire,  # Expiration timestamp (required by JWT spec)
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return {"access_token": token, "token_type": "bearer"}
