'''
Incorporated from https://github.com/mcdeoliveira/rcpy/blob/master/examples/rcpy_bare_minimum_thread.py
'''

import time
import rcpy
import rcpy.mpu9250 as mpu9250

class GyroscopeSensor:
    def __init__(self):
        self.refresh_rate = 200
        self.refresh_time = 0 #1.0/self.refresh_rate
        self.imu = mpu9250.IMU(enable_dmp = False)
        
        # start the sensor
        rcpy.set_state(rcpy.RUNNING)
        self.imu.initialize(enable_magnetometer = False)
        self.data ={}

    def thread_update(self):
        while rcpy.get_state() == rcpy.RUNNING:
            self.data = imu.read()
            time.sleep(self.refresh_time)

    def get_data(self):
        return self.data