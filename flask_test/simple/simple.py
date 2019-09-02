from . import bp
from flask import render_template


@bp.route('/')
def index():
    return 'Hello World index!'


@bp.route('/hello/', methods=['GET', 'POST'])
@bp.route('/hello/<string:name>', methods=['GET', 'POST'])
def hello(name=None):
    context = {
        "name": name
    }
    return render_template("hello.html", **context)


@bp.route('/helloi/<int:uid>')
def helloi(uid):
    print(type(uid))
    return 'Hello {}!'.format(uid)
