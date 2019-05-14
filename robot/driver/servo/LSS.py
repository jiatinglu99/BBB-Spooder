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
        #print("#{}QD\r".format(self.ID).encode())
        return "#{}QD\r".format(self.ID).encode()
    
    def updateCurrentPosition(self, degree): #degree in 1
        self.currentPosition = degree
    
    def updateDesiredPosition(self, degree): #degree in 1
        self.desiredPosition = degree
    
    def getCommandStr(self): 
        #print("#{}D{}\r".format(self.ID, int(self.desiredPosition*10)).encode())
        return "#{}D{}\r".format(self.ID, int(self.desiredPosition*10)).encode()
    
    def getCurrentAmp(self):
        return self.currentAmp
    
    def updateAmp(self, amp):
        self.currentAmp = amp
        return None
        
def test():
    sp = serial.Serial('/dev/ttyO1', baudrate = 115200, timeout = 1)
    servos = []
    for i in range(1, 13):
        servos.append(Servo(i))
    
    tempPosition = 0
    while True:
        for servo in servos:
            servo.updateDesiredPosition(tempPosition)
            sp.write(servo.getCommandStr())
        time.sleep(1)
        tempPosition += 1
        
    
    #while True:
        #sp.write(servo.getPositionQueryStr())
        #time.sleep(0.1)
        #print("h1")
        #reading = sp.readline().decode('utf-8')
        #print(reading)
        #time.sleep(1)
        
if __name__ == '__main__':
    test()