import socketserver
import threading
import cv2
import base64

class UDPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        data = self.request[0].strip()
        socket = self.request[1]
        # addr = self.client_address[0]
        self.server.handle(socket, socket, self.client_address)

class Manager:
    def __init__(self):
        # server
        HOST, PORT = "192.168.2.149", 9999
        server = socketserver.ThreadingUDPServer((HOST, PORT), UDPHandler)
        server.handle = self.handle
        server_thread = threading.Thread(target=server.serve_forever)
        server_thread.start()

        # video
        self.socket, self.client = None, None
        video_thread = threading.Thread(target=self.send_video)
        video_thread.start()

    def handle(self, message, overSocket, fromClient):
        # print(message)
        self.socket, self.client = overSocket, fromClient

    def test_max_msg_length(self):
        while True:
            if self.socket == None or self.client == None: continue
            break

        for i in range(1,10000):
            try:
                self.socket.sendto(('x'*i).encode('utf-8'), self.client)
            except OSError as e:
                print(e, i)
                break

    def send_video(self):
        capture = cv2.VideoCapture(0)
        if capture.isOpened(): _, _ = capture.read()                                            # get past slow first one
        else: capture.open()                                                                    # open the camera
        # loop
        while True:
            if self.socket == None or self.client == None: continue                             # ensure we have a destination

            rval, image = capture.read()
            image = cv2.resize(image, None, fx=0.7, fy=0.7)                                     # scale image down
            rows = 32                                                                           # number of rows to slice image into
            row_height = int(image.shape[0] / rows)                                             # height of each row of the image
            # send image in rows
            for i in range(rows):
                slice = image[row_height*i : row_height*(i+1), :]                               # crop image
                rval, buffer = cv2.imencode('.jpg', slice)                                      # encode as jpg
                jpg_str = bytes([i]) + base64.b64encode(buffer)                                 # b64 encode and prepend with slice flag

                try:
                    self.socket.sendto(jpg_str, self.client)                                    # send slice to client
                except OSError as e:                                                            # ignore if image is too big; max=9217 on OSX
                    print(e, len(jpg_str), image.shape[:2])


if __name__ == "__main__":
    manager = Manager()
