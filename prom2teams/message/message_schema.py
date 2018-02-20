from marshmallow import Schema, fields, validates


class MessageSchema(Schema):
    receiver = fields.Str()
    status = fields.Str(default='unknown', missing='unknown')
    alerts = fields.Nested('AlertSchema', many=True)
    externalURL = fields.Str()
    version = fields.Str()


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
