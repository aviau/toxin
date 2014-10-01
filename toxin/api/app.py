#
#    Copyright (C) 2014 Alexandre Viau <alexandre@alexandreviau.net>
#
#    This file is part of Toxin.
#
#    Toxin is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    Toxin is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with Toxin.  If not, see <http://www.gnu.org/licenses/>.
#

from flask import Flask
from flask.ext import restful

from toxin.api.controllers import hello
from toxin.api.controllers import hello_wsme

app = Flask(__name__)
api = restful.Api(app)

api.add_resource(hello.HelloController, '/hello')
app.register_blueprint(hello_wsme.hello_wsme, url_prefix='/hellowsme')

if __name__ == '__main__':
    app.run(debug=True)
