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
        self.current_amp = 0.0
        self.polarity = polarity
        self.offset = offset
        
        self.motion_controll = 1 # EM 1 or 0
        self.angular_stiffness = 0 # AS -10 to 10, -4 to 4 on the margin
        self.angular_holding_stiffness = 0 # AH -10 to 10
        self.angular_acceleration = 1 # AA 1-100
        self.angular_deceleration = 1 # AD 1-100
        self.baudrate = 115200 # QB cannot be changed on serial, must be done 
        self.gyre_direction = 1 # CG
        if not self.polarity:
            self.gyre_direciton = -1

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
        #return "#{}CB115200\r".format(self.ID).encode()
        #if self.ID == 17: return b''
        return "#{}D{}AS-2EM0\r".format(self.ID, int(self.desired_position*10)).encode() #AS-4EM0
            
    def get_initialize_command_bytes(self):
        temp = b''
        #temp += "#{}AS-4EM0\r".format(self.ID, self.angular_stiffness).encode()
        #temp += "#{}CAH{}\r".format(self.ID, self.angular_holding_stiffness).encode()
        #temp += "#{}CAA{}\r".format(self.ID, self.baudrate).encode() #CAA accelration
        #temp += "#{}CAD{}\r".format(self.ID, self.angular_deceleration).encode()
        #temp += "#{}CG{}\r".format(self.ID, self.gyre_direction).encode() #inittialize
        #temp += "#{}CEM{}\r".format(self.ID, self.motion_controll).encode()
        return temp

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
