import os

ENVIRONMENT = os.getenv("ENV", "dev")
# URL = "http://localhost:20080"
URL = "http://192.168.1.250:20080"
HEADERS = {"content-type": "application/json"}
HISTTIMEFORMAT = os.getenv("HISTTIMEFORMAT")
