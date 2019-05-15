import socket
from threading import Thread
import cv2

import base64
from time import time

class VideoStreamer:
    def __init__(self):
        self.sock, self.clinet = None, None
        Thread(target=self.update).start()

    def set_client(self, sock, client):
        self.sock, self.client = sock, client

    def update(self):
        capture = cv2.VideoCapture(0)
        _, _ = capture.read()                                                                   # get past slow first one

        # loop
        while True:
            if self.sock == None or self.client == None: continue                             # ensure we have a destination

            rval, image = capture.read()
            image = cv2.resize(image, None, fx=0.7, fy=0.7)                                     # scale image down
            rows = 32                                                                           # number of rows to slice image into
            row_height = int(image.shape[0] / rows)                                             # height of each row of the image
            # send image in rows
            for i in range(rows):
                slice = image[row_height*i : row_height*(i+1), :]                               # crop image
                rval, buffer = cv2.imencode('.jpg', slice)                                      # encode as jpg
                jpg_bytes = bytes([i]) + base64.b64encode(buffer)                               # b64 encode and prepend with group and slice flag
                try:
                    self.sock.sendto(jpg_bytes, self.client)                                  # send slice to client
                except OSError as e:                                                            # ignore if image is too big; max=9217 on OSX
                    print(e, len(jpg_bytes), image.shape[:2])

'''
class VideoStreamer:
    def __init__(self):
        self.sock, self.client = None, None
        self.camera = ThreadedCamera()
        self.sender = FrameSender()

        Thread(target=self.update).start()

    def set_client(self, sock, client):
        self.sender.sock = sock
        self.sender.client = client

    def update(self):
        while True:
            Thread(target=self.sender.send_frame, args=(self.camera.read(),)).start()
            # self.sender.send_frame(self.camera.read())

class FrameSender:
    def __init__(self):
        self.sock, self.client = None, None

    def send_frame(self, frame):
        if any(x is None for x in [self.sock, self.client, frame]): return   # ensure we have a destination
        frame = cv2.resize(frame, None, fx=0.7, fy=0.7)                      # scale frame down
        ROWS = 32                                                            # number of rows to slice frame into
        row_height = int(frame.shape[0] / ROWS)                              # height of each row of the frame
        # send frame in ROWS rows
        for i in range(ROWS):
            slice = frame[row_height*i : row_height*(i+1), :]                # crop frame
            rval, buffer = cv2.imencode('.jpg', slice)                       # encode as jpg
            encoded_msg = bytes([i]) + base64.b64encode(buffer)              # b64 encode and prepend with slice flag
            try:
                self.sock.sendto(encoded_msg, self.client)                   # send slice to client
            except OSError as e:                                             # ignore if frame is too big; max=9217 on OSX
                print(e, len(encoded_msg), frame.shape[:2])

class ThreadedCamera:
    def __init__(self, src=0):
        self.stream = cv2.VideoCapture(src)
        self.grabbed, self.frame = self.stream.read()
        print('CAMERA ON')
        Thread(target=self.update).start()

    def update(self):
        while True:
            self.grabbed, self.frame = self.stream.read()
            # print(self.frame.shape)

    def read(self):
        return self.frame
'''
