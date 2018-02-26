import warnings

from flask import request, current_app as app
from flask_restplus import Resource

from prom2teams.app.sender import AlarmSender
from prom2teams.prometheus.message_schema import MessageSchema
from .model import *

ns = api_v1.namespace(name='', description='Version 1 connections')


@ns.route('/')
@api_v1.doc(responses={201: 'OK'})
class AlertReceiver(Resource):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.schema = MessageSchema()
        if 'TEMPLATE_PATH' in app.config:
            self.sender = AlarmSender(app.config['TEMPLATE_PATH'])
        else:
            self.sender = AlarmSender()

    @api_v1.expect(message)
    def post(self):
        _show_deprecated_warning("Call to deprecated function. It will be removed in future versions. "
                                 "Please view the README file.")
        alerts = self.schema.load(request.get_json()).data
        self.sender.send_alarms(alerts, app.config['MICROSOFT_TEAMS']['Connector'])
        return 'OK', 201


def _show_deprecated_warning(msg):
    warnings.warn(message=msg, category=PendingDeprecationWarning)
