import unittest
import os

from prom2teams.app import configuration
from prom2teams.app import exceptions


class TestServer(unittest.TestCase):
    TEST_CONFIG_FILES_PATH = './tests/data/'
    DEFAULT_CONFIG_RELATIVE_PATH = './prom2teams/config.ini'

    def test_get_config_with_invalid_path(self):
        invalid_relative_path = os.path.join(self.TEST_CONFIG_FILES_PATH, 'invalid_path')
        self.assertRaises(FileNotFoundError, configuration._config_provided, invalid_relative_path)

    def test_get_config_without_required_keys_should_raise_exception(self):
        empty_config_relative_path = os.path.join(self.TEST_CONFIG_FILES_PATH, 'empty_config.ini')

        self.assertRaises(exceptions.MissingConnectorConfigKeyException, configuration._config_provided,
                          empty_config_relative_path)

    def test_get_config_without_override(self):
        provided_config_relative_path = os.path.join(self.TEST_CONFIG_FILES_PATH, 'not_overriding_defaults.ini')
        config = configuration._config_provided(provided_config_relative_path)

        self.assertTrue(config.get('Microsoft Teams', 'Connector'))

    def test_get_config_overriding_defaults(self):
        provided_config_relative_path = os.path.join(self.TEST_CONFIG_FILES_PATH, 'overriding_defaults.ini')
        config = configuration._config_provided(provided_config_relative_path)

        self.assertEqual(config.get('HTTP Server', 'Host'), '1.1.1.1')
        self.assertEqual(config.get('HTTP Server', 'Port'), '9089')
        self.assertTrue(config.get('Microsoft Teams', 'Connector'))

    def test_connectors_configured(self):
        provided_config_relative_path = os.path.join(self.TEST_CONFIG_FILES_PATH, 'multiple_connectors_config.ini')
        config = configuration._config_provided(provided_config_relative_path)

        self.assertEqual(config['Microsoft Teams']['connector1'], 'teams_webhook_url')
        self.assertEqual(config['Microsoft Teams']['connector2'], 'another_teams_webhook_url')
        self.assertEqual(config['Microsoft Teams']['connector3'], 'definitely_another_teams_webhook_url')

    def test_get_config_for_all_fields(self):
        provided_config_relative_path = os.path.join(self.TEST_CONFIG_FILES_PATH, 'all_fields.ini')
        config = configuration._config_provided(provided_config_relative_path)

        self.assertEqual(config.get('HTTP Server', 'Host'), '1.1.1.1')
        self.assertEqual(config.get('HTTP Server', 'Port'), '9089')
        self.assertEqual(config.get('Microsoft Teams', 'Connector'), 'some_url')
        self.assertEqual(config.get('Log', 'Level'), 'TEST')
        self.assertEqual(config.get('Log', 'Path'), '/var/log/prom2teams/test.log')
        self.assertEqual(config.get('Template', 'Path'), 'jinja2/template/path')
        self.assertEqual(config.get('Group Alerts', 'Field'), 'name')

if __name__ == '__main__':
    unittest.main()
