import unittest
import os
import json

from prom2teams.teams.alert_mapper import map_prom_alerts_to_teams_alerts
from prom2teams.prometheus.message_schema import MessageSchema
from prom2teams.app.sender import AlertSender

from deepdiff import DeepDiff

class TestJSONFields(unittest.TestCase):
    TEST_CONFIG_FILES_PATH = './tests/data/json_files/'

    def test_json_with_all_fields(self):
        with open(os.path.join(self.TEST_CONFIG_FILES_PATH, 'all_ok.json')) as json_data:
            json_received = json.load(json_data)
            alerts = MessageSchema().load(json_received)
            alert = map_prom_alerts_to_teams_alerts(alerts)[0]
            self.assertNotIn('unknown', str(alert))

    def test_json_without_mandatory_field(self):
        with open(os.path.join(self.TEST_CONFIG_FILES_PATH, 'without_mandatory_field.json')) as json_data:
            json_received = json.load(json_data)
            alerts = MessageSchema().load(json_received)
            alert = map_prom_alerts_to_teams_alerts(alerts)[0]
            self.assertIn('unknown', str(alert))

    def test_json_without_optional_field(self):
        with open(os.path.join(self.TEST_CONFIG_FILES_PATH, 'without_optional_field.json')) as json_data:
            json_received = json.load(json_data)
            alerts = MessageSchema().load(json_received)
            alert = map_prom_alerts_to_teams_alerts(alerts)[0]
            self.assertIn("'description': 'unknown'", str(alert))

    def test_json_without_instance_field(self):
        with open(os.path.join(self.TEST_CONFIG_FILES_PATH, 'without_instance_field.json')) as json_data:
            json_received = json.load(json_data)
            alerts = MessageSchema().load(json_received)
            alert = map_prom_alerts_to_teams_alerts(alerts)[0]
            self.assertEqual('unknown', str(alert['instance']))

    def test_fingerprint(self):
        with open(self.TEST_CONFIG_FILES_PATH + 'all_ok.json') as json_data:
            json_received = json.load(json_data)
            alerts = MessageSchema().load(json_received)
            alert = map_prom_alerts_to_teams_alerts(alerts)[0]
            self.assertEqual('dd19ae3d4e06ac55', str(alert['fingerprint']))

    def test_compose_all(self):
        with open(os.path.join(self.TEST_CONFIG_FILES_PATH, 'all_ok.json')) as json_data:
            with open(os.path.join(self.TEST_CONFIG_FILES_PATH, 'teams_alert_all_ok.json')) as expected_data:
                json_received = json.load(json_data)
                json_expected = json.load(expected_data)

                alerts = MessageSchema().load(json_received)
                rendered_data = AlertSender()._create_alerts(alerts)[0]
                json_rendered = json.loads(rendered_data)

                diff = DeepDiff(json_rendered, json_expected, ignore_order=True)
                self.assertTrue(not diff)

    def test_with_common_items(self):
        self.maxDiff = None
        with open(os.path.join(self.TEST_CONFIG_FILES_PATH, 'with_common_items.json')) as json_data:
            with open(os.path.join(self.TEST_CONFIG_FILES_PATH, 'teams_alert_with_common_items.json')) as expected_data:
                json_received = json.load(json_data)
                json_expected = json.load(expected_data)

                alerts = MessageSchema().load(json_received)
                rendered_data = AlertSender()._create_alerts(alerts)[0]
                json_rendered = json.loads(rendered_data)

                self.assertEqual(json_rendered.keys(), json_expected.keys())

    def test_grouping_multiple_alerts(self):
        with open(os.path.join(self.TEST_CONFIG_FILES_PATH, 'all_ok_multiple.json')) as json_data:
            with open(os.path.join(self.TEST_CONFIG_FILES_PATH, 'teams_alert_all_ok_multiple.json')) as expected_data:
                json_received = json.load(json_data)
                json_expected = json.load(expected_data)

                alerts = MessageSchema().load(json_received)
                rendered_data = AlertSender(group_alerts_by='name')._create_alerts(alerts)[0].replace("\n\n\n", " ")
                json_rendered = json.loads(rendered_data)

                diff = DeepDiff(json_rendered, json_expected, ignore_order=True)
                self.assertTrue(not diff)

    def test_with_extra_labels(self):
        excluded_labels = ('pod_name', )
        with open(os.path.join(self.TEST_CONFIG_FILES_PATH, 'all_ok_extra_labels.json')) as json_data:
            with open(os.path.join(self.TEST_CONFIG_FILES_PATH, 'teams_alert_all_ok_extra_labels.json')) as expected_data:
                json_received = json.load(json_data)
                json_expected = json.load(expected_data)

                alerts = MessageSchema(exclude_fields=excluded_labels).load(json_received)
                rendered_data = AlertSender()._create_alerts(alerts)[0]
                json_rendered = json.loads(rendered_data)

                diff = DeepDiff(json_rendered, json_expected, ignore_order=True)
                self.assertTrue(not diff)

    def test_with_extra_annotations(self):
        excluded_annotations = ('message', )
        with open(os.path.join(self.TEST_CONFIG_FILES_PATH, 'all_ok_extra_annotations.json')) as json_data:
            with open(os.path.join(self.TEST_CONFIG_FILES_PATH, 'teams_alert_all_ok_extra_annotations.json')) as expected_data:
               json_received = json.load(json_data)
               json_expected = json.load(expected_data)

               alerts = MessageSchema(exclude_annotations=excluded_annotations).load(json_received)
               rendered_data = AlertSender()._create_alerts(alerts)[0]
               json_rendered = json.loads(rendered_data)

               diff = DeepDiff(json_rendered, json_expected, ignore_order=True)
               self.assertTrue(not diff)

    def test_with_too_long_payload(self):
        with open(os.path.join(self.TEST_CONFIG_FILES_PATH, 'all_ok_multiple.json')) as json_data:
            with open(os.path.join(self.TEST_CONFIG_FILES_PATH, 'teams_alert_all_ok_splitted.json')) as expected_data:
                json_received = json.load(json_data)
                json_expected = json.load(expected_data)

                alerts = MessageSchema().load(json_received)
                rendered_data = '[' + ','.join([a.replace("\n\n\n", " ") for a in AlertSender(group_alerts_by='name', teams_client_config={'MAX_PAYLOAD': 800})._create_alerts(alerts)]) + ']'
                json_rendered = json.loads(rendered_data)

                diff = DeepDiff(json_rendered, json_expected, ignore_order=True)
                self.assertTrue(not diff)

if __name__ == '__main__':
    unittest.main()
