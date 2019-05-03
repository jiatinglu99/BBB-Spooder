from driver.sensor.central import SensorCentral
from driver.esc.central import ESCCentral
from driver.servo.central import ServoCentral
from driver.remote_control import RemoteControl

class Robot:
    def __init__(self):
        self.sensor_central = SensorCentral()
        self.esc_central = ESCCentral()
        self.servo_central = ServoCentral()
        self.remote_control = RemoteControl(handler=self)

    def controller_connected(self):
        pass

    # Like GOD
    def controller_commanded(self, type, body):
        pass

    def controller_disconnected(self):
        pass


if __name__ == "__main__":
    robot = Robot()
