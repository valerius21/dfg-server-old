import os

DEFINITIONS_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.join(DEFINITIONS_DIR, '..')


def _get_config():
    if not os.environ['DFG_PRODUCTION']:
        return os.path.join(os.environ['HOME'], '.dfg', 'config.yml')
    return os.path.join(ROOT_DIR, './etc/config.yml')


CONFIG_PATH = _get_config()
