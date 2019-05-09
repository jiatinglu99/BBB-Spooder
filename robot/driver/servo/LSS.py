"""
Drivers for LSS Servo

"""
import serial
import time

class Servo:
    def __init__(self, id, polarity=True, offset=0):
        self.id = id
        self.current_position = 0.0
        self.desired_position = 0.0
        self.current_amp = 0
        self.polarity = polarity
        self.offset = offset

    def get_position_query_str(self):
        return "#{}QD/r".format(self.id).encode()

    def update_current_position(self, degree): # degree in 1
        self.currentPosition = degree

    def update_desired_position(self, degree): # degree in 1
        self.desired_position = degree

    def get_command_str(self):
        return "#{}D{}\r".format(self.id, int(self.desired_position * 10)).encode()

    def get_current_amp(self):
        return self.current_amp

    def update_amp(self, amp):
        self.current_amp = amp

def test():
    sp = serial.Serial('/dev/ttyO1', 115200)
    servo = Servo(1)
    while True:
        sp.write(servo.get_position_query_str())
        time.sleep(0.1)
        reading = sp.readline().decode('utf-8')
        print(reading)
        time.sleep(1)
