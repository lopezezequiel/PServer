# PServer
Portable HTTP/HTTPS server for static files

### Usage

```
usage: pserver [-h] [--https] [-p PORT] [-r ROOT]
 
optional arguments:
-h, --help show this help message and exit
--https Init https server
-p PORT, --port PORT Set the port
-r ROOT, --root ROOT Set the root directory
```

Default port is 3443, default root is the current directory.

### Examples

__default port, mode and root:__

**command:**
```
python pserver.py
```

**output:**
```
The server is running now...
    port: 3443
    mode: http
    root: C:\Users\guest\Documents\Pserver

Press Ctrl+C to shutdown
```
---

**command:**
```
python pserver.py --https --port 9999 --root C:\Users\guest\www**
```

**output:**
```
The server is running now...
    port: 9999
    mode: https
    root: C:\Users\guest\www

Press Ctrl+C to shutdown
```

### Difference between pserver and pserverw
The pserver is associated with a console to display requests.

The pserverw command is identical to pserver, except that with pserver there is no associated console window.
