import socket
import threading
from cv2 import VideoCapture, resize, imencode

import base64
from time import time

class VideoStreamer:
    def __init__(self):
        self.sock, self.client = None, None
        video_thread = threading.Thread(target=self.send_video)
        video_thread.start()

    def set_client(self, sock, client):
        self.sock = sock
        self.client = client

    def send_video(self):
        capture = VideoCapture(0)
        _, _ = capture.read()                                                    # get past slow first one

        print("Opened camera")

        # loop
        while True:
            if self.sock == None or self.client == None: continue                # ensure we have a destination
            rval, image = capture.read()                                         # get image from camera
            image = resize(image, None, fx=0.7, fy=0.7)                          # scale image down
            rows = 32                                                            # number of rows to slice image into
            row_height = int(image.shape[0] / rows)                              # height of each row of the image
            # send image in rows
            for i in range(rows):
                slice = image[row_height*i : row_height*(i+1), :]                # crop image
                rval, buffer = imencode('.jpg', slice)                           # encode as jpg
                jpg_bytes = bytes([i]) + base64.b64encode(buffer)                # b64 encode and prepend with slice flag
                try:
                    self.sock.sendto(jpg_bytes, self.client)                     # send slice to client
                except OSError as e:                                             # ignore if image is too big; max=9217 on OSX
                    print(e, len(jpg_bytes), image.shape[:2])
