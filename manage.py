# -*- coding: utf-8 -*-
# from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand, Manager
from iHome import app, db

manage = Manager(app)

Migrate(app, db)

manage.add_command('db', MigrateCommand)


@app.route('/', methods=['POST', 'GET'])
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    # app.run()
    manage.run()
