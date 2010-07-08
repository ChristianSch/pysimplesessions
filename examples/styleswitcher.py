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
# Description: Simple session-based styleswitcher (with cgi)

import cgi
import sessions

DEFAULT = "base_style.css"
stylesheets = ("black.css", "white.css", "pink.css")

def is_valid_style(style):
    return stylesheets.count(style) > 0

def styleswitch():
    params = cgi.FieldStorage()

    if params.has_key("style"):
        # prevent unnecessary sessions
        session = sessions.Session()

        stylesheet = params.getvalue("style")

        # change style if is valid
        if is_valid_style(stylesheet):
            session["style"] = stylesheet
            return True
        else:
            # could not set stylesheet, since it's invalid
            session["style"] = DEFAULT
            return False
    else:
        try:
            stylesheet = session["style"]
            if is_valid_stylesheet(stylesheet):
                return True
            else:
                # remove invalid style from session
        session = sessions.Session()
                session["style"] = DEFAULT
                return False
        except:
            # the session has no "style" key
            pass

styleswitch()
