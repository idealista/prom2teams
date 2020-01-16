from marshmallow import Schema, fields, INCLUDE


class TeamsAlarmSchema(Schema):
    class Meta:
        unknown = INCLUDE
    status = fields.Str()
    severity = fields.Str()
    summary = fields.Str()
    instance = fields.Str()
    description = fields.Str()
    name = fields.Str()
    extra_labels = fields.Dict(
        keys=fields.Str(),
        values=fields.Str(),
        required=False,
        data_key='extra_labels'
    )
    extra_annotations = fields.Dict(
        keys=fields.Str(),
        values=fields.Str(),
        required=False,
        data_key='extra_annotations'
    )


class TeamsAlarm:
    def __init__(self, name, status, severity, summary, instance, description, extra_labels, extra_annotations):
        self.name = name
        self.status = status
        self.severity = severity
        self.summary = summary
        self.instance = instance
        self.description = description
        self.extra_labels = extra_labels
        self.extra_annotations = extra_annotations
