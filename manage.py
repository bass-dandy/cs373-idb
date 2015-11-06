from flask.ext.script import Manager, Server
from flask_app import app, db
import db_utils

manager = Manager(app)

manager.add_command("runserver", Server(host="0.0.0.0", port=8000))

@manager.command
def rebuild_database():
    db_utils.recreate_db()
    db_utils.seed_database_dev()

@manager.command
def rebuild_prod_database():
    db_utils.recreate_db()
    db_utils.seed_database_prod()

#if __name__ == '__main__':
    manager.run()
