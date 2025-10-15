from http.server import BaseHTTPRequestHandler, HTTPServer
from http.cookies import SimpleCookie
import json
from DB.models.User import InsertUser, SelectUser
from auth.signup import handle_signup
from auth.login import handle_login
from sessions.validation import handle_validation

class MyHandler(BaseHTTPRequestHandler): 

    def _set_headers(self, status=200, content_type='application/json'):
        self.send_response(status)
        self.send_header('Content-type', content_type)
        self.send_header("Access-Control-Allow-Origin", "http://127.0.0.1:5500")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.send_header("Access-Control-Allow-Credentials", "true")
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
        content_length = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(content_length)
        data = json.loads(body.decode('utf-8')) if body else {}

        response = {}

        if self.path == '/auth/signup': 
            response = handle_signup(data)

        elif self.path == '/auth/login': 
            response = handle_login(data)

        elif self.path == '/validate-session': 
            cookie = SimpleCookie()
            cookie.load(self.headers.get("Cookie", ""))
            session_morsel = cookie.get("sessionid")
            sessionid = session_morsel.value if session_morsel else None

            response = handle_validation(sessionid)

        json_response_data = json.dumps(response)

        # Send headers first
        self._set_headers()
        try:
            self.wfile.write(json_response_data.encode())
        except ConnectionAbortedError:
            print("Client closed the connection early. Skipping response.")

            
            
            
            
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