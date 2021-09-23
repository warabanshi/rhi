import json
import logging
import requests

import config


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class Command():

    def __init__(self, args=None):
        self.args = args

    def call_server(self, payload=None):
        r = requests.post(config.URL, data=json.dumps(payload), headers=config.HEADERS)

        logger.debug(f"send payload: {payload}")
        logger.debug(f"response code = {r}")
        logger.debug(f"response = {r.text}")

        return r
