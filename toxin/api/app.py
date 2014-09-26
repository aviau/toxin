from flask import Flask
from flask.ext import restful

from toxin.api.controllers import helloController
from toxin.api.controllers import helloWsmeController

app = Flask(__name__)
api = restful.Api(app)

api.add_resource(helloController.HelloController, '/hello')
api.add_resource(helloWsmeController.HelloWsmeController, '/hellowsme')

if __name__ == '__main__':
    app.run(debug=True)
