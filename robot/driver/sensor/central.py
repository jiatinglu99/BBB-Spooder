from gps import GPSSensor
from current_monitor import CurrentSensor
from gyroscope import GyroscopeSensor
from proximity import ProximitySensor

import time

class SensorCentral:
    def __init__(self):
        self.gps = GPSSensor()
        self.current = CurrentSensor()
        self.gyroscope = GyroscopeSensor()
        self.proximity = ProximitySensor()

    def get_gps(self):
        pass

    def get_current(self):
        pass
        
    # gyroscope_Data format sample:{'gryo':(x, y, z), 'accel':(a, b, c)}
    # example: {'gyro': (-0.06103515625, -0.1220703125, -0.42724609375), 'tb': (0.0, 0.0, 0.0), 'accel': (0.6429404860150083, 0.12662076935428568, 9.681104622146606), 'quat': (0.0, 0.0, 0.0, 0.0)}
    def get_gyroscope(self):
        return self.gyroscope.get_data()


# Uncomment the following for testing
'''
def main():
    SC = SensorCentral()
    while True:
        print(SC.get_gyroscope())
        time.sleep(0.1)

if __name__ == '__main__':
    main()

'''