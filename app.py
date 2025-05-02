from http.server import BaseHTTPRequestHandler, HTTPServer

class Server(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(302)
        secret_path = 'http://127.0.0.1:5004/secret'
        self.send_header('Location', secret_path)
        self.end_headers()

HTTPServer(('', 80), Server).serve_forever()
