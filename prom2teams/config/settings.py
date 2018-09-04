APP_NAME = 'prom2teams'
HOST = 'localhost'
PORT = 8089
# Flask settings
DEBUG = False

# Flask-Restplus settings
SWAGGER_UI_DOC_EXPANSION = 'list'
SWAGGER_UI_JSONEDITOR = True
VALIDATE = True
MASK_SWAGGER = False
ERROR_404_HELP = False

# Logging extra settings
LOG_FILE_PATH = '/var/log/' + APP_NAME + '/' + APP_NAME + '.log'
LOG_LEVEL = 'DEBUG'

# Group alerts setting
GROUP_ALERTS_BY = False

# Api
API_V1_URL_PREFIX = ''
API_V2_URL_PREFIX = '/v2'

# Template
TEMPLATE_PATH = None
