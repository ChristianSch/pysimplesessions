#!/usr/bin/python

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