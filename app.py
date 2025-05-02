import os
from http.server import BaseHTTPRequestHandler, HTTPServer

class Server(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(302)
            self.send_header('Location', '/secret')
            self.end_headers()
        elif self.path == '/secret':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'CE441{you_found_the_secret_flag}')
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'Not found')


PORT = int(os.environ.get('PORT', 8000))
print(f"Listening on port {PORT}")
HTTPServer(('', PORT), Server).serve_forever()
