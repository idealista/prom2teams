import unittest
import json
import sys

from prom2teams.teams.alarm_mapper import map_prom_alerts_to_teams_alarms
from prom2teams.prometheus.message_schema import MessageSchema
from prom2teams.app.sender import AlarmSender


class TestJSONFields(unittest.TestCase):
    TEST_CONFIG_FILES_PATH = 'tests/data/jsons/'

    def __init__(self, *args, **kwargs):
        super(TestJSONFields, self).__init__(*args, **kwargs)
        self.maxDiff = None

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

    def test_with_common_items(self):
        self.maxDiff = None
        with open(self.TEST_CONFIG_FILES_PATH + 'with_common_items.json') as json_data:
            with open(self.TEST_CONFIG_FILES_PATH + 'teams_alarm_with_common_items.json') as expected_data:
                json_received = json.load(json_data)
                json_expected = json.load(expected_data)

                alerts = MessageSchema().load(json_received)
                rendered_data = AlarmSender()._create_alarms(alerts)[0]
                json_rendered = json.loads(rendered_data)

                self.assertEqual(json_rendered.keys(), json_expected.keys())

    def test_grouping_multiple_alerts(self):
        with open(self.TEST_CONFIG_FILES_PATH + 'all_ok_multiple.json') as json_data:
            with open(self.TEST_CONFIG_FILES_PATH + 'teams_alarm_all_ok_multiple.json') as expected_data:
                json_received = json.load(json_data)
                json_expected = json.load(expected_data)

                alerts = MessageSchema().load(json_received)
                rendered_data = AlarmSender(group_alerts_by='name')._create_alarms(alerts)[0].replace("\n\n\n", " ")
                json_rendered = json.loads(rendered_data)

                self.assertDictEqual(json_rendered, json_expected)

    def test_with_extra_labels(self):
        excluded_labels = ('pod_name', )
        with open(self.TEST_CONFIG_FILES_PATH + 'all_ok_extra_labels.json') as json_data:
            with open(self.TEST_CONFIG_FILES_PATH + 'teams_alarm_all_ok_extra_labels.json') as expected_data:
                json_received = json.load(json_data)
                json_expected = json.load(expected_data)

                alerts = MessageSchema(exclude_fields=excluded_labels).load(json_received)
                rendered_data = AlarmSender()._create_alarms(alerts)[0]
                json_rendered = json.loads(rendered_data)

                # account for unsorted dicts in python 3.5
                if sys.version_info[0] == 3 and sys.version_info[1] == 5:
                    facts = json_rendered['sections'][0]['facts']
                    (extra_label1, extra_label2) = facts[-2:]
                    # if the names are not in alphabetical order
                    if extra_label2['name'] != 'prometheus':
                        # switch the fact order
                        facts[-1] = extra_label1
                        facts[-2] = extra_label2

                self.assertDictEqual(json_rendered, json_expected)

    def test_with_extra_annotations(self):
        excluded_annotations = ('message', )
        with open(self.TEST_CONFIG_FILES_PATH + 'all_ok_extra_annotations.json') as json_data:
            with open(self.TEST_CONFIG_FILES_PATH + 'teams_alarm_all_ok_extra_annotations.json') as expected_data:
               json_received = json.load(json_data)
               json_expected = json.load(expected_data)

               alerts = MessageSchema(exclude_annotations=excluded_annotations).load(json_received)
               rendered_data = AlarmSender()._create_alarms(alerts)[0]
               json_rendered = json.loads(rendered_data)

               self.assertDictEqual(json_rendered, json_expected)


if __name__ == '__main__':
    unittest.main()
