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
