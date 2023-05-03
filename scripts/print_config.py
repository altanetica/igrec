from src.settings import GlobalConfig


def print_config():
    config = GlobalConfig()
    config.dump()
