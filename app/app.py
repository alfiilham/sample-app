import os
import socket
from http.server import BaseHTTPRequestHandler, HTTPServer

MESSAGE = "Hello from Tekton + Argo CD!"
COLOR = "#2563eb"
VERSION = os.environ.get("APP_VERSION", "dev")


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        body = f"""<html><body style="font-family:sans-serif;background:{COLOR};color:white;text-align:center;padding-top:15vh">
<h1>{MESSAGE}</h1><p>version: {VERSION}</p><p>pod: {socket.gethostname()}</p></body></html>"""
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        self.wfile.write(body.encode())


if __name__ == "__main__":
    HTTPServer(("0.0.0.0", 8080), Handler).serve_forever()
