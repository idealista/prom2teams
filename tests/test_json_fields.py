import unittest
import json

from context import parse


class TestServer(unittest.TestCase):

    TEST_CONFIG_FILES_PATH = 'tests/data/'

    def test_json_with_all_fields(self):
        with open(self.TEST_CONFIG_FILES_PATH + 'jsons/all_ok.json') as json_data:
            json_received = json.load(json_data)
            alert_fields = parse(json.dumps(json_received))
            self.assertNotIn('Incorrect',str(alert_fields))

    def test_json_without_mandatory_field(self):
        with open(self.TEST_CONFIG_FILES_PATH + 'jsons/without_mandatory_field.json') as json_data:
            json_received = json.load(json_data)
            alert_fields = parse(json.dumps(json_received))
            self.assertIn('Incorrect',str(alert_fields))

    def test_json_without_optional_field(self):
        with open(self.TEST_CONFIG_FILES_PATH + 'jsons/without_optional_field.json') as json_data:
            json_received = json.load(json_data)
            alert_fields = parse(json.dumps(json_received))
            self.assertNotIn('Incorrect',str(alert_fields))


if __name__ == '__main__':
    unittest.main()
