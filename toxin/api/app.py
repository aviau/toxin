from flask import Flask
from flask.ext import restful

from toxin.api.controllers import helloController

app = Flask(__name__)
api = restful.Api(app)

api.add_resource(helloController.HelloController, '/hello')

if __name__ == '__main__':
    app.run(debug=True)
