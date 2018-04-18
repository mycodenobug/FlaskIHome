# *_*coding:utf-8 *_*
from flask import Blueprint, current_app, make_response
from flask_wtf.csrf import generate_csrf

# from werkzeug.routing import BaseConverter
#
#
# class RegexConverter(BaseConverter):
#     def __init__(self, url_map, regex):
#         super(RegexConverter, self).__init__(self, url_map)
#         self.regex = regex


html = Blueprint('html', __name__)


@html.route('/<re(".*"):file_name>')
def static_fork(file_name):
    if file_name == '':
        file_name = 'index.html'
    if file_name != 'favicon.ico':
        file_name = 'html/' + file_name
    csrf_token = generate_csrf()
    response = make_response(current_app.send_static_file(file_name))
    response.set_cookie('csrf_token', csrf_token)
    return response
