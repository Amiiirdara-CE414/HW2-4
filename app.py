from http.server import BaseHTTPRequestHandler, HTTPServer

class Server(BaseHTTPRequestHandler):
    def do_GET(self):
        print("start redirecting")
        self.send_response(302)
        self.send_header("Location", "http://127.0.0.1:5004/secret")
        self.end_headers()

print("listening on port 80")
HTTPServer(("", 80), Server).serve_forever()
