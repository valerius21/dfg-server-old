import os

DEFINITIONS_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.join(DEFINITIONS_DIR, '..')

# if os.environ["DFG_CONFIG"]:
#     CONFIG_PATH = os.environ["DFG_CONFIG"]
# elif os.environ["DFG_PRODUCTION"]:
#     CONFIG_PATH = '/config.yml'
# else:
CONFIG_PATH = os.path.join(ROOT_DIR, './etc/config.yml')
