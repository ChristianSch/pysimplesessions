# Einführung #
Dieses Projekt versucht, eine Implementierung der PHP-Sessions in Python bereitzustellen.

# Details #
Die Sessions sind wie die PHP-Sessions umgesetzt. Zumindest teilweise.

## Serverseitig ##
Alle Sessions werden in einem Verzeichnis Ihrer Wahl verwaltet. (Default: `.sessions/`)
Jede Session ist eine Datei die ihre ID als Namen trägt.

Da die Session-Klasse wie ein Wörterbuch (Python type dictionary) funktioniert, werden jegliche keys in der Session-Datei verwaltet.

## Clientseitig ##
Genau wie die PHP-Sessions wird die `session_id` Clientseitig in einem Cookie gespeichert.

## Beispiel ##
Dies ist ein kleines Beispiel für die Nutzung der pySimpleSessions.

```
#!/usr/bin/python

import sessions

# initiiere neue Session
session = sessions.Session()

# wenn session das attribut count hat, erhöhe es
try:
    # typisierung nicht vergessen
    # sonst kann count nicht iteriert werden
    session["count"] = int(session["count"]) + 1
# andernfalls setze count
except:
    session["count"] = 1

print "Sie haben uns " + str(session["count"]) + " mal besucht."
```

## Verfall des Cookies setzen ##
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
Beispiel:
```
#!/usr/bin/python

import sessions
import datetime

# verfalle in 2 Jahren (730 Tagen)
expire = datetime.datetime.now() + datetime.timedelta(730)

# initiiere neue Session mit Verfallsdatum - Wdy, DD-Mon-YY HH:MM:SS GMT
# anm. Wdy = weekday, wochentag
session = sessions.Session(expire_date=expire.strftime("%a, %d %b %Y %H:00:00 GMT"))
```