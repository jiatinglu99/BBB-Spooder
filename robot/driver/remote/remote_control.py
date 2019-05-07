# https://docs.python.org/2/library/socketserver.html

import socketserver
import threading

class RemoteControl:
    ### Command types
    # Pitch, yaw, roll, throttle
    CMD_MOTION = 0
    # Tell the robot, I would like to fly now, or I would rather stay walking (maybe find a way for this to automatically happen)
    CMD_SET_MODE = 1


    def __init__(self, **kwargs):
        try:
            HOST, PORT = "192.168.8.1", 9999
            server = socketserver.ThreadingUDPServer((HOST, PORT), UDPHandler)
            server.central_handler = kwargs["handler"]

            server_thread = threading.Thread(target=server.serve_forever)
            server_thread.start()
            # check if just serve_forever blocks
        except OSError:
            print("Could not start server:", error)

class UDPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        self.server.central_handler.controller_connected()

        while True:
            try:
                command = self.request[0].strip()
                if not command: break
                if command != b'':
                    # Commands come in the form `{type}:{body}`
                    print(data)
                    # type, body = str(command).split(':')
                    # self.server.central_handler.controller_commanded(type, body)
            except ConnectionResetError as e:
                print(e)

        self.server.central_handler.controller_disconnected()
