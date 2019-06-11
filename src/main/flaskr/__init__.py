import sys
import time
from flask import Flask
from flask import render_template, url_for, request, redirect, jsonify
from logging.config import dictConfig
import logging 
import psutil
LOGSPATH="fronttail.log"

_config = { 'filename':'', 'isPlaying': False , 'file_error':False, 'modes':['AutoPlay Mode','Play Along Mode', 'GenrePlay'], 'logs':""}

# TEMPLATES = "templates/" #goes here by default
def create_app(test_config=None):
	app = Flask(__name__, instance_relative_config=True)
	
	@app.route("/")
	def defaultRoute():
		config=_config
		return render_template("index.html", config=config)

	@app.route('/upload', methods = ['GET', 'POST'])
	def upload_file():
		if request.method == 'POST':
			f = request.files['file']
			if (f.filename.split('.')[1]=='mid'):
				f.save('music/guitar.mid')
				_config['filename']=f.filename
				_config['errors']=False
			else:
				_config['errors'] = True
			return redirect(url_for('defaultRoute'))
		elif request.method =='GET':
			return (_config['filename'])

	@app.route('/play', methods = ['GET'])
	def play():
		app.logger.info('%s play!', "user.usernam")
		_config['isPlaying'] = True
		return redirect(url_for('defaultRoute'))

	@app.route('/pause', methods = ['GET'])
	def pause():
		_config['isPlaying'] = False
		return redirect(url_for('defaultRoute'))
	
	@app.route('/stream',methods = ['GET'])
	def stream():
		generate()
		return _config['logs']
	def generate():
		f = open(LOGSPATH, "r") 
		temp=f.readlines()
		_config['logs']=""
		for lines in temp[(len(temp)-50):len(temp)]:
			_config['logs']+=lines

	@app.route('/system', methods = ['GET'])
	def system():
		cpu_per = psutil.cpu_percent()
		percent_mem = avail_mem = psutil.virtual_memory()._asdict()['percent']
		avail_mem = psutil.virtual_memory()._asdict()['available']
		free_mem = psutil.virtual_memory()._asdict()['free']
		return jsonify({'cpu':cpu_per,'memory_per':percent_mem,'memory_avail':avail_mem,'free_mem':free_mem})


	handler = logging.FileHandler(LOGSPATH)	
	app.logger.setLevel(logging.DEBUG)
	formatter = logging.Formatter('[%(asctime)s] [%(levelname)s] [%(name)s]: %(message)s')
	# tell the handler to use this format
	handler.setFormatter(formatter)
	app.logger.addHandler(handler)
	
	return app
  