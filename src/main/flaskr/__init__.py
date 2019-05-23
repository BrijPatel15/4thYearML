from flask import Flask
from flask import render_template, url_for, request, redirect


# TEMPLATES = "templates/" #goes here by default
def create_app(test_config=None):
	app = Flask(__name__, instance_relative_config=True)
	
	_config = { 'filename':'', 'isPlaying': False , 'file_error':False, 'modes':['AutoPlay Mode','Play Along Mode', 'GenrePlay']};
	@app.route("/")
	def defaultRoute():
		config=_config;
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
		elif (request.method =='GET'):
			return (_config['filename'])

	@app.route('/play', methods = ['GET'])
	def play():
		_config['isPlaying'] = True;
		return redirect(url_for('defaultRoute'))

	@app.route('/pause', methods = ['GET'])
	def pause():
		_config['isPlaying'] = False;
		return redirect(url_for('defaultRoute'))
	
	return app
