import os
from json import load
from logging import config


def setup_logger() -> None:
    config_path = os.path.join(
        os.path.dirname(__file__), "..", "config", "logging.json"
    )
    with open(config_path, "r", encoding="utf-8") as f:
        config.dictConfig(load(f))
