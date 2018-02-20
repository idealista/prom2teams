import logging

from .message_schema import MessageSchema
from .alarm_schema import Alarm, AlarmSchema


logger = logging.getLogger()

class AlarmMapper:

    def map_to_alarms(json):
        alarms = []
        schema = MessageSchema()
        result = schema.load(json)

        message = result.data

        for alert in message['alerts']:
            # mandatory
            status = alert['status']
            summary = alert['annotations']['summary']
            instance = alert['labels']['instance']
            name = alert['labels']['alertname']
            description = alert['annotations']['description']
            severity = alert['labels']['severity']


            alarm = Alarm(name, status, severity, summary, instance, description)
            alarms.append(alarm)

        return alarms

    def map_alarm_to_json(alarm):
        schema = AlarmSchema()
        result = schema.dump(alarm)
        return result.data

