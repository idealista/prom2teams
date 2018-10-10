import unittest
import json

from prom2teams.teams.alarm_mapper import map_prom_alerts_to_teams_alarms
from prom2teams.prometheus.message_schema import MessageSchema
from prom2teams.app.sender import AlarmSender


class TestJSONFields(unittest.TestCase):

    TEST_CONFIG_FILES_PATH = 'tests/data/jsons/'

    def test_json_with_all_fields(self):
        with open(self.TEST_CONFIG_FILES_PATH + 'all_ok.json') as json_data:
            json_received = json.load(json_data)
            alerts = MessageSchema().load(json_received)
            alarm = map_prom_alerts_to_teams_alarms(alerts)[0]
            self.assertNotIn('unknown', str(alarm))

    def test_json_without_mandatory_field(self):
        with open(self.TEST_CONFIG_FILES_PATH + 'without_mandatory_field.json') as json_data:
            json_received = json.load(json_data)
            alerts = MessageSchema().load(json_received)
            alarm = map_prom_alerts_to_teams_alarms(alerts)[0]
            self.assertIn('unknown', str(alarm))

    def test_json_without_optional_field(self):
        with open(self.TEST_CONFIG_FILES_PATH + 'without_optional_field.json') as json_data:
            json_received = json.load(json_data)
            alerts = MessageSchema().load(json_received)
            alarm = map_prom_alerts_to_teams_alarms(alerts)[0]
            self.assertIn("'description': 'unknown'", str(alarm))

    def test_json_without_instance_field(self):
        with open(self.TEST_CONFIG_FILES_PATH + 'without_instance_field.json') as json_data:
            json_received = json.load(json_data)
            alerts = MessageSchema().load(json_received)
            alarm = map_prom_alerts_to_teams_alarms(alerts)[0]
            self.assertEqual('unknown', str(alarm['instance']))

    def test_compose_all(self):
        with open(self.TEST_CONFIG_FILES_PATH + 'all_ok.json') as json_data:
            with open(self.TEST_CONFIG_FILES_PATH + 'teams_alarm_all_ok.json') as expected_data:
                json_received = json.load(json_data)
                json_expected = json.load(expected_data)

                alerts = MessageSchema().load(json_received)
                rendered_data = AlarmSender()._create_alarms(alerts)[0]
                json_rendered = json.loads(rendered_data)

                self.assertDictEqual(json_rendered, json_expected)

    def test_grouping_multiple_alerts(self):
        with open(self.TEST_CONFIG_FILES_PATH + 'all_ok_multiple.json') as json_data:
            with open(self.TEST_CONFIG_FILES_PATH + 'teams_alarm_all_ok_multiple.json') as expected_data:
                json_received = json.load(json_data)
                json_expected = json.load(expected_data)

                alerts = MessageSchema().load(json_received)
                rendered_data = AlarmSender(group_alerts_by='name')._create_alarms(alerts)[0].replace("\n\n\n", " ")
                json_rendered = json.loads(rendered_data)

                self.assertDictEqual(json_rendered, json_expected)


if __name__ == '__main__':
    unittest.main()
