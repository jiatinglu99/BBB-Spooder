from robot.driver.servo.lss import Servo


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
        
        self.config_init()

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
        
    def stretch(self):
        for servo in self.servos:
            servo.get_in_safe_position()
        
    def get_command_bytes(self):
        temp = b''
        for servo in self.servos:
            temp += servo.get_position_command_bytes()
        return temp
