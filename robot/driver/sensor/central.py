from .gps import GPSSensor
from .current_monitor import CurrentSensor
from .gyroscope import GyroscopeSensor
from .proximity import ProximitySensor

import time
import threading

class SensorCentral:
    def __init__(self):
        self.gps = GPSSensor()
        self.current = CurrentSensor()
        self.gyroscope = GyroscopeSensor()
        self.proximity = ProximitySensor()

        # sensor threads
        self.threads = []
        #self.threads.append(threading.Thread(target = self.gps.thread_update()))
        #self.threads.append(threading.Thread(target = self.current.thread_update()))
        self.threads.append(threading.Thread(target = self.gyroscope.thread_update()))
        #self.threads.append(threading.Thread(target = self.proximity.thread_update()))

        # start threading
        for t in self.threads:
            t.start()

    def getGPS(self):
        pass

    def getCurrent(self):
        pass

    def getGyroscope(self):
        return self.gyroscope.get_data()
