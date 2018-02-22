from flask import request, current_app as app
from flask_restplus import Resource

from prom2teams.app.sender import send_alarms
from prom2teams.prometheus.message_schema import MessageSchema


from .model import *

ns = api_v2.namespace(name='', description='Version 2 connections')


@ns.route('/<string:connector>')
@api_v2.doc(params={'connector': 'Name of connector to use'})
class AlarmSender(Resource):

    @api_v2.expect(message)
    def post(self, connector):
        alerts = MessageSchema().load(request.get_json()).data
        send_alarms(alerts, app.config['MICROSOFT_TEAMS'][connector])
        return 'OK', 201
