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

    def handle_remote_command(self, command):
        print('Got command:', command)


if __name__ == "__main__":
    robot = Robot()
