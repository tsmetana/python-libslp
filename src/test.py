#!/usr/bin/python

import sys
import slp

def service_callback(h, srvurl, lifetime, errcode, data):
    global count
    rv = False
    if errcode == slp.SLP_OK:
        print("Url: " + srvurl + ", timeout " + str(lifetime))
        count += 1
        rv = True
    elif errcode == slp.SLP_LAST_CALL:
        if count == 0:
            print("Services: Nothing found")
        else:
            print("Found " + str(count) + " services")
    else:
        print("Error: " + str(errcode))
    return rv

def attr_callback(h, attrlist, errcode, data):
    global count
    rv = False
    if errcode == slp.SLP_OK:
        print("Attrs: " + attrlist)
        count += 1
        rv = True
    elif errcode == slp.SLP_LAST_CALL:
        if count == 0:
            print("Attrs: Nothing found")
        else:
            print("Found " + str(count) + " attribute lists")
    else:
        print("Error: " + str(errcode))
    return rv

def reg_callback(h, errcode, data):
    if errcode != slp.SLP_OK:
        print("Error registering service: " + str(errcode))
    return None

############

if len(sys.argv) < 2:
    sys.exit('Usage: %s <service url>' % sys.argv[0])

url = sys.argv[1];

############

try:
    hslp = slp.SLPOpen("en", False)
except RuntimeError as e:
    print("Error opening the SLP handle: " + str(e))
    sys.exit("Giving up")

############

count = 0;
try:
    slp.SLPFindSrvs(hslp, url, None, None, service_callback, None)
except RuntimeError as e:
    print("Error discovering the service: " + str(e))

count = 0;
try:
    slp.SLPFindAttrs(hslp, url, None, None, attr_callback, None);
except RuntimeError as e:
    print("Error discovering the service attributes: " + str(e))

############

testSrvUrl = "service:nothing"
testSrvHost = "://127.0.0.1"

print("Testing registration of " + testSrvUrl + " with lifetime " + str(slp.SLP_LIFETIME_DEFAULT))

try:
    slp.SLPReg(hslp, testSrvUrl + testSrvHost, slp.SLP_LIFETIME_DEFAULT, None,
        "(desc=test)", True, reg_callback, None)
except RuntimeError as e:
    print("Error registering new service: " + str(e))

count = 0;
try:
    slp.SLPFindSrvs(hslp, testSrvUrl, None, None, service_callback, None)
except RuntimeError as e:
    print("Error discovering the service: " + str(e))

if count == 0:
    print("Could not find the registered service!")

count = 0;
try:
    slp.SLPFindAttrs(hslp, testSrvUrl, None, None, attr_callback, None)
except RuntimeError as e:
    print("Error discovering the service attributes: " + str(e))

if count == 0:
    print("Could not find the registered service attributes!")

############

slp.SLPClose(hslp);

