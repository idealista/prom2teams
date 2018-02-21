import warnings

from flask import Flask, request
from flask_restplus import Api, Resource
from prom2teams.teams.client import post
from prom2teams.teams.json_composer import compose
from prom2teams.message.alarm_mapper import AlarmMapper


app = Flask(__name__)
app.config.SWAGGER_UI_JSONEDITOR = True
api = Api(app, version='2.0', title='Prom2Teams API',
          description='A swagger interface for Prom2Teams webservices')


def run_app(config, template_path, host, port, message, logger):
    @api.route('/v2/<string:connector>')
    @api.doc(params={'connector': 'Name of connector to use'})
    class AlarmSender(Resource):
        @api.expect(message)
        def post(self, connector):
            json = request.get_json()
            alarms = AlarmMapper.map_to_alarms(json)
            webhook_url = config['Microsoft Teams'][connector]
            send_alarms_to_teams(alarms, webhook_url, template_path, logger)
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


def send_alarms_to_teams(alarms, teams_webhook_url, template_path, logger):
    for alarm in alarms:
        sending_alarm = compose(template_path, AlarmMapper.map_alarm_to_json(alarm))
        logger.debug('The message that will be sent is: %s', str(sending_alarm))
        post(teams_webhook_url, sending_alarm)


def show_deprecated_warning(message):
    warnings.warn(message=message, category=PendingDeprecationWarning)