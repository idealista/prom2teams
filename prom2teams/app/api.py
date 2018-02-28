import logging.config

from flask import Flask, Blueprint

from prom2teams.app.configuration import config_app, setup_logging
from .versions.v1 import api_v1
from .versions.v1.namespace import ns as ns_v1
from .versions.v2 import api_v2
from .versions.v2.namespace import ns as ns_v2

log = logging.getLogger('prom2teams_app')

app = Flask(__name__)


def register_api(application, api, namespace, blueprint):
    api.init_app(blueprint)
    api.add_namespace(namespace)
    application.register_blueprint(blueprint)


def init_app(application):
    config_app(application)
    setup_logging(application)

    blueprint_v1 = Blueprint('api_v1', __name__, url_prefix=application.config['API_V1_URL_PREFIX'])
    blueprint_v2 = Blueprint('api_v2', __name__, url_prefix=application.config['API_V2_URL_PREFIX'])
    register_api(application, api_v1, ns_v1, blueprint_v1)
    register_api(application, api_v2, ns_v2, blueprint_v2)


init_app(app)
log.info(app.config['APP_NAME'] + ' started on ' + app.config['SERVER_NAME'])
