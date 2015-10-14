from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
from flask_app import app, db

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)


@manager.command
def rebuild_database():
    pass


if __name__ == '__main__':
    manager.run()
