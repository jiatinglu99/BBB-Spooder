"""
Drivers for motors controlled by SSC
Servo Type 0: Original Virtual Servo 
Servo Type 1: SG90 Tower Pro: http://www.ee.ic.ac.uk/pcheung/teaching/DE1_EE/stores/sg90_datasheet.pdf
Servo Type 2: KRS-2552 or KRS-2572 in PWM mode: http://kondo-robot.com/w/wp-content/uploads/KRS-series_manual_Download-En.pdf
Servo Type 3: PLACEHOLDER
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
        elif self.type == Servo.SERVO_KRS2552:
            self.degreeMin = 
            self.degreeMax = 
            self.pulseMin = 700
            self.pulseMax = 2300
            self.pwmPeriod = 
            self.maxFreq = 
            self.minFreq = 
            self.voltageMin = 
            self.voltageMax = 
            self.torque = 
            self.weight = 
        elif self.type == Servo.SERVO_KRS2572:
            self.degreeMin = 
            self.degreeMax = 
            self.pulseMin = 
            self.pulseMax = 
            self.pwmPeriod = 
            self.maxFreq = 
            self.minFreq = 
            self.voltageMin = 
            self.voltageMax = 
            self.torque = 
            self.weight = 
        else:
            print('Invalid servo type!!!')