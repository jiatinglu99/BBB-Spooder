'''
RCPY Library Manual: https://guitar.ucsd.edu/rcpy/rcpy.pdf
RCPY Example Files: https://github.com/mcdeoliveira/rcpy/tree/master/examples
Robot Control Library(C) for ESCs: http://strawsondesign.com/docs/librobotcontrol/rc_test_escs_8c-example.html#a11
Python Initialize ESCs: https://raspberrypi.stackexchange.com/questions/29551/how-to-initialize-an-esc-with-python-code
LittleBee Programming Manual: https://www.little-bellanca.com/manual_download/flza3000-tech.pdf

'''

from rcpy.servo import servo
from time import sleep

class ESC:
    def __init__(self, channel):
        self.channel = channel

    def initialize(self):
        self.motor = servo.Servo(self.channel)
        servo.disable()
        self.motor.pulse(0)
        sleep(1)
        self.motor.pulse(1)
        sleep(1)
        #self.clk = self.motor.start(1/200)

