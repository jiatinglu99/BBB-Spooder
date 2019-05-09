from robot.driver.servo.LSS import Servo


class Leg:
    def __init__(self, XID, YID, ZID):
        self.servos = []
        # base leg for Yaw
        self.servos.append(Servo(XID, polarity = True, offset = 0))
        # secondary leg for Pitch1
        self.servos.append(Servo(YID, polarity = True, offset = 0))
        # tertiary leg for Pitch2
        self.servos.append(Servo(ZID, polarity = True, offset = 0))
        
        IDlist = [XID, YID, ZID]
        
    def getCommandStr(self):
        return "{}{}{}{}".format(self.servos[0].getCommandStr)
