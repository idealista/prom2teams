from marshmallow import Schema, fields, post_load, EXCLUDE, INCLUDE
import logging

log = logging.getLogger('prom2teams')


class MessageSchema(Schema):

    def __init__(self, exclude_fields=tuple()):
        super().__init__()
        self.exclude_fields = exclude_fields

    receiver = fields.Str()
    status = fields.Str(default='unknown', missing='unknown')
    alerts = fields.Nested('AlertSchema', many=True)
    groupKey = fields.Str()
    externalURL = fields.Str()
    version = fields.Str()
    commonAnnotations = fields.Nested('AnnotationSchema', many=False, unknown=EXCLUDE)
    commonLabels = fields.Nested('LabelSchema', many=False, unknown=EXCLUDE)    
    groupLabels = fields.Nested('LabelSchema', many=False, unknown=EXCLUDE)    

    @post_load()
    def get_alerts(self, message):
        log.debug('JSON received is:\n%s', str(message))
        prom_alerts = []

        base_labels = ('alertname', 'device', 'fstype', 'instance', 'job', 'mountpoint', 'severity')
        excluded = base_labels + self.exclude_fields

        for alert in message['alerts']:
            status = alert['status']
            summary = alert['annotations']['summary']
            instance = alert['labels']['instance']
            name = alert['labels']['alertname']
            description = alert['annotations']['description']
            severity = alert['labels']['severity']
            extra_labels = dict()

            for key in alert['labels']:
                if key not in excluded:
                    extra_labels[key] = alert['labels'][key]

            alert = PrometheusAlert(name, status, severity, summary, instance, description, extra_labels)
            prom_alerts.append(alert)
        return prom_alerts


class AlertSchema(Schema):
    status = fields.Str(default='unknown', missing='unknown')
    labels = fields.Nested('LabelSchema', many=False, unknown=INCLUDE)
    annotations = fields.Nested('AnnotationSchema', many=False, unknown=EXCLUDE)
    startsAt = fields.DateTime()
    endsAt = fields.DateTime()
    generatorURL = fields.Str()


class LabelSchema(Schema):
    alertname = fields.Str(default='unknown', missing='unknown')
    device = fields.Str()
    fstype = fields.Str()
    instance = fields.Str(default='unknown', missing='unknown')
    job = fields.Str()
    mountpoint = fields.Str()
    severity = fields.Str(default='unknown', missing='unknown')


class AnnotationSchema(Schema):
    description = fields.Str(default='unknown', missing='unknown')
    summary = fields.Str(default='unknown', missing='unknown')


class PrometheusAlert:
    def __init__(self, name, status, severity, summary, instance, description, extra_labels=None):
        self.name = name
        self.status = status
        self.severity = severity
        self.summary = summary
        self.instance = instance
        self.description = description
        self.extra_labels = extra_labels
