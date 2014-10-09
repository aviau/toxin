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

import unittest
import mongomock
import mock

from toxin.api import app


class FunctionalTest(unittest.TestCase):

    def setUp(self):
        app.app.config['TESTING'] = True

        # Mock the database
        self.db = mongomock.Connection()
        app.connect_db = mock.Mock(return_value=self.db)

        self.app = app.app.test_client()

    def post_json(self, path, **kwargs):

        response = self.app.post(
            path,
            headers={
                'Accept': 'application/json',
                'Content-Type': 'application/json'},
            **kwargs
        )

        return response
