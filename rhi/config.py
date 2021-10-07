import configparser
import os

CONF_FILE = os.path.expanduser("~") + "/.rhiconfig"
DEFAULT_HOST = "http://localhost:45312/"
HISTTIMEFORMAT = os.getenv("HISTTIMEFORMAT")
HEADERS = {"content-type": "application/json"}

URL = "http://localhost:20080"
# URL = "http://192.168.1.250:20080"

config = configparser.ConfigParser()
config.read(CONF_FILE)

CONF = config["DEFAULT"]
