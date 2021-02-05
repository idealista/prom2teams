from marshmallow import Schema, fields, INCLUDE


class TeamsAlertSchema(Schema):
    class Meta:
        unknown = INCLUDE
    status = fields.Str()
    severity = fields.Str()
    summary = fields.Str()
    instance = fields.Str()
    description = fields.Str()
    name = fields.Str()
    fingerprint = fields.Str()
    runbook_url = fields.Str()
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


class TeamsAlert:
    def __init__(self, name, status, severity, summary, instance, description, fingerprint, runbook_url, extra_labels, extra_annotations):
        self.name = name
        self.status = status
        self.severity = severity
        self.summary = summary
        self.instance = instance
        self.description = description
        self.fingerprint = fingerprint
        self.runbook_url = runbook_url
        self.extra_labels = extra_labels
        self.extra_annotations = extra_annotations
