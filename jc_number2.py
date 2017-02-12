from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import socketserver
import random


class S(BaseHTTPRequestHandler):
    def do_HEAD(self):
       self.send_response(200)
       self.send_header('Content-type', 'text/html')
       self.end_headers()
    def do_AUTH(self):
       self.send_response(401)
       self.send_header('WWW-Authenticate', 'Basic realm=\"Test\"')
       self.send_header('Content-type', 'text/html')
       self.end_headers()

    def do_GET(self):
       if self.headers.getheader('Authorization') == None:
           self.do_AUTH()
           self.wfile.write('no auth header received')
           pass
       elif self.headers.getheader('Authorization') == 'Basic dGVzdDp0ZXN0':
           self.do_HEAD()
           self.wfile.write(self.headers.getheader('Authorization'))
           self.wfile.write('authenticated!')
           pass
       else:
           self.do_AUTH()
           self.wfile.write(self.headers.getheader('Authorization'))
           self.wfile.write('not authenticated')
           pass

    def do_POST(self):
        self.do_HEAD()
        self.data_string = self.rfile.read(int(self.headers['Content-Length']))
        self.send_response(200)
        self.end_headers()

        data = json.loads(self.data_string)
        with open("test123456.json", "w") as outfile:
            json.dump(data, outfile)
        f = open("for_presen.py")
        self.wfile.write(f.read())
        return


def run(server_class=HTTPServer, handler_class=S, port=80):
    server_address = ('', port)
