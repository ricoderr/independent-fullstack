from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from DB.User import InsertUser, SelectUser

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
                "status": "success",
            } 
            json_data = json.dumps(data)
            self._set_headers()
            self.wfile.write(json_data.encode())
            
        elif self.path == '/home': 
            data = {
                "name": "Home",
                "message": "Hello from the home page!",
                "status": "success", 
            }
            json_data = json.dumps(data)
            self._set_headers()
            self.wfile.write(json_data.encode())
        else: 
            data = {
                "name": "-",
                "message": "Page Not Found!",
                "status": "Failed", 
            } 
            json_data = json.dumps(data)
            self._set_headers()
            self.wfile.write(json_data.encode())
    
    def do_POST(self): 
        if self.path == '/post': 
            content_lenth = int(self.headers['content-length'])
            data_byte = self.rfile.read(content_lenth)
            data_str = data_byte.decode('utf-8')
            data = json.loads(data_str)
            InsertUser(username=data["username"], email=data["email"])
            
            
            # response to the post.
            response_data = {
                "method": "POST", 
                "status": "Success" 
            }
            
            json_response_data = json.dumps(response_data)
            self._set_headers()
            self.wfile.write(json_response_data.encode())
            
            
            
            
            
            
if __name__ == "__main__":
    try:
        server = HTTPServer(("localhost", 8000), MyHandler)
        print('''
       -----------------------------------------------------------------------------
      | NOTE: This is just an development server which is not ready for deployment. |
       -----------------------------------------------------------------------------
                                                     -----------------------
            R I J A N's server is running at -->    | http://localhost:8000 | 
                                                     -----------------------
                                             
       Press 'Ctrl + C' to Stop the server. 
      ''')
        server.serve_forever()
    except KeyboardInterrupt:
        print("Server Stopped.")
        server.server_close()