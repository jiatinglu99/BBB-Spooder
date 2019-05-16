from driver.servo.leg import Leg

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
        self.ser = serial.Serial('/dev/ttyO1', baudrate = 115200, timeout = 1)


    def run(self):
        self.push_position()

    def stretch_legs(self):
        #for leg in self.legs:
        #    leg.stretch()
        self.legs[0].stretch()
        self.legs[1].stretch()
        self.legs[2].stretch()
        self.legs[3].stretch()


    def get_write_commands(self):
        temp = b''
        #for leg in self.legs:
        #    temp += leg.get_command_bytes()
        for i in range(4):
            temp += self.legs[i].get_command_bytes()
        return temp

    def push_position(self): # push desired angles onto the physical servos through serial
        self.ser.write(self.get_write_commands())
        
    def test_leg(self, number):
        self.legs[number].update_desired_coordinates(10, 10, 10)
        self.legs[number].calculate_angles()
        print(self.legs[number].get_command_bytes())
        
def test():
    SC = ServoCentral()
    SC.stretch_legs()
    SC.run()
    time.sleep(0.5)
    SC.test_leg(0)
    #SC.run()
    
        
if __name__ == '__main__':
    test()
