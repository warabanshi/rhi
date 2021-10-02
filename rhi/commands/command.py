import argparse
import json
import logging
import requests

import rhi.config


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class Command:
    def __init__(self, args: argparse.Namespace = None):
        self.args = args

    def call_get(self, operation="") -> requests.Response:
        path = rhi.config.URL + operation
        r = requests.get(path, headers=rhi.config.HEADERS)

        logger.debug(f"call {path}")
        logger.debug(f"response code = {r}")
        logger.debug(f"response = {r.text}")

        return r

    def call_post(
        self, operation="", payload=None
    ) -> requests.Response:
        path = rhi.config.URL + operation

        r = requests.post(path, data=json.dumps(payload), headers=rhi.config.HEADERS)

        logger.debug(f"send payload: {payload}")
        logger.debug(f"response code = {r}")
        logger.debug(f"response = {r.text}")

        return r

    def call_delete(
        self, operation="", payload=None
    ) -> requests.Response:
        path = rhi.config.URL + operation

        r = requests.delete(path, data=json.dumps(payload), headers=rhi.config.HEADERS)

        logger.debug(f"send payload: {payload}")
        logger.debug(f"response code = {r}")
        logger.debug(f"response = {r.text}")

        return r
