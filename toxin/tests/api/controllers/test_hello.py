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

from toxin.tests.api import functionalTest
from toxin.api.types import helloMessage

import json


class TestHelloController(functionalTest.FunctionalTest):

    def test_hello(self):
        response = self.app.get('/hellowsme')
        self.assertEqual(
            json.loads(response.data.decode()),
            helloMessage.HelloMessage(message='HeeeeYYY').as_dict()
        )
