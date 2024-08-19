import json
import logging
import requests
from tenacity import retry, wait_fixed, after_log

from .exceptions import MicrosoftTeamsRequestException

log = logging.getLogger('prom2teams')


class TeamsClient:
    DEFAULT_CONFIG = {
        'TIMEOUT': 30,
        'MAX_PAYLOAD': 24576,
        'RETRY_ENABLE': False,
        'RETRY_WAIT_TIME': 60
    }

    def __init__(self, config=None):
        self.session = requests.Session()
        self.session.headers.update({'Content-Type': 'application/json'})

        if config is None:
            config = {}
        config = {**TeamsClient.DEFAULT_CONFIG, **config}
        self.timeout = config['TIMEOUT']
        self.max_payload_length = config['MAX_PAYLOAD']
        self.retry = config['RETRY_ENABLE']
        self.wait_time = config['RETRY_WAIT_TIME']

    def post(self, teams_webhook_url, message):
        @retry(wait=wait_fixed(self.wait_time), after=after_log(log, logging.WARN))
        def post_with_retry(teams_webhook_url, message):
            self._do_post(teams_webhook_url, message)

        def simple_post(teams_webhook_url, message):
            self._do_post(teams_webhook_url, message)

        log.debug('The message that will be sent is: ' + message)
        if self.retry:
            post_with_retry(teams_webhook_url, message)
        else:
            simple_post(teams_webhook_url, message)

    def _do_post(self, teams_webhook_url, message):
        response = self.session.post(teams_webhook_url, data=message, timeout=self.timeout)
        if response.status_code != 202 and (response.status_code != 200 or response.text != '1'):
            exception_msg = 'Error performing request to: {}.\n' \
                ' Returned status code: {}.\n' \
                ' Returned data: {}\n' \
                ' Sent message: {}\n'
            exception_msg = exception_msg.format(teams_webhook_url,
                                 str(response.status_code),
                                 str(response.text),
                                 str(message))
            raise MicrosoftTeamsRequestException(
                exception_msg, code=response.status_code)
