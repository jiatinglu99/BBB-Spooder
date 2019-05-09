import socket
import threading
from time import time

class RemoteControl:
    ### Command types ###
    # Pitch, yaw, roll, throttle
    CMD_UPDATE = '1'
    # Tell the robot, I would like to fly now, or I would rather stay walking (maybe find a way for this to automatically happen)
    CMD_MODE = '2'

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
            self.handler.controller_commanded(Command(type=string[0], body=string[1:]))

class Command:
    def __init__(self, **kwargs):
        self.type = kwargs['type']
        self.body = kwargs['body']
        self.timestamp = time()
