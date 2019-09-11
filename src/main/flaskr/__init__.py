import sys
import time
from flask import Flask
from flask import render_template, url_for, request, redirect, jsonify
import logging
# from flask.logging import default_handler

from flaskr.api.system.routes import mod_system
from flaskr.views.homepage.routes import mod
from flaskr.api.mode.routes import mod_mode
from flaskr.api.guitar.routes import mod_guitar
# from flaskr.static.GuitarLogger import getLogger
LOGSPATH="main/flaskr/static/fronttail.log"

_config = { 'filename':'', 'isPlaying': False , 'file_error':False, 'modes':['AutoPlay Mode','Play Along Mode', 'GenrePlay'], 'logs':""}

# TEMPLATES = "templates/" #goes here by default
def create_app(test_config=None):
	logger = logging.getLogger(__name__)
	logging.basicConfig(filename=LOGSPATH, filemode='w', format='[%(name)s] - [%(levelname)s]: %(message)s')
	app = Flask(__name__, instance_relative_config=True)
	
	app.register_blueprint(mod)
	app.register_blueprint(mod_system, url_prefix='/api')
	app.register_blueprint(mod_mode, url_prefix='/api')
	app.register_blueprint(mod_guitar, url_prefix='/api')
	logger.debug('App started')
	return app
  