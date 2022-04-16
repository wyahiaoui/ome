# Python 3 server example
from http.server import BaseHTTPRequestHandler, HTTPServer
import modules.info as info
import json


INDEX_LOC = "/Users/wissem/freelance/ome/web/html/index.html"
CSS_LOC = "/Users/wissem/freelance/ome/web/styles/index.css"
JS_LOC = "/Users/wissem/freelance/ome/web/js/index.js"
hostName = "localhost"
serverPort = 8080

class LocationServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        filename = INDEX_LOC
        mime_type = "text/html"

        if self.path.endswith(".css"):
            mime_type = "text/css"
            filename = CSS_LOC
        elif self.path.endswith(".js"):
            mime_type = "application/javascript"
            filename = JS_LOC
        
        with open(filename, "rb") as f:
            self.send_header("Content-type", mime_type)    
            self.end_headers()
            self.wfile.write(f.read())
    
    def do_POST(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(bytes(json.dumps(info.ACTUAL_INFO, ensure_ascii=False), 'utf-8'))

def run_server():        
    webServer = HTTPServer((hostName, serverPort), LocationServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")