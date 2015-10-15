from flask.ext.script import Manager
from flask_app import app

manager = Manager(app)


@manager.command
def rebuild_database():
    pass


if __name__ == '__main__':
    manager.run()
