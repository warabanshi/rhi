import os

ENVIRONMENT = os.getenv('ENV', 'dev')
URL = 'http://localhost:8000/'
HEADERS = {'content-type': 'application/json'}
HISTTIMEFORMAT = os.getenv('HISTTIMEFORMAT')
