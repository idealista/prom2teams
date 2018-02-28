import requests

from .exceptions import MicrosoftTeamsRequestException

session = requests.Session()
session.headers.update({'Content-Type': 'application/json'})


def post(teams_webhook_url, message):
    response = session.post(teams_webhook_url, data=message)
    if not response.ok:
        exception_msg = 'Error performing request to: {}.' \
                            ' Returned status code: {}.' \
                            ' Returned data: {}'
        raise MicrosoftTeamsRequestException(exception_msg.format(teams_webhook_url,
                                             str(response.status_code),
                                             str(response.text)))
