import json
import logging


logger = logging.getLogger()

def check_fields(json_alerts_attr, json_alerts_labels_attr, json_alerts_annotations_attr):
    mandatory_fields = ['alertname', 'status', 'instance', 'summary']
    optional_fields = ['severity', 'description']
    fields = mandatory_fields + optional_fields

    alert_fields = {}
    
    for field in fields:
        alert_field_key = 'alert_' + field
        if field in json_alerts_attr:
            alert_fields[alert_field_key] = json_alerts_attr[field]
        elif field in json_alerts_labels_attr:
            alert_fields[alert_field_key] = json_alerts_labels_attr[field]
        elif field in json_alerts_annotations_attr:
            alert_fields[alert_field_key] = json_alerts_annotations_attr[field]
        # If the field isn't in the JSON but it's a mandatory field, then we use default values
        elif field in mandatory_fields:
            if field in json_alerts_attr:
                alert_fields[alert_field_key] = json_alerts_attr[field]
            else:
                alert_fields[alert_field_key] = 'unknown'
    return alert_fields

def parse(json_str):
    json_values = json.loads(json_str)

    parsed_alarms = {}

    for i, alert in enumerate(json_values['alerts']):
        json_alerts_attr = alert
        json_alerts_labels_attr = json_alerts_attr['labels']
        json_alerts_annotations_attr = json_alerts_attr['annotations']
        parsed_alarms['alarm_' + str(i)]=check_fields(json_alerts_attr, json_alerts_labels_attr, json_alerts_annotations_attr)

    return parsed_alarms
