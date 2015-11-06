from flask_restful import Resource, abort
from flask import Response
import os

class TestAPI(Resource):
    """API Endpoint to run test cases"""
    def get(self):
        print("running tests!")
        #os.system("make clean")
        os.system("make test")
        output = ""
        with open('Tests.tmp', 'r') as testOutput:
            for line in testOutput:
                output += line
            #output = str.join([line for line in testOutput])
        os.system("make clean")

        print(output)

        return output
