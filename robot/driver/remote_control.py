# https://docs.python.org/2/library/socketserver.html

import socketserver
import time
import threading

class RemoteControl:
    def __init__(self, **kwargs):
        try:
            HOST, PORT = "192.168.8.1", 9999
            server = ThreadedTCPServer((HOST, PORT), TCPHandler)
            server.central_handler = kwargs["handler"]

            server_thread = threading.Thread(target=server.serve_forever)
            server_thread.daemon = True
            server_thread.start()
        except OSError:
            print("Could not start server:", error)

class TCPHandler(socketserver.StreamRequestHandler):
    def handle(self):
        self.server.central_handler.controller_connected()

        while True:
            try:
                command = self.rfile.readline().strip()
                if not command: break

                if command != b'':
                    # Commands come in the form `{type}:{body}`
                    type, body = str(command).split(':')
                    self.server.central_handler.controller_commanded(type, body)
            except: ConnectionResetError:
                break

        self.server.central_handler.controller_disconnected()

# Run on a background thread. Thread swapping might cause problems later. We'll see.
class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass
