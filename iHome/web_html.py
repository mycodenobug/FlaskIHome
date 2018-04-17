# *_*coding:utf-8 *_*
from flask import Blueprint, current_app


html = Blueprint('html', __name__)


@html.route('/<file_name>')
def static_fork(file_name):
    file_name = 'html/' + file_name

    return current_app.send_static_file(file_name)
