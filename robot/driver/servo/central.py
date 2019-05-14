from driver.servo.lss import LSS

class ServoCentral:
    def __init__(self):
        self.status = 0 
        '''
        Number      Status
        0           Not initialized, or initializing
        1           Working, and providing torque
        2           Limp
        '''
