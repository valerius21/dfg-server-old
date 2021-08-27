import yaml

from dfg_server.definitions import CONFIG_PATH


class Config:
    """Parsing the config.yml"""
    graphql_endpoint = None
    config = None
    study_size = None
    private_image_part = None
    accumulate_results = None
    accumulation_size = None
    image_server_public = None
    image_server_private = None
    port = None

    def __init__(self):
        with open(CONFIG_PATH, "r", encoding='utf-8') as cfg:
            Config.config = yaml.load(cfg, Loader=yaml.FullLoader)

        Config.graphql_endpoint = Config.config['graphql_endpoint']
        Config.study_size = Config.config['study_size']
        Config.private_image_part = Config.config['private_image_part']
        Config.accumulation_size = Config.config['accumulation_size']
        Config.image_server_private = Config.config['image_server_private']
        Config.image_server_public = Config.config['image_server_public']
        Config.port = Config.config['port']
