from marshmallow import Schema, fields, post_load, EXCLUDE, INCLUDE
import logging

log = logging.getLogger('prom2teams')


class MessageSchema(Schema):
    class Meta:
        unknown = INCLUDE
    def __init__(self, exclude_fields=tuple(), exclude_annotations=tuple()):
        super().__init__()
        self.exclude_fields = exclude_fields
        self.exclude_annotations = exclude_annotations

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

        base_labels = ('alertname', 'device', 'fstype', 'instance', 'mountpoint', 'severity')
        excluded = base_labels + self.exclude_fields
        base_annotations = ('description', 'summary')
        excluded_annotations = base_annotations + self.exclude_annotations

        for alert in message['alerts']:
            status = alert['status']
            summary = alert['annotations']['summary']
            instance = alert['labels']['instance']
            name = alert['labels']['alertname']
            description = alert['annotations']['description']
            severity = alert['labels']['severity']
            extra_labels = dict()
            extra_annotations = dict()

            for key in alert['labels']:
                if key not in excluded:
                    extra_labels[key] = alert['labels'][key]

            for key in alert.get('annotations'):
                annotation = alert['annotations'][key]

                # Annotations with 1 or more dots in them will be interpreted by JSON methods beyond this file to be objects with subobjects.
                # Here, we consider only the dotless case - where an annotation is not interpreted as a dictionary.
                annotation_is_not_dict = not(isinstance(annotation, dict))

                if key not in excluded_annotations and annotation_is_not_dict:
                    extra_annotations[key] = annotation

            alert = PrometheusAlert(name, status, severity, summary, instance, description, extra_labels, extra_annotations)
            prom_alerts.append(alert)
        return prom_alerts


class AlertSchema(Schema):
    status = fields.Str(default='unknown', missing='unknown')
    labels = fields.Nested('LabelSchema', many=False, unknown=INCLUDE)
    annotations = fields.Nested('AnnotationSchema', many=False, unknown=INCLUDE)
    startsAt = fields.DateTime()
    endsAt = fields.DateTime()
    generatorURL = fields.Str()
    fingerprint = fields.Str()
    class Meta:
        unknown = EXCLUDE

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
    def __init__(self, name, status, severity, summary, instance, description, extra_labels=None, extra_annotations=None):
        self.name = name
        self.status = status
        self.severity = severity
        self.summary = summary
        self.instance = instance
        self.description = description
        self.extra_labels = extra_labels
        self.extra_annotations = extra_annotations
