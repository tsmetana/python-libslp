#!/usr/bin/python

import sys
import slp

def service_callback(h, srvurl, lifetime, errcode, data):
    rv = False
    if errcode == slp.SLP_OK:
        print "Url: " + srvurl + ", timeout " + str(lifetime)
        rv = True
    elif errcode == slp.SLP_LAST_CALL:
        print "Services: No more results"
    else:
        print "Error: " + str(errcode)

    return rv

def attr_callback(h, attrlist, errcode, data):
    rv = False
    if errcode == slp.SLP_OK:
        print "Attrs: " + attrlist
        rv = True
    elif errcode == slp.SLP_LAST_CALL:
        print "Attrs: No more results"
    else:
        print "Error: " + str(errcode)

    return rv

def reg_callback(h, errcode, data):
    if errcode != slp.SLP_OK:
        print "Error registering service: " + str(errcode)
    return None

if len(sys.argv) < 2:
    sys.exit('Usage: %s <service url>' % sys.argv[0])

url = sys.argv[1];

try:
    hslp = slp.SLPOpen("en", False)
except RuntimeError as e:
    print "Error opening the SLP handle: " + str(e);
    exit(1);

try:
    slp.SLPFindSrvs(hslp, url, None, None, service_callback, None);
except RuntimeError as e:
    print "Error discovering the service: " + str(e);

try:
    slp.SLPFindAttrs(hslp, url, None, None, attr_callback, None);
except RuntimeError as e:
    print "Error discovering the service attributes: " + str(e);

testSrvUrl = "service:nothing:"

print "Testing registration of " + testSrvUrl + " with lifetime " + str(slp.SLP_LIFETIME_DEFAULT);

try:
    slp.SLPReg(hslp, testSrvUrl, slp.SLP_LIFETIME_DEFAULT, None,
        "(desc=test)", True, reg_callback, None);
except RuntimeError as e:
    print "Error registering new service: " + str(e);

try:
    slp.SLPFindSrvs(hslp, testSrvUrl, None, None, service_callback, None);
except RuntimeError as e:
    print "Error discovering the service: " + str(e);

try:
    slp.SLPFindAttrs(hslp, testSrvUrl, None, None, attr_callback, None);
except RuntimeError as e:
    print "Error discovering the service attributes: " + str(e);

slp.SLPClose(hslp);

