import warnings

from flask import Flask, request
from flask_restplus import Api, Resource
from prom2teams.web_service.teams_client import post
from prom2teams.teams.json_composer import compose_all
from prom2teams.prometheus.message_schema import MessageSchema
from prom2teams.teams.alarm_mapper import TeamsAlarmMapper


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
            webhook_url = config['Microsoft Teams'][connector]
            message_schema = MessageSchema()
            alerts = message_schema.load(request.get_json()).data
            alarms = TeamsAlarmMapper.map_prom_alerts_to_teams_alarms(alerts)
            sending_alarms = compose_all(template_path, alarms)
            send_alarms_to_teams(sending_alarms, webhook_url, template_path, logger)
            return 'OK', 201

    @api.route('/')
    class AlarmSenderDeprecated(Resource):
        @api.expect(message)
        def post(self):
            webhook_url = config['Microsoft Teams']['Connector']
            deprecated_message = "Call to deprecated function. It will be removed in future versions. " \
                                 "Please view the README file."
            show_deprecated_warning(deprecated_message)
            message_schema = MessageSchema()
            alerts = message_schema.load(request.get_json()).data
            alarms = TeamsAlarmMapper.map_prom_alerts_to_teams_alarms(alerts)
            sending_alarms = compose_all(template_path, alarms)
            send_alarms_to_teams(sending_alarms, webhook_url, template_path, logger)
            return 'OK', 201

    @api.errorhandler
    def default_error_handler(e):
        message = 'An unhandled exception occurred.'
        logger.exception(message + e)
        return {'message': message}, 500

    app.run(host=host, port=port, debug=False)


def send_alarms_to_teams(sending_alarms, teams_webhook_url, template_path, logger):
    for team_alarm in sending_alarms:
        print(team_alarm)
        logger.debug('The message that will be sent is: %s', str(team_alarm))
        post(teams_webhook_url, team_alarm)


def show_deprecated_warning(message):
    warnings.warn(message=message, category=PendingDeprecationWarning)



