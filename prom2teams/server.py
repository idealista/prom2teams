import logging
import configparser
import os
import warnings

from logging.config import fileConfig
from flask import Flask, request
from flask_restplus import Api, Resource

from prom2teams.teams.client import post
from prom2teams.teams.json_composer import compose
from prom2teams.message.parser import parse
from prom2teams.exceptions import MissingConnectorConfigKeyException


logger = logging.getLogger()
dir = os.path.dirname(__file__)

def run(provided_config_file, template_path, log_file_path, log_level):
    config = get_config(provided_config_file)
    load_logging_config(log_file_path, log_level)
    host = config['HTTP Server']['Host']
    port = int(config['HTTP Server']['Port'])

    app = Flask(__name__)
    api = Api(app)
    @api.route('/v2/<string:connector>')
    class AlarmSender(Resource):
        def post(self, connector):
            json_str = request.get_json()
            webhook_url = config['Microsoft Teams'][connector]
            send_alarms_to_teams(json_str, webhook_url, template_path)
            return 'OK', 201

    @api.route('/')
    class AlarmSenderDeprecated(Resource):
        def post(self):
            deprecated_message = "Call to deprecated function. It will be removed in future versions. Please view the README file."
            show_deprecated_warning(deprecated_message)
            json_str = request.get_json()
            webhook_url = config['Microsoft Teams']['Connector']
            send_alarms_to_teams(json_str, webhook_url, template_path)
            return 'OK', 201

    app.run(host=host, port=port, debug=False)


def send_alarms_to_teams(json, teams_webhook_url, template_path):
    alarms = parse(json)
    for key, alarm in alarms.items():
        sending_alarm = compose(template_path, alarm)
        logger.debug('The message that will be sent is: %s',
                     str(sending_alarm))
        post(teams_webhook_url, sending_alarm)


def load_logging_config(log_file_path, log_level):
    config_file = os.path.join(dir, 'logging_console_config.ini')
    defaults = {'log_level': log_level}
    if(log_file_path):
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


def show_deprecated_warning(message):
    warnings.simplefilter('always', DeprecationWarning)
    warnings.warn(message=message, category=DeprecationWarning)
    warnings.simplefilter('default', DeprecationWarning)

