import json
import logging
import requests

import config


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class Command:
    def __init__(self, args=None):
        self.args = args

    def call_get(self, operation="") -> requests.Response:
        path = config.URL + operation
        r = requests.get(path, headers=config.HEADERS)

        logger.debug(f"call {path}")
        logger.debug(f"response code = {r}")
        logger.debug(f"response = {r.text}")

        return r

    def call_post(
        self, operation="", payload=None, method=requests.post
    ) -> requests.Response:
        path = config.URL + operation

        r = method(path, data=json.dumps(payload), headers=config.HEADERS)

        logger.debug(f"send payload: {payload}")
        logger.debug(f"response code = {r}")
        logger.debug(f"response = {r.text}")

        return r
