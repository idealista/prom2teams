import logging
import configparser

from http.server import BaseHTTPRequestHandler, HTTPServer
from logging.config import fileConfig

from teams.client import post
from teams.json_composer import compose
from message.parser import parse

from exceptions import MissingConnectorConfigKeyException


logger = logging.getLogger()


def generate_request_handler(teams_webhook_url, template_path):
    class PrometheusRequestHandler(BaseHTTPRequestHandler):
        def __init__(self, *args, **kwargs):
            self.teams_webhook_url = teams_webhook_url
            self.template_path = template_path
            super(PrometheusRequestHandler, self).__init__(*args, **kwargs)

        def _set_headers(self, status_code):
            self.send_response(status_code)
            self.send_header('Content-type', 'text/html')
            self.end_headers()

        def do_POST(self):
            try:
                content_length = self.headers['Content-Length']
                post_data = self.rfile.read(int(content_length))

                logger.debug(f'Data received: {post_data}')
                message = compose(self.template_path, parse(post_data))
                logger.debug(f'The message that will be sent is: {message}')

                post(self.teams_webhook_url, message)
                self._set_headers(200)
            except Exception as e:
                logger.error('Error processing request: %s', str(e))
                self.send_error(500, 'Error processing request')
    return PrometheusRequestHandler


def run(config_file, template_path):
    config = get_config(config_file)

    fileConfig('logging_config.ini')

    host = config['HTTP Server']['Host']
    port = int(config['HTTP Server']['Port'])

    server_address = (host, port)
    request_handler = generate_request_handler(
        config['Microsoft Teams']['Connector'],
        template_path)
    httpd = HTTPServer(server_address, request_handler)
    httpd.serve_forever()


def get_config(provided_config_file):
    default_config = configparser.ConfigParser()
    default_config.read_file(open('config.ini'))
    default_sections = default_config._sections

    provided_config = configparser.ConfigParser(defaults=default_sections)
    provided_config.read_file(open(provided_config_file))

    try:
        provided_config['Microsoft Teams']['Connector']
    except KeyError:
        exception_msg = 'missing required Microsoft Teams' \
                        ' Connector key in provided config'

        raise MissingConnectorConfigKeyException(exception_msg)

    return provided_config
