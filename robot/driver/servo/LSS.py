"""
Drivers for motors controlled by SSC

"""

class Servo:
    def __init__(self, ID, polarity = True, offset = 0):
        self.ID = ID
        self.currentPosition = 0
        self.desiredPosition = 0
        self.currentAmp = 0
        self.polarity = polarity
        self.offset = offset

    def getCommandPositionStr(self, degree): 
        self.desiredPosition = int(degree*10)
        return "#{}D{}\r".format(self.ID, self.desiredPosition)

    def getCurrentAmp(self):
        return self.currentAmp
    
    def updateAmp(self, amp):
        self.currentAmp = amp
        return None