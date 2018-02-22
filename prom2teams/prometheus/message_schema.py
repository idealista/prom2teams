from marshmallow import Schema, fields, post_load


class MessageSchema(Schema):
    receiver = fields.Str()
    status = fields.Str(default='unknown', missing='unknown')
    alerts = fields.Nested('AlertSchema', many=True)
    externalURL = fields.Str()
    version = fields.Str()

    @post_load
    def get_alerts(self, message):
        prom_alerts = []
        for alert in message['alerts']:
            status = alert['status']
            summary = alert['annotations']['summary']
            instance = alert['labels']['instance']
            name = alert['labels']['alertname']
            description = alert['annotations']['description']
            severity = alert['labels']['severity']

            alert = PrometheusAlert(name, status, severity, summary, instance, description)
            prom_alerts.append(alert)
        return prom_alerts


class AlertSchema(Schema):
    status = fields.Str(default='unknown', missing='unknown')
    labels = fields.Nested('LabelSchema', many=False)
    annotations = fields.Nested('AnnotationSchema', many=False)
    startsAt = fields.Date()
    endsAt = fields.Date()
    generatorURL = fields.Str()


class LabelSchema(Schema):
    alertname = fields.Str(default='unknown', missing='unknown')
    device = fields.Str()
    fstype = fields.Str()
    instance = fields.Str(default='unknown', missing='unknown')
    job = fields.Str()
    mountpoint = fields.Str()
    severity = fields.Str(default=None, missing=None)


class AnnotationSchema(Schema):
    description = fields.Str(default=None, missing=None)
    summary = fields.Str(default='unknown', missing='unknown')


class PrometheusAlert:
    def __init__(self, name, status, severity, summary, instance, description):
        self.name = name
        self.status = status
        self.severity = severity
        self.summary = summary
        self.instance = instance
        self.description = description
