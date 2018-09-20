from prom2teams.teams.teams_alarm_schema import TeamsAlarm, TeamsAlarmSchema
from collections import defaultdict


def map_alarm_to_json(alarm):
    schema = TeamsAlarmSchema()
    result = schema.dump(alarm)
    return result.data


def map_prom_alerts_to_teams_alarms(alerts):
    alerts = group_alerts(alerts, 'status')
    teams_alarms = []
    schema = TeamsAlarmSchema()
    for same_status_alerts in alerts:
        for alert in alerts[same_status_alerts]:
            alarm = TeamsAlarm(alert.name, alert.status.lower(), alert.severity,
                               alert.summary, alert.instance, alert.description)
            json_alarm = schema.dump(alarm).data
            teams_alarms.append(json_alarm)
    return teams_alarms


def map_and_group(alerts, group_alerts_by):
    alerts = group_alerts(alerts, 'status')
    teams_alarms = []
    schema = TeamsAlarmSchema()
    for same_status_alerts in alerts:
        grouped_alerts = group_alerts(alerts[same_status_alerts], group_alerts_by)
        for alert in grouped_alerts:
            features = group_features(grouped_alerts[alert])
            name, description, instance, severity, status, summary = (teams_visualization(features["name"]),
                                                                      teams_visualization(features["description"]),
                                                                      teams_visualization(features["instance"]),
                                                                      teams_visualization(features["severity"]),
                                                                      teams_visualization(features["status"]),
                                                                      teams_visualization(features["summary"]))
            alarm = TeamsAlarm(name, status.lower(), severity, summary, instance, description)
            json_alarm = schema.dump(alarm).data
            teams_alarms.append(json_alarm)
    return teams_alarms


def teams_visualization(feature):
    feature.sort()
    # Teams won't print just one new line
    return ',\n\n\n'.join(feature) if feature else 'unknown'


def group_alerts(alerts, group_alerts_by):
    groups = defaultdict(list)
    for alert in alerts:
        groups[alert.__dict__[group_alerts_by]].append(alert)
    return dict(groups)


def group_features(alerts):
    grouped_features = {feature: list(set([individual_alert.__dict__[feature] for individual_alert in alerts]))
                        for feature in ["name", "description", "instance", "severity", "status", "summary"]}
    return grouped_features
