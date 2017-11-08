import json
import logging


logger = logging.getLogger()

def check_fields(json_alerts_attr, json_alerts_labels_attr, json_alerts_annotations_attr):
    mandatory_fields = ['alertname', 'status', 'summary']
    optional_fields = ['severity', 'description', 'instance']
    fields = mandatory_fields + optional_fields

    alert_fields = {}
    
    # Set the instance to 'none' by default. 
    alert_fields['alert_instance'] = 'none'

    for field in fields:
        alert_field_key = 'alert_' + field
        if field in json_alerts_attr:
            alert_fields[alert_field_key] = json_alerts_attr[field]
        elif field in json_alerts_labels_attr:
            alert_fields[alert_field_key] = json_alerts_labels_attr[field]
        elif field in json_alerts_annotations_attr:
            alert_fields[alert_field_key] = json_alerts_annotations_attr[field]
        # If the field isn't in the JSON but it's a mandatory field, then we send an error message
        elif field in mandatory_fields:
            alert_fields['alert_severity'] = 'severe'
            alert_fields['alert_status'] = 'incorrect'
            alert_fields['alert_summary'] = 'Incorrect JSON received. At least one mandatory field ('+field+') is absent.'
            return alert_fields

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
