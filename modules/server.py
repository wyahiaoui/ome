# Python 3 server example
from http.server import BaseHTTPRequestHandler, HTTPServer
import time
from bs4 import BeautifulSoup

INDEX_LOC = "/Users/wissem/freelance/ome/web/html/index.html"
CSS_LOC = "/Users/wissem/freelance/ome/web/styles/index.css"
JS_LOC = "/Users/wissem/freelance/ome/web/js/index.js"
hostName = "localhost"
serverPort = 8080

class MyServer(BaseHTTPRequestHandler):
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
            self.wfile.write(f.read(), "utf-8")
        

if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")