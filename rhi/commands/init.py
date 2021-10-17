import configparser

from typing import Any, Dict

import validators

import rhi.lib.helper
import rhi.config

from rhi.commands.command import Command


class Init(Command):
    def write_to_file(self, conf: Dict[str, Any]) -> None:
        config = configparser.ConfigParser()
        config["DEFAULT"] = conf

        with open(rhi.config.CONF_FILE, mode="w") as f:
            config.write(f)

    def ask_url(self) -> str:
        rhi_server = input(f"Where is rhi-server host? [{rhi.config.DEFAULT_HOST}] >> ")
        if len(rhi_server.strip()) == 0:
            rhi_server = rhi.config.DEFAULT_HOST

        if not validators.url(rhi_server):
            raise Exception(f"Invalist URL have been specified: {rhi_server}")

        return rhi_server

    def invoke(self) -> None:
        if rhi.lib.helper.exists_conf_file():
            print(f"Config file {rhi.config.CONF_FILE} alraedy exists.")
            yn = input("Would you force initialize? (y/n) >> ")

            if yn.upper() != "Y":
                return  # user didn't choose Y. do nothing

        print(f"Initialize {rhi.config.CONF_FILE}")

        conf = {}
        try:
            conf["url"] = self.ask_url()
        except Exception as e:
            print(e)
            return

        try:
            self.write_to_file(conf)
            print(f"{rhi.config.CONF_FILE} was created")
        except Exception as e:
            print(f"Creating {rhi.config.CONF_FILE} failed. {e}")
