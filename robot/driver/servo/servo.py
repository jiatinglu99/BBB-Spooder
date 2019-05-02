"""
Drivers for motors controlled by SSC
Motor Type 0: Original Virtual Motor 
Motor Type 1: SG90 Tower Pro: http://www.ee.ic.ac.uk/pcheung/teaching/DE1_EE/stores/sg90_datasheet.pdf
Motor Type 2: KRS-2552 or KRS-2572 in PWM mode: http://kondo-robot.com/w/wp-content/uploads/KRS-series_manual_Download-En.pdf
Motor Type 3: PLACEHOLDER
"""

class Motor:
    MOTOR_SG90 = 0
    MOTOR_KRS = 1
    MOTOR_PLACEHOLDER = 2

    def __init__(self, type):
        self.type = type

        if self.type == Motor.MOTOR_SG90:
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
        elif self.type == Motor.MOTOR_KRS2552:
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
        elif self.type == Motor.MOTOR_KRS2572:
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
        elif self.type == Motor.MOTOR_PLACEHOLDER:
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
            print('Invalid motor type!!!')