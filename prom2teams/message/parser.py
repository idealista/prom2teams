import json
import logging


logger = logging.getLogger()


def parse(json_str):
    return_dict = {}
    json_values = json.loads(json_str)

    json_alerts_attr = json_values['alerts'][0]
    json_alerts_labels_attr = json_alerts_attr['labels']
    json_alerts_annotations_attr = json_alerts_attr['annotations']

    mandatory_fields = ['alertname', 'status', 'instance', 'summary']
    optional_fields = ['severity', 'description']
    fields = mandatory_fields + optional_fields

    for field in fields:
        if field in json_alerts_attr:
            return_dict['alert_'+field] = json_alerts_attr[field]
        elif field in json_alerts_labels_attr:
            return_dict['alert_'+field] = json_alerts_labels_attr[field]
        elif field in json_alerts_annotations_attr:
            return_dict['alert_'+field] = json_alerts_annotations_attr[field]
        elif field in mandatory_fields:
            return_dict['alert_severity'] = 'severe'
            return_dict['alert_summary'] = 'Incorrect JSON received. At least one mandatory field ('+field+') is absent.'
            return_dict['alert_status'] = 'incorrect'            
            return return_dict

    return return_dict
