"""
Drivers for LSS Servo

"""
import serial
import time

class Servo:
    def __init__(self, ID, polarity = True, offset = 0):
        self.ID = ID
        self.current_position = 0.0
        self.desired_position = 0.0
        self.current_amp = 0
        self.polarity = polarity
        self.offset = offset

    def set_safe_parameters(self, init, forward, backward):
        self.safe_init = init
        self.safe_forward = forward
        self.safe_backward = backward
    
    def update_current_position(self, degree): #degree in 1
        self.current_position = degree
    
    def update_desired_position(self, degree): #degree in 1
        self.desired_position = degree

    def get_position_query_bytes(self):
        #print("#{}QD\r".format(self.ID).encode())
        return "#{}QD\r".format(self.ID).encode()
    
    def get_position_command_bytes(self): 
        #print("#{}D{}\r".format(self.ID, int(self.desiredPosition*10)).encode())
        if self.polarity:
            return "#{}D{}\r".format(self.ID, int(self.desired_position*10)).encode()
        else:
            return "#{}D{}\r".format(self.ID, -int(self.desired_position*10)).encode()
    
    def get_current_amp(self):
        return self.current_amp
    
    def update_amp(self, amp):
        self.current_amp = amp
        return None

    def get_in_safe_position(self):
        self.update_desired_position(self.safe_init)
        
def test():
    sp = serial.Serial('/dev/ttyO1', baudrate = 115200, timeout = 1)
    servos = []
    for i in range(1, 13):
        servos.append(Servo(i))
    
    temp_position = 0
    while True:
        for servo in servos:
            servo.update_desired_position(temp_position)
            sp.write(servo.get_command_str())
        time.sleep(1)
        temp_position += 1
        
    
    #while True:
        #sp.write(servo.getPositionQueryStr())
        #time.sleep(0.1)
        #print("h1")
        #reading = sp.readline().decode('utf-8')
        #print(reading)
        #time.sleep(1)
        
if __name__ == '__main__':
    #test()
    pass