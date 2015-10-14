from flask import Flask
from flask_restful import Api
from flask.ext.sqlalchemy import SQLAlchemy
import config.py


app = Flask(__name__)
app.config.from_pyfile(config.py)
db = SQLAlchemy(app)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
