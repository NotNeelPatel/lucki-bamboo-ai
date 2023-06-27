from http.server import HTTPServer, BaseHTTPRequestHandler
from llama_cpp import Llama
from lucki_ai import water

HOST = "10.0.0.61"
PORT = 8000

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if (".wav" in self.path):
            with open(self.path[1:], 'rb') as file:
                    self.send_response(200)
                    self.send_header('Content-type', 'audio/wav')
                    self.end_headers()
                    self.wfile.write(file.read())
        response = ""
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        
        if (self.path) == "/WATER":
            response = water()

server = HTTPServer((HOST, PORT), RequestHandler)
print("Server Ready!")
server.serve_forever()
server.server_close()
            



