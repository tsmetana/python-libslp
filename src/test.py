#!/usr/bin/python

import sys
import slp

def service_callback(h, srvurl, lifetime, errcode, data):
    rv = False
    if errcode == 0:
        print "Url: " + srvurl + ", timeout " + str(lifetime)
        rv = True
    elif errcode == 1:
        print "Services: No more results"
    else:
        print "Error: " + str(errcode)

    return rv

def attr_callback(h, attrlist, errcode, data):
    rv = False
    if errcode == 0:
        print "Attrs: " + attrlist
        rv = True
    elif errcode == 1:
        print "Attrs: No more results"
    else:
        print "Error: " + str(errcode)

    return rv

if len(sys.argv) < 2:
    sys.exit('Usage: %s <service url>' % sys.argv[0])

url = sys.argv[1];

hslp = slp.SLPOpen("en", False)

slp.SLPFindSrvs(hslp, url, None, None, service_callback, None);
slp.SLPFindAttrs(hslp, url, None, None, attr_callback, None);

slp.SLPClose(hslp);

