from flask.ext import restful
from wsmeext.flask import signature

from toxin.api.types import helloMessage


class HelloWsmeController(restful.Resource):

    @signature(helloMessage.helloMessage)
    def get():
        message = helloMessage.helloMessage()
        message.message = "HeeeeYYYY"
        return message
