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
            self.config = yaml.load(cfg, Loader=yaml.FullLoader)

        self.endpoint = self.config['graphql_endpoint']
        self.study_size = self.config['study_size']
        self.private_image_part = self.config['private_image_part']
        self.accumulate_results = self.config['accumulate_results']
        self.accumulation_size = self.config['accumulation_size']
