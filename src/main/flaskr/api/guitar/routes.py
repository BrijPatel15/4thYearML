from flask import Blueprint, render_template, url_for, request, redirect, jsonify
import signal, subprocess, os
mod_guitar = Blueprint('api_guitar', __name__)
_config = { 'filename':None, 'isPlaying': False , 'file_error':False, 'modes':['AutoPlay Mode','Play Along Mode', 'GenrePlay'], 'logs':""}
subPID = -1000
globalProcess = None

@mod_guitar.route('/upload', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # print(request.files)
        f = request.files['file']
        if (f.filename.split('.')[1]=='mid'):
            f.save('../music/guitar.mid')
            _config['filename']=f.filename
            _config['errors']=False
            status = "Ok"
            msg = "Successfully uploaded"
            f.close()
        else:
            _config['errors'] = True
            status= "Error"
            msg = "Error occured during upload"
        return jsonify({'status': status, 'message':msg, 'data': _config['filename']})
    elif request.method =='GET':
        return (_config['filename'])

@mod_guitar.route('/play', methods = ['GET'])
def play():
    # mod.logger.info('%s play!', "user.usernam")
    if (_config['filename'] != None):
        _config['isPlaying'] = True
        status = "200"
        msg = "Success"
        data = _config['filename']
        dir_path = os.path.dirname(os.path.realpath(__file__))
        dir_path = dir_path+"/../../../../modules/playSong.py"
        cmd = "python3.7 "+ dir_path
        # cmd = "pwd"
        
        try:
            globalProcess = subprocess.Popen(cmd, shell=True)
            print("Process ID: ",globalProcess.pid)
            # subPID = globalProcess.pid
            # out, error = globalProcess.communicate()
            # print ("out:" + str(out))
            # print ("error:" + str(error))
        except subprocess.CalledProcessError as e:
            status = "500"
            msg = e.output
    else:
        status ="500"
        msg = "Must upload file to play a song."
        data =""
    return jsonify({'status': status, 'message':msg, 'data': data})

@mod_guitar.route('/pause', methods = ['GET'])
def pause():
    status = "200"
    msg = "Success"
    data = _config['filename']
    if (globalProcess!=None):
        globalProcess.terminate()
    else:
        status="500"
        msg="Song is not playing."
    return jsonify({'status': status, 'message':msg, 'data': data})