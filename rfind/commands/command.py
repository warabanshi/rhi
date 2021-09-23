import json
import requests

import config


class Command():

    def __init__(self, args=None):
        self.args = args

    def call_server(self, payload=None):
        r = requests.post(config.URL, data=json.dumps(payload), headers=config.HEADERS)

        print(f"send payload: {payload}")
        print(f"response code = {r}")
        print(f"response = {r.text}")

        return r
