from flask_restful import Resource, abort
from flask import Response
import os

class TestAPI(Resource):
    """API Endpoint to run test cases"""
    def get(self):
        print("running tests!")
        os.system("make test")
        with open('Tests.tmp', 'r') as testOutput:
            output = str.join([line for line in testOutput])
        os.system("make clean")

        return output
