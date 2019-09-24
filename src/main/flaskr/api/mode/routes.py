from flask import Blueprint, render_template, url_for, request, redirect, jsonify, request, json, current_app
from ..exception import ApiException
from http import HTTPStatus
import logging
mod_mode = Blueprint('mode', __name__)
_config = { 'filename':'', 'isPlaying': False , 'file_error':False, 'modes':['AutoPlay Mode','Play Along Mode', 'GenrePlay'], 'logs':"", 'currMode': 'DEFAULT'}
# logger = current_app.logger

@mod_mode.route('/mode', methods = ['GET', 'POST'])
def mode():
    if request.method == 'POST':
        data = request.data
        dataDict = json.loads(data)
        _config['currMode']=dataDict['data']
        status = HTTPStatus.OK
        msg ="Success"
        data =  _config['currMode']
        current_app.logger.info('Set mode to '+ _config['currMode'])
        return jsonify({'status_code': status, 'message':msg, 'data': data})
    elif request.method =='GET':
        return (_config['currMode'])

@mod_mode.errorhandler(ApiException)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response