from http.server import HTTPServer, BaseHTTPRequestHandler
from lucki_ai import water

HOST = "10.0.0.61"
PORT = 8000

class RequestHandler(BaseHTTPRequestHandler):
    # Get requests
    def do_GET(self):
        # wget HOST:PORT/filename.wav -> downloads filename.wav
        if (".wav" in self.path):
            with open(self.path[1:], 'rb') as file:
                    self.send_response(200)
                    self.send_header('Content-type', 'audio/wav')
                    self.end_headers()
                    self.wfile.write(file.read())
        
        # curl HOST:PORT/*
        response = ""
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        
        # curl HOST:PORT/WATER
        # curl this URL if the plant needs water, output is the AI response
        if (self.path) == "/WATER":
            response = water()

server = HTTPServer((HOST, PORT), RequestHandler)
print("Server Ready!")
server.serve_forever()
server.server_close()
            



