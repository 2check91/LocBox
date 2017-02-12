#!/usr/bin/env python

from http.server import BaseHTTPRequestHandler, HTTPServer
from firebase import firebase
import json


# HTTPRequestHandler class
class testHTTPServer_RequestHandler(BaseHTTPRequestHandler):
  def do_HEAD(self):
        # Send response status code
        self.send_response(200)
        # Send headers

        self.send_header('Content-type','text/html')
        self.end_headers()

  def do_GETACC(self,rqdict):
    print ("get acc")
    fb = firebase.FirebaseApplication('https://asdfasda-4bc1f.firebaseio.com', None)
    result_dict = fb.get('/users', rqdict["phone"])
    with open('users_firebase.json', 'w') as outfile:
        json.dump(result_dict, outfile)
    return(result_dict)

  def do_REQAUTH(self,rqdict):
    rpdict = self.do_GETACC(rqdict)
    print ("do reqauth")
    #if rpdict['authenticationState'] in ('') ANY STATUS CHECK
    if rpdict != None and len(rpdict) != 0:
        #pass #call sms
        return("sms")
    return('Unable to request authorize')

  def do_AUTHORIZATION(self,rqdict):
    rpdict = self.do_GETACC(rqdict)
    print ("do AUTHORIZATION")
    if rpdict['authenticationState'] == 'PENDING':
        if      (rpdict['amount'] < rqdict['amount'] and rpdict != None and len(rpdict['amount']) > 0) \
            or    (rpdict['lat'] == rqdict['lat'] and rpdict != None and len(rpdict['lat']) > 0) \
            or  (rpdict['lon'] == rqdict['lon'] and rpdict != None and len(rpdict['lon']) > 0) \
            or  (rqdict['merchants_only'] in rpdict['merchants_only']  and rpdict != None and len(rpdict['merchants_only']) > 0):
            # update status
            return("AUTHENTICATED")
        else:
            # update status
            return("FAILED")
    else:
            return("Unable to authorize")

  def do_PARSEREQUEST(self, req_dict):
    self.do_HEAD()
    if req_dict['typ'] == 'ReqAuth':
        sms=self.do_REQAUTH(req_dict)
        print("sms")
    elif req_dict['typ'] == 'Authorization':
        status = self.do_AUTHORIZATION(req_dict)
        print(status)
    else:
        self.wfile.write('Missing request')
        #self.wfile.write('Missing request')


  def do_GET(self):
    # Send response status code
    self.do_HEAD()
    # Send message back to client
    req_dict1 = {"typ":"ReqAuth", "phone":"4842740749"}
    req_dict2 = {"typ":"Authorization", "phone":"4842740742", "amount": 1500, "lat": 123, "lon": 123, "merchants_only": "Organic Cafe"}
    req_dict3 = {"typ":"Authorization", "phone":"4842740742", "amount": 2500, "lat": 123, "lon": 123, "merchants_only": "Organic Cafe"}

    self.do_PARSEREQUEST(req_dict1)
    self.do_PARSEREQUEST(req_dict2)
    self.do_PARSEREQUEST(req_dict3)
    return

def run():
  print('starting server...')

  # Server settings
  # Choose port 8080, for port 80, which is normally used for a http server, you need root access
  server_address = ('127.0.0.1', 8081)
  httpd = HTTPServer(server_address, testHTTPServer_RequestHandler)
  print('running server...')
  httpd.serve_forever()

run()
