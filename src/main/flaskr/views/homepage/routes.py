from flask import Blueprint, render_template

mod = Blueprint('view', __name__)

_config = { 'filename':'', 'isPlaying': False , 'file_error':False, 'modes':['AutoPlay Mode','Play Along Mode', 'GenrePlay'], 'logs':""}
@mod.route("/")
def defaultRoute():
    config=_config
    return render_template("index.html")