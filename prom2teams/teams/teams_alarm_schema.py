from marshmallow import Schema, fields


class TeamsAlarmSchema(Schema):
    status = fields.Str()
    severity = fields.Str()
    summary = fields.Str()
    instance = fields.Str()
    description = fields.Str()
    name = fields.Str()


class TeamsAlarm:
    def __init__(self, name, status, severity, summary, instance, description):
        self.name = name
        self.status = status
        self.severity = severity
        self.summary = summary
        self.instance = instance
        self.description = description
