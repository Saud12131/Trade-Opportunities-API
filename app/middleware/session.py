from datetime import datetime

sessions = {}

def get_session(api_key: str):
    if api_key not in sessions:
        sessions[api_key] = {
            "requests": [],  # store timestamps
            "history": []
        }

    return sessions[api_key]


def add_request(api_key: str):
    now = datetime.utcnow()
    sessions[api_key]["requests"].append(now)


def add_history(api_key: str, sector: str):
    sessions[api_key]["history"].append(sector)