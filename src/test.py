#!/usr/bin/python

import sys
import slp

def service_callback(h, srvurl, lifetime, errcode, data):
    rv = False
    if errcode == 0:
        print "Url: " + srvurl + ", timeout " + str(lifetime)
        rv = True
    elif errcode == 1:
        print "No more results"
    else:
        print "Error: " + str(errcode)

    return rv

hslp = slp.SLPOpen("en", False)
err = slp.SLPFindSrvs(hslp, "service:ssh.openslp", None, None, service_callback, None);

slp.SLPClose(hslp);

