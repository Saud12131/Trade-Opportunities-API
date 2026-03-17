from datetime import datetime, timedelta
from fastapi import HTTPException
from app.middleware.session import sessions

MAX_REQUESTS = 3
WINDOW_SECONDS = 60


def check_rate_limit(api_key: str):
    now = datetime.utcnow()
    window_start = now - timedelta(seconds=WINDOW_SECONDS)

    requests = sessions[api_key]["requests"]

    # remove old requests
    requests = [req for req in requests if req > window_start]
    sessions[api_key]["requests"] = requests

    if len(requests) >= MAX_REQUESTS:
        raise HTTPException(
            status_code=429,
            detail="Rate limit exceeded. Try again later."
        )