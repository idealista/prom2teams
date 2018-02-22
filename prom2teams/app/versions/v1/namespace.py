import warnings

from flask import request, current_app as app
from flask_restplus import Resource

from prom2teams.app.sender import send_alarms
from prom2teams.prometheus.message_schema import MessageSchema


from .model import *

ns = api_v1.namespace(name='', description='Version 1 connections')


@ns.route('/')
class AlarmSender(Resource):

    @api_v1.expect(message)
    def post(self):
        _show_deprecated_warning("Call to deprecated function. It will be removed in future versions. "
                                 "Please view the README file.")
        alerts = MessageSchema().load(request.get_json()).data
        send_alarms(alerts, app.config['MICROSOFT_TEAMS']['Connector'])
        return 'OK', 201


def _show_deprecated_warning(msg):
    warnings.warn(message=msg, category=PendingDeprecationWarning)
