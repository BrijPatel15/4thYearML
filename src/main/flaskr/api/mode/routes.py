from flask import Blueprint, render_template, url_for, request, redirect, jsonify, request, json

mod_mode = Blueprint('mode', __name__)
_config = { 'filename':'', 'isPlaying': False , 'file_error':False, 'modes':['AutoPlay Mode','Play Along Mode', 'GenrePlay'], 'logs':"", 'currMode': 'DEFAULT'}
@mod_mode.route('/mode', methods = ['GET', 'POST'])
def mode():
    if request.method == 'POST':
        data = request.data
        dataDict = json.loads(data)
        _config['currMode']=dataDict['data']
        status = "200"
        msg ="Success"
        data =  _config['currMode']
        return jsonify({'status': status, 'message':msg, 'data': data})
    elif request.method =='GET':
        return (_config['currMode'])