import os
from logging import config

import yaml


def setup_logger() -> None:
    config_path = os.path.join(
        os.path.dirname(__file__), "..", "config", "logging.yaml"
    )
    with open(config_path, "r", encoding="utf-8") as f:
        config.dictConfig(yaml.load(f.read(), Loader=yaml.SafeLoader))
