import argparse
import configparser
import logging.config
import os

import sys
import yaml
from flask import Flask, Blueprint

from prom2teams import root
from .teams_client import post
from .versions.v1 import api_v1
from .versions.v1.namespace import ns as ns_v1
from .versions.v2 import api_v2
from .versions.v2.namespace import ns as ns_v2
from .exceptions import MissingConnectorConfigKeyException

log = logging.getLogger(__name__)

app = Flask(__name__)


def _config_command_line():
    parser = argparse.ArgumentParser(description='Receives alert notifications '
                                                 'from Prometheus Alertmanager '
                                                 '(https://github.com/prometheus/alertmanager) '
                                                 'and sends it to Microsoft Teams using configured connectors ')

    parser.add_argument('-c', '--configpath', help='config INI file path', required=False)
    parser.add_argument('-l', '--logfilepath', help='log file path', required=False)
    parser.add_argument('-v', '--loglevel', help='log level', required=False)
    parser.add_argument('-t', '--templatepath', help='Jinja2 template file path', required=False)
    return parser.parse_args()


def _setup_logging(application):
    with open(os.path.join(root, 'config/logging.yml'), 'rt') as f:
        config = yaml.safe_load(f.read())

        for logger in config['loggers']:
            config['loggers'][logger]['level'] = application.config['LOG_LEVEL']
        config['root']['level'] = application.config['LOG_LEVEL']
        config['loggers']['prom2teams.app']['level'] = 'INFO'

        environment = os.getenv('APP_ENVIRONMENT', 'None')
        if environment == 'pro' or environment == 'pre':
            config['handlers']['file']['filename'] = application.config['LOG_FILE_PATH']
            for logger in config['loggers']:
                config['loggers'][logger]['handlers'] = ['file']
            config['root']['handlers'] = ['file']
        else:
            del config['handlers']['file']

        logging.config.dictConfig(config)


def _config_app(application):
    try:
        # Load the default configuration
        application.config.from_object('config.settings')

        # Load the configuration from the instance folder
        instance = os.path.join(root, 'instance')
        config = os.path.join(instance, 'config.py')
        if os.path.isdir(instance) and os.path.exists(config):
            application.config.from_pyfile(config)

        # Load the file specified by the APP_CONFIG_FILE environment variable
        # Variables defined here will override those in the default configuration
        if 'APP_CONFIG_FILE' in os.environ:
            config_provided = _config_provided(os.getenv('APP_CONFIG_FILE'))
            _update_application_configuration(application, config_provided)

        # Parse and load command line properties
        # Variables defined here will override previous configuration
        command_line_args = _config_command_line()
        if command_line_args.configpath:
            config_provided = _config_provided(command_line_args.configpath)
            _update_application_configuration(application, config_provided)
        if command_line_args.loglevel:
            application.config['LOG_LEVEL'] = command_line_args.loglevel
        if command_line_args.logfilepath:
            application.config['LOG_FILE_PATH'] = command_line_args.logfilepath
        if command_line_args.templatepath:
            application.config['TEMPLATE_PATH'] = command_line_args.templatepath

        if 'MICROSOFT_TEAMS' not in application.config:
            raise MissingConnectorConfigKeyException('missing connector key in config')

    except MissingConnectorConfigKeyException:
        sys.exit('No Microsoft Teams connector available')


def _update_application_configuration(application, configuration):
    if 'Microsoft Teams' in configuration:
        application.config['MICROSOFT_TEAMS'] = configuration['Microsoft Teams']
    if 'Template' in configuration and 'Path' in configuration['Template']:
        application.config['TEMPLATE_PATH'] = configuration['Template']['Path']
    if 'Log' in configuration and 'Level' in configuration['Log']:
        application.config['LOG_LEVEL'] = configuration['Log']['Level']
    if 'Log' in configuration and 'Path' in configuration['Log']:
        application.config['LOG_FILE_PATH'] = configuration['Log']['Path']
    if 'HTTP Server' in configuration:
        _host, _port = application.config['SERVER_NAME'].split(':', 1)
        if 'Host' in configuration['HTTP Server']:
            _host = configuration['HTTP Server']['Host']
        if 'Port' in configuration['HTTP Server']:
            _port = configuration['HTTP Server']['Port']
        application.config['SERVER_NAME'] = _host + ':' + _port


def _config_provided(filepath):
    config = configparser.ConfigParser()
    try:
        with open(filepath) as f_prov:
            config.read_file(f_prov)

        if not config.options('Microsoft Teams'):
            raise MissingConnectorConfigKeyException('missing connector key in provided config')

    except configparser.NoSectionError:
        raise MissingConnectorConfigKeyException('missing required Microsoft Teams / '
                                                 'connector key in provided config')
    return config


def _register_api(application, api, namespace, blueprint):
    api.init_app(blueprint)
    api.add_namespace(namespace)
    application.register_blueprint(blueprint)


def init_app(application):
    _config_app(application)
    _setup_logging(application)

    blueprint_v1 = Blueprint('api_v1', __name__, url_prefix=application.config['API_V1_URL_PREFIX'])
    blueprint_v2 = Blueprint('api_v2', __name__, url_prefix=application.config['API_V2_URL_PREFIX'])
    _register_api(application, api_v1, ns_v1, blueprint_v1)
    _register_api(application, api_v2, ns_v2, blueprint_v2)


init_app(app)
log.info(app.config['APP_NAME'] + ' started on ' + app.config['SERVER_NAME'])
