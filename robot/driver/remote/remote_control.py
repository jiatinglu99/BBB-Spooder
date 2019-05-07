 # https://docs.python.org/2/library/socketserver.html

import socket
import threading

class RemoteControl:
    ### Command types ###
    """
        It might not make sense to have hello or goodbye messages because they are not guaranteed to come in the right order or at all.
    """
    # Controller connected
    CMD_HELLO = '0'
    # Pitch, yaw, roll, throttle
    CMD_UPDATE = '1'
    # Tell the robot, I would like to fly now, or I would rather stay walking (maybe find a way for this to automatically happen)
    CMD_MODE = '2'
    # Controller disconnected
    CMD_GOODBYE = '3'

    def __init__(self, **kwargs):
        self.handler = kwargs['handler']
        HOST, PORT = '192.168.8.1', 9999
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind((HOST, PORT))
        thread = threading.Thread(target=self.loop)
        thread.start()

    def loop(self):
        while True:
            data, addr = self.sock.recvfrom(17)
            string = data.decode('utf-8')
            self.handler.controller_commanded(string[0],string[1:])
