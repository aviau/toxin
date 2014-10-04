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

from flask.ext import restful

from wsmeext.flask import signature
import wsme.api
from toxin.api.types import registration


class RegisterController(restful.Resource):

    @signature(registration.Registration)
    def get(self):
        return registration.Registration.sample()

    @signature(body=registration.Registration, status_code=201)
    def post(self, r):
        return
