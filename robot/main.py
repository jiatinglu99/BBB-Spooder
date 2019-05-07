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

    def controller_connected(self):
        print('Controller connected')

    # Like GOD
    def controller_commanded(self, type, body):
        if type == RemoteControl.CMD_SET_MODE:
            print('Set mode:', body)
        elif type == RemoteControl.CMD_MOTION:
            pitch, yaw, roll, throttle = body.split(',')

    def controller_disconnected(self):
        print('Controller disconnected')
        # Land/stop?


if __name__ == "__main__":
    robot = Robot()
