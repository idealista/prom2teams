import unittest

from prom2teams.teams.teams_alert_validation import remove_double_quotes_from_teams_alert
from prom2teams.teams.teams_alert_schema import TeamsAlert

ALERT = {
    "name": "Watchdog",
    "status": "firing",
    "severity": 'non""""e',
    "summary": "unknown",
    "instance": "unknown",
    "description": "unknown",
    "fingerprint": '07109567b88e9"""""eb6c',
    "runbook_url": "",
    "extra_labels": {'prometheus': 'cattle-monitoring-s"""""ystem/rancher-monitoring-prometheus'},
    "extra_annotations": {'message': 'This is an alert meant to ensure that the entire alerting pipeline is functional.\nThis alert is always firing, therefore it should always be firing in Alertmanager\nand always fire against a receiver. There are integrations with various notification\nmechanisms that send a notification when this alert is not firing. For example the\n"DeadMansSnitch" integration in PagerDuty.\n'},
}

ALERT_WITHOUT_QUOTES = {
    "name": "Watchdog",
    "status": "firing",
    "severity": 'none',
    "summary": "unknown",
    "instance": "unknown",
    "description": "unknown",
    "fingerprint": '07109567b88e9eb6c',
    "runbook_url": "",
    "extra_labels": {'prometheus': 'cattle-monitoring-system/rancher-monitoring-prometheus'},
    "extra_annotations": {'message': 'This is an alert meant to ensure that the entire alerting pipeline is functional.\nThis alert is always firing, therefore it should always be firing in Alertmanager\nand always fire against a receiver. There are integrations with various notification\nmechanisms that send a notification when this alert is not firing. For example the\nDeadMansSnitch integration in PagerDuty.\n'},
}

TEAMS_ALERT = TeamsAlert(ALERT['name'], ALERT['status'].lower(), ALERT['severity'],
                         ALERT['summary'], ALERT['instance'], ALERT['description'],
                         ALERT['fingerprint'], ALERT['runbook_url'], ALERT['extra_labels'],
                         ALERT['extra_annotations'])

TEAMS_ALERT_WITHOUT_QUOTES = TeamsAlert(ALERT_WITHOUT_QUOTES['name'], ALERT_WITHOUT_QUOTES['status'].lower(), ALERT_WITHOUT_QUOTES['severity'],
                         ALERT_WITHOUT_QUOTES['summary'], ALERT_WITHOUT_QUOTES['instance'], ALERT_WITHOUT_QUOTES['description'],
                         ALERT_WITHOUT_QUOTES['fingerprint'], ALERT_WITHOUT_QUOTES['runbook_url'], ALERT_WITHOUT_QUOTES['extra_labels'],
                         ALERT_WITHOUT_QUOTES['extra_annotations'])


class TestServer(unittest.TestCase):
    def test_remove_double_quotes_from_teams_alert(self):
        alert = remove_double_quotes_from_teams_alert(TEAMS_ALERT)
        self.assertEqual(alert.extra_labels, TEAMS_ALERT_WITHOUT_QUOTES.extra_labels)
        self.assertEqual(alert.extra_annotations, TEAMS_ALERT_WITHOUT_QUOTES.extra_annotations)
        self.assertEqual(alert.severity, TEAMS_ALERT_WITHOUT_QUOTES.severity)
        self.assertEqual(alert.fingerprint, TEAMS_ALERT_WITHOUT_QUOTES.fingerprint)


if __name__ == '__main__':
    unittest.main()
