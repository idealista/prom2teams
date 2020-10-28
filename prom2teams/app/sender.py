

from prom2teams.teams.alarm_mapper import map_and_group, map_prom_alerts_to_teams_alarms
from prom2teams.teams.composer import TemplateComposer
from .teams_client import TeamsClient



class AlarmSender:
    def __init__(self, template_path=None, group_alerts_by=False, teams_client_config=None):
        self.json_composer = TemplateComposer(template_path)
        self.group_alerts_by = group_alerts_by
        self.teams_client = TeamsClient(teams_client_config)
        self.max_payload = self.teams_client.max_payload_length

    def _create_alarms(self, alerts):
        if self.group_alerts_by:
            alarms = map_and_group(alerts, self.group_alerts_by, self.json_composer.compose, self.max_payload)
        else:
            alarms = map_prom_alerts_to_teams_alarms(alerts)
        return self.json_composer.compose_all(alarms)

    def send_alarms(self, alerts, teams_webhook_url):
        sending_alarms = self._create_alarms(alerts)
        for team_alarm in sending_alarms:
            self.teams_client.post(teams_webhook_url, team_alarm)
