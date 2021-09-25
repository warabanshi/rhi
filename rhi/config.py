import os

ENVIRONMENT = os.getenv("ENV", "dev")
URL = "http://localhost"
HEADERS = {"content-type": "application/json"}
HISTTIMEFORMAT = os.getenv("HISTTIMEFORMAT")
