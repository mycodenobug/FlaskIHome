# -*- coding: utf-8 -*-
# from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand, Manager
from iHome import create_app, db, models

app = create_app('development')

manage = Manager(app)

Migrate(app, db)

manage.add_command('db', MigrateCommand)

if __name__ == '__main__':
    print app.url_map
    manage.run()
