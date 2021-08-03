import yaml


class Config:
    """Parsing the config.yml"""
    endpoint = None
    config = None
    study_size = None
    private_image_part = None
    accumulate_results = None
    accumulation_size = None

    def __init__(self):
        with open("config.yml", "r", encoding='utf-8') as cfg:
            Config.config = yaml.load(cfg, Loader=yaml.FullLoader)

        Config.endpoint = Config.config['graphql_endpoint']
        Config.study_size = Config.config['study_size']
        Config.private_image_part = Config.config['private_image_part']
        Config.accumulate_results = Config.config['accumulate_results']
        Config.accumulation_size = Config.config['accumulation_size']
