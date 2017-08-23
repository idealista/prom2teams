import json
import logging


logger = logging.getLogger()


def parse(json_str):
    logger.debug('received: %s', json_str)

    json_values = json.loads(json_str)

    json_alerts_attr = json_values['alerts'][0]
    json_alerts_labels_attr = json_alerts_attr['labels']
    json_alerts_annotations_attr = json_alerts_attr['annotations']

    return {
        'alert_name': json_alerts_labels_attr['alertname'],
        'alert_instance': json_alerts_labels_attr['instance'],
        'alert_severity': json_alerts_labels_attr['severity'],
        'alert_summary': json_alerts_annotations_attr['summary'],
        'alert_description': json_alerts_annotations_attr['description'],
        'alert_status': json_alerts_attr['status']
    }
