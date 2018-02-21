import logging
import configparser
import os
import warnings
import prom2teams.model

from logging.config import fileConfig
from prom2teams.exceptions import MissingConnectorConfigKeyException
from .api import run_app


logger = logging.getLogger()
dir = os.path.dirname(__file__)


def run(provided_config_file, template_path, log_file_path, log_level):
    warnings.simplefilter('once', PendingDeprecationWarning)
    config = get_config(provided_config_file)
    load_logging_config(log_file_path, log_level)
    host = config['HTTP Server']['Host']
    port = int(config['HTTP Server']['Port'])

    run_app(config, template_path, host, port, prom2teams.model.message, logger)


def load_logging_config(log_file_path, log_level):
    config_file = os.path.join(dir, 'logging_console_config.ini')
    defaults = {'log_level': log_level}
    if log_file_path:
        config_file = os.path.join(dir, 'logging_file_config.ini')
        defaults = {
                    'log_level': log_level,
                    'log_file_path': log_file_path
        }
    fileConfig(config_file, defaults=defaults)


def get_config(provided_config_file):
    provided_config = configparser.ConfigParser()
    default_config_path = os.path.join(dir, 'config.ini')
    try:
        with open(default_config_path) as f_default:
            provided_config.read_file(f_default)

        with open(provided_config_file) as f_prov:
            provided_config.read_file(f_prov)

        if not provided_config.options('Microsoft Teams'):
            raise MissingConnectorConfigKeyException('missing connector key in provided config')

    except configparser.NoSectionError:
        raise MissingConnectorConfigKeyException('missing required Microsoft Teams / '
                                                 'connector key in provided config')
    return provided_config
