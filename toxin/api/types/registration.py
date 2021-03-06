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

import wsme
import wsme.types as wtypes

from toxin.api.types import base


class Registration(base.Base):
    username = wsme.wsattr(wtypes.text, mandatory=True)
    """Username"""

    password = wsme.wsattr(wtypes.text, mandatory=True)
    """Password"""

    email = wsme.wsattr(wtypes.text, mandatory=True)
    """email address"""

    @classmethod
    def sample(cls):
        return cls(
            username="ReAzem",
            password="linux123",
            email="reazem@reazem.net",
        )
