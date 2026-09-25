from http.server import BaseHTTPRequestHandler, HTTPServer


def add(a, b):
    return a + b


class Handler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/health":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")

        else:
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello from DevOps CI/CD Lab!")


if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", 8080), Handler)

    print("Server listening on port 8080")

    server.serve_forever()