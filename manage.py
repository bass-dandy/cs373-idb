from flask.ext.script import Manager, Server
from flask_app import app

manager = Manager(app)

manager.add_command("runserver", Server(host="0.0.0.0", port=8000))

@manager.command
def rebuild_database():
    pass


if __name__ == '__main__':
    manager.run()
