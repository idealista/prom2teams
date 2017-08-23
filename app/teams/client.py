import requests

from .exceptions import MicrosoftTeamsRequestException


session = requests.Session()
session.headers.update({'Content-Type': 'application/json'})


def post(teams_webhook_url, message):
    response = session.post(
        teams_webhook_url,
        data=message)

    if not response.ok:
        exception_msg = f'Error performing request to: {teams_webhook_url}.' \
            f' Returned status code: {response.status_code}.' \
            f' Returned data: {response.text}'
        raise MicrosoftTeamsRequestException(exception_msg)
