from prom2teams.teams.teams_alarm_schema import TeamsAlarm, TeamsAlarmSchema


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
