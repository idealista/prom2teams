import requests

from .exceptions import MicrosoftTeamsRequestException

session = requests.Session()
session.headers.update({'Content-Type': 'application/json'})


def post(teams_webhook_url, message):
    response = session.post(teams_webhook_url, data=message)
    if not response.ok or response.text is not '1':
        exception_msg = 'Error performing request to: {}.\n' \
                        ' Returned status code: {}.\n' \
                        ' Returned data: {}\n' \
                        ' Sent message: {}\n'
        raise MicrosoftTeamsRequestException(exception_msg.format(teams_webhook_url,
                                                                  str(response.status_code),
                                                                  str(response.text),
                                                                  str(message)),
                                             code=response.status_code)
