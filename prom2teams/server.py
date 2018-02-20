import logging
import configparser
import os
import warnings

from logging.config import fileConfig
from flask import Flask, request
from flask_restplus import Api, Resource

from prom2teams.teams.client import post
from prom2teams.teams.json_composer import compose
from prom2teams.message.alarm_mapper import AlarmMapper
from prom2teams.exceptions import MissingConnectorConfigKeyException

app = Flask(__name__)
app.config.SWAGGER_UI_JSONEDITOR = True
api = Api(app, version='2.0', title='Prom2Teams API',
          description='A swagger interface for Prom2Teams webservices',)

logger = logging.getLogger()
dir = os.path.dirname(__file__)

from .model import message


def run(provided_config_file, template_path, log_file_path, log_level):
    warnings.simplefilter('once', PendingDeprecationWarning)
    config = get_config(provided_config_file)
    load_logging_config(log_file_path, log_level)
    host = config['HTTP Server']['Host']
    port = int(config['HTTP Server']['Port'])

    @api.route('/v2/<string:connector>')
    @api.doc(params={'connector': 'Name of connector to use'})
    class AlarmSender(Resource):
        @api.expect(message)
        def post(self, connector):
            json = request.get_json()
            alarms = AlarmMapper.map_to_alarms(json)
            webhook_url = config['Microsoft Teams'][connector]
            send_alarms_to_teams(alarms, webhook_url, template_path)
            return 'OK', 201

    @api.route('/')
    class AlarmSenderDeprecated(Resource):
        def post(self):
            deprecated_message = "Call to deprecated function. It will be removed in future versions. " \
                                 "Please view the README file."
            show_deprecated_warning(deprecated_message)
            json = request.get_json()
            alarms = AlarmMapper.map_to_alarms(json)
            webhook_url = config['Microsoft Teams']['Connector']
            send_alarms_to_teams(alarms, webhook_url, template_path)
            return 'OK', 201

    app.run(host=host, port=port, debug=False)


def send_alarms_to_teams(alarms, teams_webhook_url, template_path):

    for alarm in alarms:
        sending_alarm = compose(template_path, AlarmMapper.map_alarm_to_json(alarm))
        logger.debug('The message that will be sent is: %s', str(sending_alarm))
        post(teams_webhook_url, sending_alarm)


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


def show_deprecated_warning(message):
    warnings.warn(message=message, category=PendingDeprecationWarning)
