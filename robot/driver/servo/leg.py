from robot.driver.servo.lss import Servo
from robot.driver.helpers.DegreeMath import * 

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
        self.desired_coordinates = (10,10,10)
        self.current_coordinates = self.acquire_positions()

        self.config_init()

    def acquire_positions(self):
        return (0,0,0)

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
        else
            self.length_a = 5.0
            self.length_b = 10.85
            self.length_c = 10.0

    def stretch(self):
        for servo in self.servos:
            servo.get_in_safe_position()

    def calculate_angles(self):
        coord_a = self.current_coordinates[0]
        coord_b = self.current_coordinates[1]
        coord_c = self.current_coordinates[2]
        CLT = sqrt(sqrd(coord_a)+sqrd(coord_b))
        S = sqrt(sqrd(CLT-self.length_a)+sqrd(coord_c))
        angle_a = acos(coord_b/CLT)
        X = (sqrd(S)-sqrd(self.length_b)-sqrd(self.length_c))/(-2*self.length_b*self.length_c)
        angle_c = 180 - acos()
        
    def update_desired_coordinates(self, a, b, c):
        self.desired_coordinates = (a,b,c)

    def get_command_bytes(self):
        temp = b''
        for servo in self.servos:
            temp += servo.get_position_command_bytes()
        return temp