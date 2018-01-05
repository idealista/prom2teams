import unittest
import json

from context import parse

class TestJSONFields(unittest.TestCase):

    TEST_CONFIG_FILES_PATH = 'tests/data/jsons/'

    def test_json_with_all_fields(self):
        with open(self.TEST_CONFIG_FILES_PATH + 'all_ok.json') as json_data:
            json_received = json.load(json_data)
            alert_fields = parse(json.dumps(json_received))
            self.assertNotIn('Incorrect',str(alert_fields))

    def test_json_without_mandatory_field(self):
        with open(self.TEST_CONFIG_FILES_PATH + 'without_mandatory_field.json') as json_data:
            json_received = json.load(json_data)
            alert_fields = parse(json.dumps(json_received))
            self.assertIn('Incorrect',str(alert_fields))

    def test_json_without_optional_field(self):
        with open(self.TEST_CONFIG_FILES_PATH + 'without_optional_field.json') as json_data:
            json_received = json.load(json_data)
            alert_fields = parse(json.dumps(json_received))
            self.assertNotIn('Incorrect',str(alert_fields))

    def test_json_without_instance_field(self):
        with open(self.TEST_CONFIG_FILES_PATH + 'without_instance_field.json') as json_data:
            json_received = json.load(json_data)
            alert_fields = parse(json.dumps(json_received))
            self.assertEqual('none',str(alert_fields['alarm_0']['alert_instance']))

    def test_json_without_summary_field(self):
        with open(self.TEST_CONFIG_FILES_PATH + 'without_summary_field.json') as json_data:
            json_received = json.load(json_data)
            alert_fields = parse(json.dumps(json_received))
            self.assertNotIn('Incorrect',str(alert_fields))
            self.assertEqual(alert_fields['alarm_0']['alert_alertname'],alert_fields['alarm_0']['alert_summary'])

if __name__ == '__main__':
    unittest.main()
