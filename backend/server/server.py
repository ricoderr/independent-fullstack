from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class MyHandler(BaseHTTPRequestHandler): 

    def _set_headers(self, status=200, content_type='application/json'):
        self.send_response(status)
        self.send_header('Content-type', content_type)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def do_OPTIONS(self):
        self._set_headers()
    
    def do_GET(self): 
        if self.path == '/':
            data = {
                "name": "landing",
                "message": "Hello from the landing page!",
                "status": "success"
            } 
            json_data = json.dumps(data)
            self._set_headers()
            self.wfile.write(json_data.encode())
            
        elif self.path == '/home': 
            data = {
                "name": "Home",
                "message": "Hello from the home page!",
                "status": "success"
            }
            json_data = json.dumps(data)
            self._set_headers()
            self.wfile.write(json_data.encode())
        else: 
            self._set_headers(status=200, content_type='text/html')
            self.wfile.write(b"<h1>Sorry! No Page Found :( </h1>")

server_address = ('', 8000)
httpd = HTTPServer(server_address, MyHandler)
print("Rijan's dashing server is running at http://localhost:8000/ Successfully!")
httpd.serve_forever()
