from flask import request, current_app as app
from flask_restplus import Resource

from prom2teams.app.sender import AlarmSender
from prom2teams.prometheus.message_schema import MessageSchema
from .model import *

ns = api_v2.namespace(name='', description='Version 2 connections')


@ns.route('/<string:connector>')
@api_v2.doc(params={'connector': 'Name of connector to use'},
            responses={201: 'OK'})
class AlertReceiver(Resource):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.schema = MessageSchema()
        if app.config['TEMPLATE_PATH']:
            self.sender = AlarmSender(app.config['TEMPLATE_PATH'], app.config['GROUP_ALERTS_BY'])
        else:
            self.sender = AlarmSender(group_alerts_by=app.config['GROUP_ALERTS_BY'])

    @api_v2.expect(message)
    def post(self, connector):
        alerts = self.schema.load(request.get_json()).data
        self.sender.send_alarms(alerts, app.config['MICROSOFT_TEAMS'][connector])
        return 'OK', 201
