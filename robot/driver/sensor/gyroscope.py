'''
Incorporated from https://github.com/mcdeoliveira/rcpy/blob/master/examples/rcpy_bare_minimum_thread.py
'''

import time
import rcpy
import rcpy.mpu9250 as mpu9250
import threading

class GyroscopeSensor:
    def __init__(self):
        # set state to rcpy.RUNNING
        rcpy.set_state(rcpy.RUNNING)
        # no magnetometer
        mpu9250.initialize(enable_magnetometer = False)

        # start the sensor
        rcpy.set_state(rcpy.RUNNING)

    def get_data(self):
        return mpu9250.read()
