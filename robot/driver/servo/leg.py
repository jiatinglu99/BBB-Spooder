from robot.driver.servo.LSS import Servo


class Leg:
    def __init__(self, XID, YID, ZID):
        servos = []
        # base leg for Yaw
        servos.append(Servo(XID, polarity = True, offset = 0))
        # secondary leg for Pitch1
        servos.append(Servo(YID, polarity = True, offset = 0))
        # tertiary leg for Pitch2
        servos.append(Servo(ZID, polarity = True, offset = 0))
        
    def getCommandStr(self):
        commandCollection = self.servoX
