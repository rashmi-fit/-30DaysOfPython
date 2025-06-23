from http.server import HTTPServer, BaseHTTPRequestHandler

HOST = "192.168.0.255"
PORT = 8080


class NeuralHTTP(BaseHTTPRequestHandler):

      def do_GET(self):
            self.send_repose(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()

            self.wfile.write(bytes("<html><body><h1>Neural Network Server</h1></body></html>", "utf-8"))

server = HTTPServer((HOST, PORT), NeuralHTTP)

print("Server now running...")

server.serve_forever()

server.server_close()

print("Server stopped")
