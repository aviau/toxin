from flask.ext import restful


class HelloController(restful.Resource):
    def get(self):
        return {'hello': 'world'}

