import logging
from flask_restplus import Api

log = logging.getLogger(__name__)

api_v2 = Api(version='2.0', title='Prom2Teams API v2',
             description='A swagger interface for Prom2Teams webservices')


@api_v2.errorhandler
def default_error_handler(e):
    msg = 'An unhandled exception occurred.'
    log.exception(msg + e)
    return {'message': msg}, 500
