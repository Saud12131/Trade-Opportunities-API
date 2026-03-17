from fastapi import HTTPException

# predefined API keys
VALID_API_KEYS = ["test123", "demo123"]


def validate_api_key(api_key: str):
    if api_key not in VALID_API_KEYS:
        raise HTTPException(
            status_code=401,
            detail="Invalid API Key"
        )