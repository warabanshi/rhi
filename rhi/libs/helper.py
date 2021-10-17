import os

import rhi.config


def exists_conf_file() -> bool:
    return os.path.isfile(rhi.config.CONF_FILE)
