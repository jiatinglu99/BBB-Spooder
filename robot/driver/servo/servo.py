"""
Drivers for motors controlled by SSC
Servo Type 0: Original Virtual Servo 
Servo Type 1: SG90 Tower Pro: http://www.ee.ic.ac.uk/pcheung/teaching/DE1_EE/stores/sg90_datasheet.pdf

"""

class Servo:
    SERVO_SG90 = 0
    SERVO_KRS = 1

    def __init__(self, type):
        self.type = type

        if self.type == Servo.SERVO_SG90:
            #degree range
            self.degreeMin = 0
            self.degreeMax = 180

            #duty cycle range
            self.pulseMin = 1000 #μs
            self.pulseMax = 2000 #μs
            self.pwmPeriod = 20 #ms

            #compatible PWM frequency range 
            self.maxFreq = 20
            self.minFreq = 20
            
            #specs
            self.voltageMin = 4.8 #V
            self.voltageMax = 6.0 #V
            self.torque = 2.5 #kg-cm
            self.weight = 14.7 #g
        else:
            print('Invalid servo type!!!')