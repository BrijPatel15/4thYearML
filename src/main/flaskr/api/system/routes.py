from flask import Blueprint, jsonify
import psutil
mod_system = Blueprint('api', __name__)

LOGSPATH="fronttail.log"

_config = { 'filename':'', 'isPlaying': False , 'file_error':False, 'modes':['AutoPlay Mode','Play Along Mode', 'GenrePlay'], 'logs':""}

@mod_system.route('/system', methods = ['GET'])
def system():
    cpu_per = psutil.cpu_percent()
    percent_mem = avail_mem = psutil.virtual_memory()._asdict()['percent']
    avail_mem = psutil.virtual_memory()._asdict()['available']
    free_mem = psutil.virtual_memory()._asdict()['free']
    return jsonify({'cpu':cpu_per,'memory_per':percent_mem,'memory_avail':avail_mem,'free_mem':free_mem})

@mod_system.route('/stream',methods = ['GET'])
def stream():
    generate()
    return _config['logs']
def generate():
    f = open(LOGSPATH, "r") 
    temp=f.readlines()
    _config['logs']=""
    for lines in temp[(len(temp)-50):len(temp)]:
        _config['logs']+=lines