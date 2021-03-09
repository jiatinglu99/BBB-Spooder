#from robot.driver.servo.lss import Servo
#from robot.driver.helpers.DegreeMath import *
try:
    from .lss import Servo
except Exception:
    from lss import Servo
try:
    from .helpers import *
except Exception:
    from helpers import *

import time

class Leg:
    def __init__(self, sel=0, ID1=0, P1=True, O1=0, ID2=0, P2=True, O2=0, ID3=0, P3=True, O3=0):
        self.sel = sel# config selection
        self.servos = []
        # base leg for Yaw
        self.servos = [
            Servo(ID1, polarity=P1, offset=O1),
            Servo(ID2, polarity=P2, offset=O2),
            Servo(ID3, polarity=P3, offset=O3)
        ]
        # storing ID numbers for all
        self.IDlist = [ID1, ID2, ID3]
        # Acquire position for each servo upon power up
        self.desired_coordinates = [17.0,15.0,10.0]
        self.current_coordinates = self.acquire_positions()
        
        self.safe_walking_range = (0.0,0.0,0.0,0.0) # (front_extreme, back_extreme, extention_out, normal_height)
        self.config_init()
        self.increment = 0
        self.lift = False # lift actually means "is stepping back"
        self.SWITCH_NOW = False

    def acquire_positions(self):
        return [0.0,0.0,0.0]

    def config_init(self):
        if self.sel == 4:
            self.servos[0].set_safe_parameters(-45, 0, 0)
        elif self.sel == 5:
            self.servos[0].set_safe_parameters(-45, 0, 0)
        elif self.sel == 6:
            self.servos[0].set_safe_parameters(45, 0, 0)
        elif self.sel == 7:
            self.servos[0].set_safe_parameters(45, 0, 0)
        else:
            self.servos[0].set_safe_parameters(0, 0, 0)
        self.servos[1].set_safe_parameters(0, 0, 0)
        self.servos[2].set_safe_parameters(0, 0, 0)

        if self.sel < 4:
            self.length_a = 5.0
            self.length_b = 10.0
            self.length_c = 10.0
        else:
            self.length_a = 5.0
            self.length_b = 10.85
            self.length_c = 10.0
        '''
        inner front leg
        ID  Front   Back    Out     Height
        0   5.5     -0.5    10      18
        1   same
        2   0.5     -5.5    10      18
        3   sames
        
        4   10      4       6       18
        5   same
        
        6   -4     -10      6       18
        7   same
        '''
        front_extreme_inner = 5.5
        walk_length = 6
        front_extreme_outer = 10
        common_out_inner = 10
        common_out_outer = 6
        common_height = 15
        if self.sel == 0 or self.sel == 1:
            self.safe_walking_range = (front_extreme_inner, front_extreme_inner-walk_length, common_out_inner, common_height)
        elif self.sel == 2 or self.sel == 3:
            self.safe_walking_range = (walk_length-front_extreme_inner, -front_extreme_inner, common_out_inner, common_height)
        elif self.sel == 4 or self.sel == 5:
            self.safe_walking_range = (front_extreme_outer, front_extreme_outer-walk_length, common_out_outer, common_height)
        elif self.sel == 6 or self.sel == 7:
            self.safe_walking_range = (walk_length-front_extreme_outer,-front_extreme_outer, common_out_outer, common_height)
        
    def stretch(self):
        for servo in self.servos:
            servo.get_in_safe_position()

    def calculate_angles(self):
        coord_a = self.desired_coordinates[0]
        coord_b = self.desired_coordinates[1]
        coord_c = self.desired_coordinates[2]
        CLT = sqrt(sqrd(coord_a)+sqrd(coord_b))
        S = sqrt(sqrd(CLT-self.length_a)+sqrd(coord_c))
        angle_a = acos(coord_b/CLT)
        X = (sqrd(S)-sqrd(self.length_b)-sqrd(self.length_c))/(-2*self.length_b*self.length_c)
        angle_c = 180 - acos(X)
        M = atan2((coord_c), (CLT-self.length_a))
        angle_b = asin((self.length_c*sin(180-angle_c)/S))-M
        
        if self.sel == 4 or self.sel == 5:
            angle_a -= 90.0
        elif self.sel == 6  or self.sel == 7:
            angle_a += 90.0
        self.servos[0].update_desired_position(angle_a)
        self.servos[1].update_desired_position(angle_b)
        self.servos[2].update_desired_position(-angle_c)
        
    def walk_proceed(self, thrt):
        self.increment = thrt
        temp = self.desired_coordinates
        if self.lift:
            self.desired_coordinates = [temp[0] + self.increment*5.0 ,temp[1],temp[2]]
            #if self.sel == 4: print(temp[0])
            if temp[0] > self.safe_walking_range[0]:
                self.lift = False
                self.SWITCH_NOW = True
        else:
            self.desired_coordinates = [temp[0] - self.increment, temp[1], temp[2]]
        
    def is_done(self):
        #if self.sel == 4:
        #    print(self.lift, self.SWITCH_NOW)
        temp = self.desired_coordinates
        if self.SWITCH_NOW:
            self.SWITCH_NOW = False
            return True
        if not self.lift and temp[0] < self.safe_walking_range[1]: # case of stepping normally and reaches the end
            self.go_to_front() # tell leg to go to front
            #return False
        return False
        
    def daniel_calculate_angles(self):
        x, y, z = self.desired_coordinates
        if self.lift:
            z = self.desired_coordinates[2]-3
        angle_a = atan2(x, y)
        
        y=sqrt(x**2 + y**2)
        length_d = sqrt(z**2 + (y-self.length_a)**2)
        angle_c = acos((self.length_b**2 + self.length_c**2 - length_d**2) / (2 * self.length_b * self.length_c))
        angle_b = asin(self.length_c / length_d * sin(angle_c)) - atan2(z,y)

        if self.sel == 4 or self.sel == 5:
            angle_a -= 90
        elif self.sel == 6  or self.sel == 7:
            angle_a += 90
        self.servos[0].update_desired_position(angle_a)
        self.servos[1].update_desired_position(angle_b)
        self.servos[2].update_desired_position(-(180 - angle_c))
        
    def update_desired_coordinates(self, a, b, c):
        self.desired_coordinates = (a,b,c)
        #print(self.desired_coordinates)

    def get_command_bytes(self):
        temp = b''
        for servo in self.servos:
            temp += servo.get_position_command_bytes()
        return temp
        
    def get_initialize_command_bytes(self):
        temp = b''
        for servo in self.servos:
            temp += servo.get_initialize_command_bytes()
        return temp
        
    def go_to_front(self): #NEEDS WORK
        #self.desired_coordinates[0] = self.safe_walking_range[0]
        self.lift = True #imma need to lift
        pass
    
    def go_to_percent(self, percent):
        temp = self.desired_coordinates
        length = self.safe_walking_range[0] - self.safe_walking_range[1]
        begin = self.safe_walking_range[1]
        self.desired_coordinates[0] = begin + percent*length