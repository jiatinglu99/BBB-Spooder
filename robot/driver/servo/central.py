from leg import Leg

import serial
import time

class ServoCentral:
    def __init__(self):
        self.status = 0
        '''
        Number      Status
        0           Not initialized, or initializing
        1           Working, and providing torque
        2           Limp
        '''
        self.legs = [
            Leg(sel=0,  ID1=1, P1=True, O1=1772,    ID2=2, P2=False, O2=904,    ID3=3, P3=False, O3=1739),   # 0: inner leg top left
            Leg(sel=1,  ID1=4, P1=False, O1=427,    ID2=5, P2=True, O2=-14,     ID3=6, P3=True, O3=-435),    # 1: inner leg top right
            Leg(sel=2,  ID1=7, P1=True, O1=-468,    ID2=8, P2=True, O2=-25,     ID3=9, P3=True, O3=932),     # 2: inner leg bottom left
            Leg(sel=3,  ID1=10, P1=False, O1=14,    ID2=11, P2=False, O2=38,    ID3=12, P3=False, O3=-923),  # 3: inner leg bottom right
            Leg(sel=4,  ID1=13, P1=True, O1=-1353,  ID2=14, P2=False, O2=472,   ID3=15, P3=False, O3=-12),   # 4: outer leg top left
            Leg(sel=5,  ID1=16, P1=False, O1=-446,  ID2=17, P2=True, O2=-18,    ID3=18, P3=True, O3=-913),   # 5: outer leg top right
            Leg(sel=6,  ID1=19, P1=True, O1=-7,     ID2=20, P2=True, O2=5,      ID3=21, P3=True, O3=-427),   # 6: outer leg bottom left
            Leg(sel=7,  ID1=22, P1=False, O1=-916,  ID2=23, P2=False, O2=-5,    ID3=24, P3=False, O3=-906)   # 7: outer leg bottom right
        ]
        self.ser = serial.Serial('/dev/ttyO1', baudrate = 115200, timeout = 1) # baudrate could be 5000000
        self.reset_all_servos()
        self.push_initialize_commands()
        time.sleep(0.5)
        
    def reset_all_servos(self):
        #self.ser.write("#254QB500000\r".encode())
        self.ser.write("#254RESET\r".encode())
        
    def push_initialize_commands(self):
        self.ser.write(self.get_initialize_commands())

    def run(self):
        for leg in self.legs:
            leg.daniel_calculate_angles()
        self.push_position()
        self.ser.flush()

    def stretch_legs(self):
        for leg in self.legs:
            leg.stretch()

    def get_write_commands(self):
        temp = b''
        for leg in self.legs:
            temp += leg.get_command_bytes()
            
        #return self.legs[3].get_command_bytes()
        return temp
        
    def get_initialize_commands(self):
        temp = b''
        for leg in self.legs:
            temp += leg.get_initialize_command_bytes()
        return temp
        
    def push_position(self): # push desired angles onto the physical servos through serial
        self.ser.write(self.get_write_commands())
    
        
    def test_leg(self, numb):
        reverse = True
        m = 2
        d = 0
        out = 13
        #for i in range(5):
        t=time.time()
        while True:
            for number in range(0,2):
                self.legs[number].update_desired_coordinates(2, out, m)
            for number in range(2,4):
                self.legs[number].update_desired_coordinates(-2, out, m)#)m)
            self.legs[4].update_desired_coordinates(10, out, m)#)m)
            self.legs[5].update_desired_coordinates(10, out, m)#)m)
            self.legs[6].update_desired_coordinates(-10, out, m)#)m)
            self.legs[7].update_desired_coordinates(-10, out, m)#)m)
            #for number in range(0,8):
            #    self.legs[number].daniel_calculate_angles()
            
            #self.legs[3].calculate_angles()
            self.run()
            #if reverse: m
            #d+=0.05
            #if d>10:
            #    d = -4
            
            m += 0.07 * (-1) ** (reverse + 1)
            
            # if reverse:
            #     m += 0.05
            # else:
            #     m -= 0.05
            
            if reverse and m>14:
                reverse = not reverse
            elif not reverse and m<10:
                reverse = not reverse
            
            # Time monitoring section
            #time.sleep(0.001)
            #print(time.time()-t)
            #t=time.time()
            #self.reset_all_servos()
    def leg_test_range(self, leg_ID, front, back, out, height):
        self.legs[4].update_desired_coordinates(10, out, height)#)m)
        self.legs[5].update_desired_coordinates(10, out, height)#)m)
        self.legs[6].update_desired_coordinates(-10, out, height)#)m)
        self.legs[7].update_desired_coordinates(-10, out, height)#)m)
        reverse = True
        x = back
        inc = 0.2
        while True:
           # self.legs[4].update_desired_coordinates(x, out, height)
            #self.legs[5].update_desired_coordinates(x, out, height)
            for leg in self.legs:
                 if leg.sel == leg_ID:
                     leg.update_desired_coordinates(x, out, height)
            #else:
            #    leg.stretch()
            self.run()
            if reverse:
                x += inc
                if x > front:
                    reverse = not reverse
            elif not reverse:
                x -= inc
                if x<back:
                    reverse = not reverse
        
def test():
    SC = ServoCentral()
    #SC.stretch_legs()
    #SC.run()
    time.sleep(0.1)
    #SC.test_leg(0)
    #SC.leg_test_range(4, 10, 4, 6, 18)
    SC.leg_test_range(0, 5.5, -0.5, 10, 18)
    '''
    inner front leg
    ID  Front   Back    Out     Height
    0   5.5     -0.5    10      18
    1   same
    2   0.5     -5.5    10      18
    3   sames
    
    4   10      4       6       18
    5 same
    
    6   -4     -10      6       18
    7   same
    '''
        
if __name__ == '__main__':
    test()
