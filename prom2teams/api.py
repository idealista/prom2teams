from flask import Flask
from flask_restplus import Api


app = Flask(__name__)
app.config.SWAGGER_UI_JSONEDITOR = True
api = Api(app, version='2.0', title='Prom2Teams API', description='A swagger interface for Prom2Teams webservices')