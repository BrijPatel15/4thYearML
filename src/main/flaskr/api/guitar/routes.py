from flask import Blueprint, render_template, url_for, request, redirect, jsonify

mod_guitar = Blueprint('api_guitar', __name__)
_config = { 'filename':'', 'isPlaying': False , 'file_error':False, 'modes':['AutoPlay Mode','Play Along Mode', 'GenrePlay'], 'logs':""}
@mod_guitar.route('/upload', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        if (f.filename.split('.')[1]=='mid'):
            f.save('music/guitar.mid')
            _config['filename']=f.filename
            _config['errors']=False
            status = "Ok"
            msg = "Successfully uploaded"
        else:
            _config['errors'] = True
            status= "Error"
            msg = "Error occured during upload"
        return jsonify({'status': status, 'message':msg})
    elif request.method =='GET':
        return (_config['filename'])

@mod_guitar.route('/play', methods = ['GET'])
def play():
    # mod.logger.info('%s play!', "user.usernam")
    _config['isPlaying'] = True
    status = "200"
    msg = "Success"
    data = "Pause"
    return jsonify({'status': status, 'message':msg, 'data': data})

@mod_guitar.route('/pause', methods = ['GET'])
def pause():
    status = "200"
    msg = "Success"
    data = "Play"
    return jsonify({'status': status, 'message':msg, 'data': data})