import argparse
import json
import logging
import requests

import rhi.config
import rhi.exceptions

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class Command:
    def __init__(self, args: argparse.Namespace = None):
        self.args = args

    def get_path(self, operation) -> str:
        try:
            return rhi.config.CONF["url"].rstrip("/") + "/" + operation.lstrip("/")
        except KeyError as e:
            raise rhi.exceptions.RhiConfigException(
                'Config "url" was not found. Please try to run "init" command.'
            ) from e

    def call_get(self, operation="") -> requests.Response:
        path = self.get_path(operation)
        r = requests.get(path, headers=rhi.config.HEADERS)

        logger.debug(f"call {path}")
        logger.debug(f"response code = {r}")
        logger.debug(f"response = {r.text}")

        return r

    def call_post(self, operation="", payload=None) -> requests.Response:
        path = self.get_path(operation)

        r = requests.post(path, data=json.dumps(payload), headers=rhi.config.HEADERS)

        logger.debug(f"send payload: {payload}")
        logger.debug(f"response code = {r}")
        logger.debug(f"response = {r.text}")

        return r

    def call_delete(self, operation="", payload=None) -> requests.Response:
        path = self.get_path(operation)

        r = requests.delete(path, data=json.dumps(payload), headers=rhi.config.HEADERS)

        logger.debug(f"send payload: {payload}")
        logger.debug(f"response code = {r}")
        logger.debug(f"response = {r.text}")

        return r
