from marshmallow import Schema, fields


class AlarmSchema(Schema):
    status = fields.Str()
    severity = fields.Str()
    summary = fields.Str()
    instance = fields.Str()
    description = fields.Str()
    name = fields.Str()

class Alarm:
    def __init__(self, name, status, severity, summary, instance, description):
        self.name = name
        self.status = status
        self.severity = severity
        self.summary = summary
        self.instance = instance
        self.description = description










