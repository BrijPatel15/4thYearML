from flask import Blueprint, jsonify, send_from_directory, current_app
import psutil
mod_system = Blueprint('api', __name__)

LOGSPATH="static/fronttail.log"

_config = { 'filename':'', 'isPlaying': False , 'file_error':False, 'modes':['AutoPlay Mode','Play Along Mode', 'GenrePlay'], 'logs':""}

@mod_system.route('/system', methods = ['GET'])
def system():
    cpu_per = psutil.cpu_percent()
    percent_mem = avail_mem = psutil.virtual_memory()._asdict()['percent']
    avail_mem = psutil.virtual_memory()._asdict()['available']
    free_mem = psutil.virtual_memory()._asdict()['free']
    return jsonify({'cpu':cpu_per,'memory_per':percent_mem,'memory_avail':avail_mem,'free_mem':free_mem})

@mod_system.route('/log',methods = ['GET'])
def fetchLogs():
        return send_from_directory('static', 'fronttail.log' )
