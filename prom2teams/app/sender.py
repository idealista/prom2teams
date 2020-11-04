

from prom2teams.teams.alert_mapper import map_and_group, map_prom_alerts_to_teams_alerts
from prom2teams.teams.composer import TemplateComposer
from .teams_client import TeamsClient



class AlertSender:
    def __init__(self, template_path=None, group_alerts_by=False, teams_client_config=None):
        self.json_composer = TemplateComposer(template_path)
        self.group_alerts_by = group_alerts_by
        self.teams_client = TeamsClient(teams_client_config)
        self.max_payload = self.teams_client.max_payload_length

    def _create_alerts(self, alerts):
        if self.group_alerts_by:
            alerts = map_and_group(alerts, self.group_alerts_by, self.json_composer.compose, self.max_payload)
        else:
            alerts = map_prom_alerts_to_teams_alerts(alerts)
        return self.json_composer.compose_all(alerts)

    def send_alerts(self, alerts, teams_webhook_url):
        sending_alerts = self._create_alerts(alerts)
        for team_alert in sending_alerts:
            self.teams_client.post(teams_webhook_url, team_alert)
