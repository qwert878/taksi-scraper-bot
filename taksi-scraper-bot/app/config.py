import os
from dotenv import load_dotenv

load_dotenv()

API_ID = int(os.getenv("API_ID", 0))
API_HASH = os.getenv("API_HASH", "")
SESSION_STRING = os.getenv("SESSION_STRING", "")

def parse_chat(value: str):
    value = value.strip()
    try:
        return int(value)
    except ValueError:
        return value

SOURCE_GROUPS = [
    parse_chat(x)
    for x in os.getenv("SOURCE_GROUPS", "").split(",")
    if x.strip()
]

TARGET_GROUP = parse_chat(os.getenv("TARGET_GROUP", ""))
