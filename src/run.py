
import sys

if (len(sys.argv)<2 ):
    FLASK_ENV="production"
elif (sys.argv[1]=="dev"):
    FLASK_ENV="development"
elif (sys.argv[1]=="prod"):
    FLASK_ENV="production"
else:
    raise Exception('Invalid parameter= {}'.format(sys.argv[1]))

FLASK_APP="main/flaskr"

APP_ENV = "FLASK_APP"
MODE_ENV = "FLASK_ENV"
import os
import subprocess

os.environ[APP_ENV] = FLASK_APP
os.environ[MODE_ENV] = FLASK_ENV

subprocess.run(["flask", "run"])