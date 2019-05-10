from driver.sensor.gps import GPSSensor
from driver.sensor.current_monitor import CurrentSensor
from driver.sensor.gyroscope import GyroscopeSensor
from driver.sensor.proximity import ProximitySensor

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
