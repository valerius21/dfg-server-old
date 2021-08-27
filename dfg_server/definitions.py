import os

DEFINITIONS_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.join(DEFINITIONS_DIR, '..')
CONFIG_PATH = os.path.join(ROOT_DIR, './etc/config.yml')

if not os.environ['DFG_PRODUCTION']:
    CONFIG_PATH = os.path.join(os.environ['HOME'], '/.dfg', 'config.yml')
