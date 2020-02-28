from gps import GPSSensor
from current_monitor import CurrentSensor
from gyroscope import GyroscopeSensor
from proximity import ProximitySensor

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

    def get_gyroscope(self):
        return self.gyroscope.get_data()
