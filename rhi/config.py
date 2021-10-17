import configparser
import os

CONF_FILE = os.path.expanduser("~") + "/.rhiconfig"
DEFAULT_HOST = "http://localhost:45312/"
HISTTIMEFORMAT = os.getenv("HISTTIMEFORMAT")

config = configparser.ConfigParser()
config.read(CONF_FILE)

CONF = config["DEFAULT"]
