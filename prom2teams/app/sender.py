import logging

from prom2teams.teams.alarm_mapper import map_and_group, map_prom_alerts_to_teams_alarms
from prom2teams.teams.composer import TemplateComposer
from .teams_client import post

log = logging.getLogger('prom2teams')


class AlarmSender:

    def __init__(self, template_path=None, group_alerts_by=False):
        self.group_alerts_by = group_alerts_by
        if template_path:
            self.json_composer = TemplateComposer(template_path)
        else:
            self.json_composer = TemplateComposer()

    def _create_alarms(self, alerts):
        if self.group_alerts_by:
            alarms = map_and_group(alerts, self.group_alerts_by)
        else:
            alarms = map_prom_alerts_to_teams_alarms(alerts)
        return self.json_composer.compose_all(alarms)

    def send_alarms(self, alerts, teams_webhook_url):
        sending_alarms = self._create_alarms(alerts)
        for team_alarm in sending_alarms:
            log.debug('The message that will be sent is: %s', str(team_alarm))
            post(teams_webhook_url, team_alarm)
