from http.server import SimpleHTTPRequestHandler, HTTPServer
import os

class Handler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/health":
            self.send_response(200); self.end_headers(); self.wfile.write(b"ok")
        else:
            self.path = "/index.html"
            return SimpleHTTPRequestHandler.do_GET(self)

if __name__ == "__main__":
    os.chdir(os.path.join(os.path.dirname(__file__), "..", "frontend"))
    HTTPServer(("0.0.0.0", 8080), Handler).serve_forever()
