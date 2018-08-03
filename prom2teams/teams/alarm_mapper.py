from prom2teams.teams.teams_alarm_schema import TeamsAlarm, TeamsAlarmSchema
from collections import defaultdict


def map_alarm_to_json(alarm):
    schema = TeamsAlarmSchema()
    result = schema.dump(alarm)
    return result.data

def map_prom_alerts_to_teams_alarms(alerts):
    teams_alarms = []
    schema = TeamsAlarmSchema()
    for alert in alerts:
        alarm = TeamsAlarm(alert.name, alert.status, alert.severity,
                           alert.summary, alert.instance, alert.description)
        json_alarm = schema.dump(alarm).data
        teams_alarms.append(json_alarm)
    return teams_alarms

def map_prom_alerts_to_teams_alarms(alerts):
    teams_alarms = []
    schema = TeamsAlarmSchema()
    for alert in alerts:
        alarm = TeamsAlarm(alert.name, alert.status, alert.severity,
                           alert.summary, alert.instance, alert.description)
        json_alarm = schema.dump(alarm).data
        teams_alarms.append(json_alarm)
    return teams_alarms


def map_and_group(alerts):
    teams_alarms = []
    schema = TeamsAlarmSchema()
    grouped_alerts = group_alerts(alerts)
    for alert in grouped_alerts:
        instances = remove_duplicated_instances(group_alerts[alert])
        name, status, severity, summary, instance, description = (grouped_alerts[alert][0].name, 'unknown',
                                                                  'unknown', 'unknown',
                                                                  instances, 'unknown')
        alarm = TeamsAlarm(name, status, severity, summary, instance, description)
        json_alarm = schema.dump(alarm).data
        teams_alarms.append(json_alarm)
    return teams_alarms


def group_alerts(alerts):
    groups = defaultdict(list)
    for alert in alerts:
        groups[alert.name].append(alert)
    return dict(groups)

def remove_duplicated_instances(alerts):
    instances = []
    for individual_alert in alerts:
        instances.append(individual_alert.instance)
    return list(set(instances))
