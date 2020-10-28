from collections import defaultdict, OrderedDict

from prom2teams.teams.teams_alarm_schema import TeamsAlarm, TeamsAlarmSchema

GROUPABLE_FIELDS = ['name', 'description', 'instance',
                    'severity', 'status', 'summary', 'fingerprint']
EXTRA_FIELDS = ['extra_labels', 'extra_annotations']
FIELD_SEPARATOR = ',\n\n\n'


def map_prom_alerts_to_teams_alarms(alerts):
    alerts = _group_alerts(alerts, 'status')
    teams_alarms = []
    schema = TeamsAlarmSchema()
    for same_status_alerts in alerts:
        for alert in alerts[same_status_alerts]:
            alarm = TeamsAlarm(alert.name, alert.status.lower(), alert.severity,
                               alert.summary, alert.instance, alert.description,
                               alert.fingerprint, alert.extra_labels,
                               alert.extra_annotations)
            json_alarm = schema.dump(alarm)
            teams_alarms.append(json_alarm)
    return teams_alarms


def map_and_group(alerts, group_alerts_by, compose, payload_limit):
    alerts = _group_alerts(alerts, 'status')
    teams_alarms = []
    for same_status_alerts in alerts:
        grouped_alerts = _group_alerts(alerts[same_status_alerts], group_alerts_by)
        for alert_group in grouped_alerts.values():
            json_alarms = _map_group(alert_group, compose, payload_limit)
            teams_alarms.extend(json_alarms)
    return teams_alarms


def _map_group(alert_group, compose, payload_limit):
    schema = TeamsAlarmSchema()
    combined_alerts = []
    teams_alarms = []
    for alert in alert_group:
        json_alarm = schema.dump(_combine_alerts_to_alarm([*combined_alerts, alert]))
        if len(compose(json_alarm).encode('utf-8')) > payload_limit:
            teams_alarms.append(schema.dump(_combine_alerts_to_alarm([alert])))
            teams_alarms.append(schema.dump(_combine_alerts_to_alarm(combined_alerts)))
            combined_alerts.clear()
            json_alarm = None
        else:
            combined_alerts.append(alert)

    if json_alarm:
        teams_alarms.append(json_alarm)
    return teams_alarms


def _combine_alerts_to_alarm(alerts):
    dicts = list(map(vars, alerts))
    groupable = _combine_groupable_fields(dicts)
    extra = _combine_extra_fields(dicts)
    return _map_dict_alert_to_alarm({**groupable, **extra})


def _map_dict_alert_to_alarm(alert):
    return TeamsAlarm(alert['name'], alert['status'].lower(), alert['severity'], alert['summary'],
                      alert['instance'], alert['description'], alert['fingerprint'],
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
