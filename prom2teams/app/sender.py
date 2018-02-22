import logging

from flask import current_app as app

from prom2teams.teams.alarm_mapper import map_prom_alerts_to_teams_alarms
from prom2teams.teams.json_composer import compose_all
from .teams_client import post

log = logging.getLogger('prom2teams')


def send_alarms(alerts, teams_webhook_url):
    alarms = map_prom_alerts_to_teams_alarms(alerts)
    sending_alarms = compose_all(alarms, app.config['TEMPLATE_PATH'])
    for team_alarm in sending_alarms:
        log.debug('The message that will be sent is: %s', str(team_alarm))
        post(teams_webhook_url, team_alarm)
