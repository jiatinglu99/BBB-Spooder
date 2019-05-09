"""
Drivers for LSS Servo

"""
import serial
import time

class Servo:
    def __init__(self, ID, polarity = True, offset = 0):
        self.ID = ID
        self.currentPosition = 0.0
        self.desiredPosition = 0.0
        self.currentAmp = 0
        self.polarity = polarity
        self.offset = offset
        
    def getPositionQueryStr(self):
        return "#{}QD/r".format(self.ID).encode()
    
    def updateCurrentPosition(self, degree): #degree in 1
        self.currentPosition = degree
    
    def updateDesiredPosition(self, degree): #degree in 1
        self.desiredPosition = degree
    
    def getCommandStr(self): 
        return "#{}D{}\r".format(self.ID, int(self.desiredPosition*10)).encode()
    
    def getCurrentAmp(self):
        return self.currentAmp
    
    def updateAmp(self, amp):
        self.currentAmp = amp
        return None
        
def test():
    sp = serial.Serial('/dev/ttyO1', 115200)
    servo = Servo(1)
    while True:
        sp.write(servo.getPositionQueryStr())
        time.sleep(0.1)
        reading = sp.readline().decode('utf-8')
        print(reading)
        time.sleep(1)
        