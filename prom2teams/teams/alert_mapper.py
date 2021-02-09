from collections import defaultdict, OrderedDict

from prom2teams.teams.teams_alert_schema import TeamsAlert, TeamsAlertSchema

GROUPABLE_FIELDS = ['name', 'description', 'instance',
                    'severity', 'status', 'summary', 'fingerprint', 'runbook_url']
EXTRA_FIELDS = ['extra_labels', 'extra_annotations']
FIELD_SEPARATOR = ',\n\n\n'


def map_prom_alerts_to_teams_alerts(alerts):
    alerts = _group_alerts(alerts, 'status')
    teams_alerts = []
    schema = TeamsAlertSchema()
    for same_status_alerts in alerts:
        for alert in alerts[same_status_alerts]:
            alert = TeamsAlert(alert.name, alert.status.lower(), alert.severity,
                               alert.summary, alert.instance, alert.description,
                               alert.fingerprint, alert.runbook_url, alert.extra_labels,
                               alert.extra_annotations)
            json_alert = schema.dump(alert)
            teams_alerts.append(json_alert)
    return teams_alerts


def map_and_group(alerts, group_alerts_by, compose, payload_limit):
    alerts = _group_alerts(alerts, 'status')
    teams_alerts = []
    for same_status_alerts in alerts:
        grouped_alerts = _group_alerts(alerts[same_status_alerts], group_alerts_by)
        for alert_group in grouped_alerts.values():
            json_alerts = _map_group(alert_group, compose, payload_limit)
            teams_alerts.extend(json_alerts)
    return teams_alerts


def _map_group(alert_group, compose, payload_limit):
    schema = TeamsAlertSchema()
    combined_alerts = []
    teams_alerts = []
    for alert in alert_group:
        json_alert = schema.dump(_combine_alerts_to_alert([*combined_alerts, alert]))
        if len(compose(json_alert).encode('utf-8')) > payload_limit:
            teams_alerts.append(schema.dump(_combine_alerts_to_alert([alert])))
            teams_alerts.append(schema.dump(_combine_alerts_to_alert(combined_alerts)))
            combined_alerts.clear()
            json_alert = None
        else:
            combined_alerts.append(alert)

    if json_alert:
        teams_alerts.append(json_alert)
    return teams_alerts


def _combine_alerts_to_alert(alerts):
    dicts = list(map(vars, alerts))
    groupable = _combine_groupable_fields(dicts)
    extra = _combine_extra_fields(dicts)
    return _map_dict_alert_to_alert({**groupable, **extra})


def _map_dict_alert_to_alert(alert):
    return TeamsAlert(alert['name'], alert['status'].lower(), alert['severity'], alert['summary'],
                      alert['instance'], alert['description'], alert['fingerprint'], alert['runbook_url'],
                      alert['extra_labels'], alert['extra_annotations'])


def _combine_groupable_fields(alerts):
    return {field: _teams_visualization([alert[field] for alert in alerts]) for field in GROUPABLE_FIELDS}


def _combine_extra_fields(alerts):
    return {field: {k: v for alert in alerts for k, v in alert[field].items()} for field in EXTRA_FIELDS}


def _teams_visualization(field):
    field.sort()
    # Teams won't print just one new line
    return FIELD_SEPARATOR.join(OrderedDict.fromkeys(field)) if field else 'unknown'


def _group_alerts(alerts, group_alerts_by):
    groups = defaultdict(list)
    for alert in alerts:
        groups[alert.__dict__[group_alerts_by]].append(alert)
    return dict(groups)
