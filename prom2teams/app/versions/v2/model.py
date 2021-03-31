from flask_restplus import fields
from . import api_v2

annotations = api_v2.model('annotations', {
    'description': fields.String(default='disk usage 93% on rootfs device'),
    'summary': fields.String(default='Disk usage alert on CS30.evilcorp'),
    'runbook_url':  fields.String(default='http://myurl.runbook.org')
})

labels = api_v2.model('labels', {
    'alertname': fields.String(default='DiskSpace'),
    'fstype': fields.String(default='rootfs'),
    'device': fields.String(default='rootfs'),
    'instance': fields.String(default='cs30.evilcorp'),
    'job': fields.String(default='fsociety'),
    'mountpoint': fields.String(default='/'),
    'severity': fields.String(default='severe')
})

alert = api_v2.model('alert', {
    'status': fields.String(default='Resolved'),
    'startsAt': fields.String(default='2017-05-09T07:01:37.803Z'),
    'endsAt': fields.String(default='2017-05-09T07:01:37.803Z'),
    'generatorURL': fields.String(default='my.prometheusserver.url'),
    'labels': fields.Nested(labels),
    'annotations': fields.Nested(annotations)
})

message = api_v2.model('message', {
    'receiver': fields.String(default='test_webhook'),
    'status': fields.String(default='Resolved'),
    'alerts': fields.List(fields.Nested(alert)),
    'externalURL': fields.String(default='my.prometheusalertmanager.url'),
    'version': fields.String(default='4')
})
