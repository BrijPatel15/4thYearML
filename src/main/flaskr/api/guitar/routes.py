from flask import Blueprint, render_template, url_for, request, redirect, jsonify, current_app
from http import HTTPStatus
import signal, subprocess, os
from ..exception import ApiException 
mod_guitar = Blueprint('api_guitar', __name__)
_config = { 'filename':None, 'isPlaying': False , 'file_error':False, 'modes':['AutoPlay Mode','Play Along Mode', 'GenrePlay'], 'logs':""}
subPID = -1000
globalProcess=None

@mod_guitar.route('/upload', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        if (f.filename.split('.')[1]=='mid'):
            f.save('../music/guitar.mid')
            _config['filename']=f.filename
            _config['errors']=False
            status = HTTPStatus.OK
            msg = "Successfully uploaded"
            f.close()
        else:
            _config['errors'] = True
            status= HTTPStatus.INTERNAL_SERVER_ERROR
            msg = "Error occured during upload"
            raise ApiException(msg, status_code=status)
        return jsonify({'status_code': status, 'message':msg, 'data': _config['filename']})
    elif request.method =='GET':
        return (_config['filename'])

@mod_guitar.route('/debug', methods = ['POST'])
def play_notes():
    if request.method == 'POST':
        f = request.json['notes']
        print("got notes: ", f)
        dir_path = os.path.dirname(os.path.realpath(__file__))
        dir_path = dir_path+"/../../../../modules/testMotors.py "
        for item in f:
            dir_path = dir_path + item + " "
        cmd = "python3.7 "+ dir_path
        try:
            globalProcess = subprocess.Popen(cmd, shell=True)
            print("Process ID: ",globalProcess.pid)
            subPID=globalProcess.pid
            status = HTTPStatus.OK
            msg = "Success"
        except subprocess.CalledProcessError as e:
            status = HTTPStatus.INTERNAL_SERVER_ERROR
            msg = e.output
            raise ApiException(msg, status_code=status)
        return jsonify({'status_code': status, 'message':msg, 'data': _config['filename']})
    elif request.method =='GET':
        return (_config['filename'])

@mod_guitar.route('/play', methods = ['GET'])
def play():
    if (_config['filename'] != None):
        _config['isPlaying'] = True
        status = HTTPStatus.OK
        msg = "Success"
        
        dir_path = os.path.dirname(os.path.realpath(__file__))
        dir_path = dir_path+"/../../../../modules/playSong.py"
        cmd = "python3.7 "+ dir_path       
        try:
            globalProcess = subprocess.Popen(cmd, shell=True)
            print("Process ID: ",globalProcess.pid)
            subPID=globalProcess.pid
        except subprocess.CalledProcessError as e:
            status = HTTPStatus.INTERNAL_SERVER_ERROR
            msg = e.output
            raise ApiException(msg, status_code=status)
        # data = jsonify({'pid': subPID})
    else:
        status = HTTPStatus.INTERNAL_SERVER_ERROR
        msg = "Must upload file to play a song."
        data = ""
        raise ApiException(msg, status_code=status)
    return jsonify({'status_code': status, 'message':msg, 'data': {'pid': subPID}})

@mod_guitar.route('/pause', methods = ['POST'])
def pause():
    subPID =request.json['pid']
    status = HTTPStatus.OK
    msg = "Success"
    data = _config['filename']
    if (subPID<=0):
        status=HTTPStatus.INTERNAL_SERVER_ERROR
        msg="Song is not playing."
        raise ApiException(msg, status_code=status)
        # return jsonify({'status_code': status, 'message':msg, 'payload': data})
    # globalProcess.terminate()
    os.kill(subPID+1, signal.SIGTERM) #or signal.SIGKILL 
    subPID=-1000
    return jsonify({'status_code': status, 'message':msg, 'data': data})


@mod_guitar.route('/test', methods = ['GET'])
def runTestMotorScript():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    dir_path = dir_path+"/../../../../modules/testMotors.py"
    cmd = "python3.7 "+ dir_path 
    try:
        globalProcess = subprocess.Popen(cmd, shell=True)
        print("Process ID: ",globalProcess.pid)
        subPID=globalProcess.pid
    except subprocess.CalledProcessError as e:
        status = HTTPStatus.INTERNAL_SERVER_ERROR
        msg = e.output
        raise ApiException(msg, status_code=status)

@mod_guitar.errorhandler(ApiException)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response