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

import json

from toxin.api.types import helloMessage
from toxin.tests.api import functionalTest


class TestHelloWsmeController(functionalTest.FunctionalTest):

    def test_hello_wsme(self):
        response = self.app.get(
            '/hellowsme',
            headers={'Accept': 'application/json'}
        )

        self.assertEqual(response.status_code, 200)

        self.assertEqual(
            json.loads(response.data.decode()),
            helloMessage.HelloMessage(message='HeeeeYYY').as_dict()
        )
