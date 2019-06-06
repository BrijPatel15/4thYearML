
import sys
if (sys.argv[1]=="dev"):
    FLASK_ENV="development"
else:
    FLASK_ENV="production"
FLASK_APP="main/flaskr"

APP_ENV = "FLASK_APP"
MODE_ENV = "FLASK_ENV"
import os
import subprocess

os.environ[APP_ENV] = FLASK_APP
os.environ[MODE_ENV] = FLASK_ENV

subprocess.run(["flask", "run"])