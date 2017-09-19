import json
import logging


logger = logging.getLogger()


def parse(json_str):
    alert_fields = {}
    json_values = json.loads(json_str)

    json_alerts_attr = json_values['alerts'][0]
    json_alerts_labels_attr = json_alerts_attr['labels']
    json_alerts_annotations_attr = json_alerts_attr['annotations']

    mandatory_fields = ['alertname', 'status', 'instance', 'summary']
    optional_fields = ['severity', 'description']
    fields = mandatory_fields + optional_fields

    for field in fields:
        alert_field_key = 'alert_' + field
        if field in json_alerts_attr:
            alert_fields[alert_field_key] = json_alerts_attr[field]
        elif field in json_alerts_labels_attr:
            alert_fields[alert_field_key] = json_alerts_labels_attr[field]
        elif field in json_alerts_annotations_attr:
            alert_fields[alert_field_key] = json_alerts_annotations_attr[field]
        elif field in mandatory_fields:
            alert_fields['alert_severity'] = 'severe'
            alert_fields['alert_summary'] = 'Incorrect JSON received. At least one mandatory field ('+field+') is absent.'
            alert_fields['alert_status'] = 'incorrect'
            return alert_fields

    return alert_fields
