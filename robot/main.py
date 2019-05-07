from driver.sensor.central import SensorCentral
from driver.esc.central import ESCCentral
from driver.servo.central import ServoCentral
from driver.remote.remote_control import RemoteControl

class Robot:
    def __init__(self):
        self.sensor_central = SensorCentral()
        self.esc_central = ESCCentral()
        self.servo_central = ServoCentral()
        self.remote_control = RemoteControl(handler=self)

    def controller_commanded(self, type, body):
        if type == RemoteControl.CMD_HELLO:
            print('Connected!')
        elif type == RemoteControl.CMD_UPDATE:
            print(body)
        elif type == RemoteControl.CMD_MODE:
            print('Set mode', body)
        elif type == RemoteControl.CMD_GOODBYE:
            print('Disconnected!')

if __name__ == "__main__":
    robot = Robot()
