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

        def log_message(self, format, *args):
            logger.info("%s - - [%s] %s" % (self.address_string(),
                                            self.log_date_time_string(),
                                            format % args))

    return PrometheusRequestHandler


def run(provided_config_file, template_path, log_file_path, log_level):
    config = get_config('config.ini', provided_config_file)

    load_logging_config(log_file_path, log_level)

    host = config['HTTP Server']['Host']
    port = int(config['HTTP Server']['Port'])

    server_address = (host, port)
    request_handler = generate_request_handler(
        config['Microsoft Teams']['Connector'],
        template_path)
    httpd = HTTPServer(server_address, request_handler)

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        logger.info('server stopped')

    httpd.server_close()


def load_logging_config(log_file_path, log_level):
    config_file = 'logging_console_config.ini'
    defaults = {'log_level': log_level}

    if(log_file_path):
        config_file = 'logging_file_config.ini'
        defaults = {
                    'log_level': log_level,
                    'log_file_path': log_file_path
        }

    fileConfig(config_file, defaults=defaults)


def get_config(default_config_file, provided_config_file):
    provided_config = configparser.ConfigParser()

    with open(default_config_file) as f_def:
        provided_config.read_file(f_def)

    with open(provided_config_file) as f_prov:
        provided_config.read_file(f_prov)

    try:
        provided_config['Microsoft Teams']['Connector']
    except KeyError:
        exception_msg = 'missing required Microsoft Teams' \
                        ' Connector key in provided config'

        raise MissingConnectorConfigKeyException(exception_msg)

    return provided_config
