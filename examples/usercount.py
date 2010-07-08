#!/usr/bin/python
# -*- coding: utf-8 -*-

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
# You should have receivedd a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

# Author: Christian Schulze <xcr4cx@googlemail.com>
# Description: Simple session-based visit counter

import sessions

# initiate new Session
session = sessions.Session()

# if session has the attribute count, iterate it
try:
    # do not forget typecasting! int(bla)
    # otherwise you cannot iterate the count
    session["count"] = int(session["count"]) + 1
# else set count
except:
    session["count"] = 1

print "You visited us " + str(session["count"]) + " times."
