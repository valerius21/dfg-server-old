import yaml


class Config:
    endpoint = None
    config = None

    def __init__(self):
        with open("../config.yml", "r", encoding='utf-8') as cfg:
            self.config = yaml.load(cfg, Loader=yaml.FullLoader)

        self.endpoint = self.config['graphql_endpoint']
