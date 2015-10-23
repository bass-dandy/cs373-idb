from flask_restful import Resource


class HelloWorldAPI(Resource):
    """Single artist through id"""

    def get(self):
        """Get artist with id"""
        return "Hello World!"
