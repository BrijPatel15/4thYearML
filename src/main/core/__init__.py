from flask import Flask
from flask import render_template, url_for, request, redirect


# TEMPLATES = "templates/" #goes here by default

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    
    @app.route("/")
    def defaultRoute():
        return render_template("index.html")

    @app.route('/upload', methods = ['GET', 'POST'])
    def upload_file():
       if request.method == 'POST':
          f = request.files['file']
          f.save(f.filename)
          return redirect(url_for('defaultRoute'))

    return app
