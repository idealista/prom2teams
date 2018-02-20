import unittest
import json

from context import AlarmMapper


class TestJSONFields(unittest.TestCase):

    TEST_CONFIG_FILES_PATH = 'tests/data/jsons/'

    def test_json_with_all_fields(self):
        with open(self.TEST_CONFIG_FILES_PATH + 'all_ok.json') as json_data:
            json_received = json.load(json_data)
            alarm = AlarmMapper.map_to_alarms(json_received)[0]
            alert_fields = AlarmMapper.map_alarm_to_json(alarm)
            self.assertNotIn('unknown', str(alert_fields))

    def test_json_without_mandatory_field(self):
        with open(self.TEST_CONFIG_FILES_PATH + 'without_mandatory_field.json') as json_data:
            json_received = json.load(json_data)
            alarm = AlarmMapper.map_to_alarms(json_received)[0]
            alert_fields = AlarmMapper.map_alarm_to_json(alarm)
            self.assertIn('unknown', str(alert_fields))

    def test_json_without_optional_field(self):
        with open(self.TEST_CONFIG_FILES_PATH + 'without_optional_field.json') as json_data:
            json_received = json.load(json_data)
            alarm = AlarmMapper.map_to_alarms(json_received)[0]
            alert_fields = AlarmMapper.map_alarm_to_json(alarm)
            self.assertNotIn('unknown', str(alert_fields))

    def test_json_without_instance_field(self):
        with open(self.TEST_CONFIG_FILES_PATH + 'without_instance_field.json') as json_data:
            json_received = json.load(json_data)
            alarm = AlarmMapper.map_to_alarms(json_received)[0]
            alert_fields = AlarmMapper.map_alarm_to_json(alarm)
            self.assertEqual('unknown', str(alert_fields['instance']))

if __name__ == '__main__':
    unittest.main()
