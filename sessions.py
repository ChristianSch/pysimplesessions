#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 2 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have receivedd a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Author: Christian Schulze <xcr4cx@googlemail.com>
# Description: Simple sessions implemented in Python

import Cookie
import os
import sys
import uuid
SESSION_PATH = os.getcwd() + '/.sessions'

class Session(dict):
    def __init__(self, expire_date=None):
        if SESSION_PATH:
            if not os.path.exists(SESSION_PATH):
                os.mkdir(SESSION_PATH)
                self.sessions_path = os.getcwd() + "/.sessions"
            else:
                self.sessions_path = SESSION_PATH
        else:
            sys.stderr.write("No such SESSIONS_PATH")
            sys.exit()

        self.cookie = Cookie.SimpleCookie()

        try:
            self.cookie.load(os.environ["HTTP_COOKIE"])
            self.id = self.cookie["session_id"].value
            self.readSession()
        except:
            pass #sys.stderr.write("exception in __init__") #debug

        # be really sure, self.id is not already set
        try: self.id
        except: self.id = uuid.uuid4()

        # no session but cookie
        if not os.path.exists(self.sessions_path + '/' + str(self.id)):
            self.id = uuid.uuid4()

        # set cookie
        self.cookie["session_id"] = self.id
        if True: #try:
            self.cookie["expires"] = expire_date
        else: #except:
            pass
        print self.cookie, "\n\n"
    
    def setSession(self):
        # set session
        sessions_file = open(self.sessions_path + '/' + str(self.id), 'w')
        session_vars = ""
        for atr in self:
            session_vars += atr + ': ' +  str(self[atr])  + '\n'
        sessions_file.write(session_vars)

    def readSession(self):
        if os.path.exists(self.sessions_path + '/' + str(self.id)) and self.id:
            session_file = open(self.sessions_path + '/' + str(self.id)).read()
            lines = session_file.split('\n')
            for line in lines:
                if line != '':
                    line = line.split(':', 1)
                    atr = line[0]

                    while line[1].startswith(' '):
                        line[1] = line[1][1:]

                    val = line[1]
                    self[atr] = val
        else:
            sys.stderr.write("Cannot read session :" + self.id)

    def __del__(self):
        self.setSession()
