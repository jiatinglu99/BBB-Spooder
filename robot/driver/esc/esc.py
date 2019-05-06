'''
RCPY Library Manual: https://guitar.ucsd.edu/rcpy/rcpy.pdf
RCPY Example Files: https://github.com/mcdeoliveira/rcpy/tree/master/examples
Robot Control Library(C) for ESCs: http://strawsondesign.com/docs/librobotcontrol/rc_test_escs_8c-example.html#a11
Python Initialize ESCs: https://raspberrypi.stackexchange.com/questions/29551/how-to-initialize-an-esc-with-python-code
LittleBee Programming Manual: https://www.little-bellanca.com/manual_download/flza3000-tech.pdf
'''

from rcpy import servo
from time import sleep

class ESC:
    FREQ = 200
    WAKEUP_DURATION = 3
    WAKEUP_VALUE = -0.1

    def __init__(self, channel):
        self.channel = channel
        self.esc = servo.ESC(channel)
        self.awake = False

    def wakeup(self):
        for i in range(0, self.FREQ * self.WAKEUP_DURATION + 1):
            self.esc.pulse(self.WAKEUP_VALUE)
            sleep(1 / self.FREQ)
        self.awake = True

    def set_throttle(self, throttle):
        assert(self.awake, "ESC is not awake yet; wakeup() first.")

        self.esc.set(throttle)
        clk = self.esc.start(1 / self.FREQ)

    def pulse_throttle(self, throttle):
        assert(self.awake, "ESC is not awake yet; wakeup() first.")

        self.esc.pulse(throttle)

    def sweep(self, duration):
        assert(self.awake, "ESC is not awake yet; wakeup() first.")

        sweep_limit = 0.5
        dir = 1
        thr = 0
        for i in range(0, self.FREQ * duration + 1):
            thr += dir * sweep_limit / self.FREQ
            if thr > sweep_limit:
                thr = sweep_limit
                dir = -1
            elif thr < 0:
                thr = 0
                dir = 1
            self.esc.pulse(thr)
            sleep(1 / self.FREQ)
