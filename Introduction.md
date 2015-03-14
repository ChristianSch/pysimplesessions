# Introduction #

This project is intended to provide an implementation of the PHP sessions in Python.

# Details #

The sessions are implemented like the PHP sessions. At least partly.

## Server-side ##
All sessions are managed in a directory of choice. (Default: `.sessions/`)
Every session is handled as a file with its ID as name.

Since the session-class works like a dictionary, all keys are stored in the sessions file on exit.

## Client-side ##
Exactly like the PHP sessions, the `session_id` is stored in a cookie.

## Example Usage ##
Here is a small example usage for the pySimpleSessions.

```
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
```

## Set cookie expiration ##
```
10.1.2  Expires and Max-Age

   Netscape's original proposal defined an Expires header that took a
   date value in a fixed-length variant format in place of Max-Age:

   Wdy, DD-Mon-YY HH:MM:SS GMT

   Note that the Expires date format contains embedded spaces, and that
   "old" cookies did not have quotes around values.  Clients that
   implement to this specification should be aware of "old" cookies and
   Expires.
```
http://tools.ietf.org/html/rfc2109.html#10.1.2

Example:
```
#!/usr/bin/python

import sessions
import datetime

# expire in two years (730 days)
expire = datetime.datetime.now() + datetime.timedelta(730)

# initiate new Session with expire date - Wdy, DD-Mon-YY HH:MM:SS GMT
session = sessions.Session(expire_date=expire.strftime("%a, %d %b %Y %H:00:00 GMT"))
```