from robot.driver.servo.LSS import Servo


class Leg:
    def __init__(self, xid, yid, zid):
        self.servos = []
        # Parameters below for polarity and offset are redundant
        # base leg for Yaw
        self.servos.append(Servo(xid, polarity=True, offset=0))
        # secondary leg for Pitch1
        self.servos.append(Servo(yid, polarity=True, offset=0))
        # tertiary leg for Pitch2
        self.servos.append(Servo(zid, polarity=True, offset=0))

        # storing ID numbers for all
        IDlist = [xid, yid, zid]

    def initialize(self):
        # Acquire position for each servo upon power up
        for servo in self.servos:
            if 
        

    def get_command_str(self):
        return "{}{}{}{}".format(   self.servos[0].get_command_str,
                                    self.servos[0].get_command_str,
                                    self.servos[0].get_command_str
                                    self.servos[0].get_command_str)
