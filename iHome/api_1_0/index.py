# *_*coding:utf-8 *_*
from . import api


@api.route('/index', methods=['POST', 'GET'])
def hello_world():

    return 'Hello World!'
