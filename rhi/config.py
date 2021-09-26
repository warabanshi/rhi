import os

ENVIRONMENT = os.getenv("ENV", "dev")
URL = "http://localhost:20080"
HEADERS = {"content-type": "application/json"}
HISTTIMEFORMAT = os.getenv("HISTTIMEFORMAT")
