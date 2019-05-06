"""
Drivers for motors controlled by SSC

"""

class Servo:
    def __init__(self, ID, polarity = True, offset = 0):
        self.ID = ID
        self.currentPosition = 0
        self.desiredPosition = 0
        self.polarity = polarity
        self.offset = offset

    def command_position_str(self, degree):
        self.desiredPosition = int(degree*10)
        return "#{}PD{}\r".format(self.ID, self.desiredPosition)
    