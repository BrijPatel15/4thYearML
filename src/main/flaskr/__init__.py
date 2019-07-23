import sys
import time
from flask import Flask
from flask import render_template, url_for, request, redirect, jsonify
from logging.config import dictConfig
import logging 

from flaskr.api.system.routes import mod_system
from flaskr.views.homepage.routes import mod
from flaskr.api.mode.routes import mod_mode
from flaskr.api.guitar.routes import mod_guitar
LOGSPATH="fronttail.log"

_config = { 'filename':'', 'isPlaying': False , 'file_error':False, 'modes':['AutoPlay Mode','Play Along Mode', 'GenrePlay'], 'logs':""}

# TEMPLATES = "templates/" #goes here by default
def create_app(test_config=None):
	app = Flask(__name__, instance_relative_config=True)
	
	app.register_blueprint(mod)
	app.register_blueprint(mod_system, url_prefix='/api')
	app.register_blueprint(mod_mode, url_prefix='/api')
	app.register_blueprint(mod_guitar, url_prefix='/api')
	handler = logging.FileHandler(LOGSPATH)	
	app.logger.setLevel(logging.DEBUG)
	formatter = logging.Formatter('[%(asctime)s] [%(levelname)s] [%(name)s]: %(message)s')
	# tell the handler to use this format
	handler.setFormatter(formatter)
	app.logger.addHandler(handler)
	
	return app
  