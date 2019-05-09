from driver.sensor.central import SensorCentral
from driver.esc.central import ESCCentral
from driver.servo.central import ServoCentral
from driver.remote.remote_control import RemoteControl, Command
from pid import PID
import time

class Robot:
    ### Initializes the robot and all its peripheral centrals
    def __init__(self):
        self.FREQ = 200 # updates per second
        self.sensor_central = SensorCentral()
        self.esc_central = ESCCentral()
        self.servo_central = ServoCentral()
        self.remote_control = RemoteControl(handler=self)

    ### Might have a problem when we are walking and don't want to use PID. Anyway, sets up PID and starts updating
    def start_updating(self):
        # create last_command variable for future loops
        self.last_command = None
        # setup pitch_pid
        self.pitch_pid = PID(3.55, 0.005, 2.05)
        self.pitch_pid.SetPoint=0.0
        self.pitch_pid.setSampleTime(1 / self.FREQ / 2)
        # setup roll_pid
        self.roll_pid = PID(3.55, 0.005, 2.05)
        self.roll_pid.SetPoint=0.0
        self.roll_pid.setSampleTime(1 / self.FREQ / 2)
        # update
        while True:
            if self.last_command == None: continue                              # still waiting for the initial connection

            # check if we have effectively disconnected (elapsed time > 2s)
            if time.time() - self.last_command.timestamp > 2:
                print('We might have disconnected.')
                print('Take appropriate stabilizing/landing action.')
                continue

            # take appropriate action given command type
            type, body = self.last_command.type, self.last_command.body
            if type == RemoteControl.CMD_UPDATE:
                commands = [body[i:i+4] for i in range(0, len(body), 4)]        # commands always come in as YYYYTTTTRRRRPPPP
                self.handle_quad_pid(self.normalize_components(commands))       # handle quad movement after normalizing components
            elif type == RemoteControl.CMD_MODE:
                print('Set mode', body)

            time.sleep(1 / self.FREQ)

    ### Normalizes the command components, where forward direction is with the antennae on the __backside__.
    def normalize_components(self, commands):
        yaw, throttle, roll, pitch = map(int, commands)                         # convert to int, unpack commands array
        yaw = (yaw - 1000) / (100 / 3)                                          # -30 deg/s to +30 deg/s
        throttle = 1 - throttle / 2000                                          # 0 to 1
        roll = (roll - 1000) / (50 / 3)                                         # -60 deg below horizontal to +60 deg below horizontal
        pitch = (1000 - pitch) / (50 / 3)                                       # -60 deg below horizontal to +60 deg below horizontal
        return map(lambda x: round(x, 3), [yaw, throttle, roll, pitch])         # round to 3 decimal points

    ### Handles the commands for PID
    def handle_quad_pid(self, normalized_components):
        # target values
        yaw, throttle, roll, pitch = normalized_components
        print(yaw, throttle, roll, pitch)
        # throttles of each propellor, 0-3 (we 0 index; come on now)
        throttles = [throttle, throttle, throttle, throttle]

        # yaw not yet; idk how to do it yet
        pass

        current_gyroscope = self.sensor_central.get_gyroscope()
        # roll -- might have to flip += and -=
        self.roll_pid.SetPoint = roll
        self.roll_pid.update(current_gyroscope[0])
        roll_pid_output = self.roll_pid.output
        throttles[0] += roll_pid_output
        throttles[2] += roll_pid_output
        throttles[1] -= roll_pid_output
        throttles[3] -= roll_pid_output
        # pitch -- might have to flip += and -=
        self.pitch_pid.SetPoint = pitch
        self.pitch_pid.update(current_gyroscope[1])
        pitch_pid_output = self.pitch_pid.output
        throttles[0] += pitch_pid_output
        throttles[3] += pitch_pid_output
        throttles[2] -= pitch_pid_output
        throttles[1] -= pitch_pid_output

        # push throttles to esc_central
        throttles = map(lambda n: clamp(n, 0, 1), throttles)                    # ensure throttles are between 0 and 1

    # delegate method for RemoteControl
    def controller_commanded(self, command):
        self.last_command = command

    # clamp a value in a range
    def clamp(self, n, bottom, top):
        return max(bottom, min(n, top))

if __name__ == "__main__":
    robot = Robot()
    robot.start_updating()
