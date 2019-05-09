#from driver.sensor.central import SensorCentral
#from driver.esc.central import ESCCentral
#from driver.servo.central import ServoCentral
from driver.remote.remote_control import RemoteControl, Command
import time

class Robot:
    def __init__(self):
        #self.sensor_central = SensorCentral()
        #self.esc_central = ESCCentral()
        #self.servo_central = ServoCentral()
        self.remote_control = RemoteControl(handler=self)

    def start_updating(self):
        self.last_command = None
        while True:
            if self.last_command == None: continue

            type = self.last_command.type
            body = self.last_command.body
            # Time elapsed since the last command came in
            time_elapsed = time.time() - self.last_command.timestamp
            if time_elapsed > 2:
                print('We might have disconnected.')
                print('Take appropriate stabilizing/landing action.')
                continue

            if type == RemoteControl.CMD_UPDATE:
                # commands always come in as YYYYTTTTRRRRPPPP
                commands = [line[i:i+4] for i in range(0, len(body), 4)]
                handle_quad_pid(commands)
            elif type == RemoteControl.CMD_MODE:
                print('Set mode', body)

            FREQ = 1 / 200
            time.sleep(FREQ)

    def handle_quad_pid(self, components):
        # Brought in normalized
        yaw, throttle, roll, pitch = components


    def controller_commanded(self, command):
        self.last_command = command

if __name__ == "__main__":
    robot = Robot()
    robot.start_updating()
