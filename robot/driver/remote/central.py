from pyPS4Controller.controller import Controller

class RemoteController(Controller):
    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)
        self.l3_up = 0
        self.l3_down = 0
        self.l3_left = 0
        self.l3_right = 0
        self.r3_up = 0
        self.r3_down = 0
        self.r3_left = 0
        self.r3_right = 0

    # Right pad buttons
    def on_x_press(self):
        pass
    def on_x_release(self):
        print("X released")
    def on_triangle_press(self):
        pass
    def on_triangle_release(self):
        print("TRIANGLE released")
    def on_circle_press(self):
        pass
    def on_circle_release(self):
        print("CIRCLE released")
    def on_square_press(self):
        pass
    def on_square_release(self):
        print("SQUARE released")

    # Back left buttons
    def on_L1_press(self):
        pass
    def on_L1_release(self):
        print("L1 released")
    def on_L2_press(self, value):
        pass
    def on_L2_release(self):
        print("L2 released")

    # Back right buttons
    def on_R1_press(self):
        pass
    def on_R1_release(self):
        print("R1 released")
    def on_R2_press(self, value):
        pass
    def on_R2_release(self):
        print("R2 released")

    # Left pad buttons
    def on_up_arrow_press(self):
        print("UP pressed")
    def on_down_arrow_press(self):
        print("DOWN pressed")
    def on_up_down_arrow_release(self):
        print("UP and DOWN released")
    def on_left_arrow_press(self):
        print("LEFT pressed")
    def on_right_arrow_press(self):
        print("RIGHT pressed")
    def on_left_right_arrow_release(self):
        print("LEFT and RIGHT released")

    # Left joystick
    def on_L3_up(self, value):
        print("LEFT JOYSTICK: UP {}".format(value))
        self.l3_up = value
    def on_L3_down(self, value):
        print("LEFT JOYSTICK: DOWN {}".format(value))
        self.l3_down = value
    def on_L3_left(self, value):
        print("LEFT JOYSTICK: LEFT {}".format(value))
        self.l3_left = value
    def on_L3_right(self, value):
        print("LEFT JOYSTICK: RIGHT {}".format(value))
        self.l3_right = value
    def on_L3_at_rest(self):
        print("LEFT JOYSTICK: AT REST")
        self.reset_l3()

    # Right joystick
    def on_R3_up(self, value):
        print("RIGHT JOYSTICK: UP {}".format(value))
        self.r3_up = value
    def on_R3_down(self, value):
        print("RIGHT JOYSTICK: DOWN {}".format(value))
        self.r3_down = value
    def on_R3_left(self, value):
        print("RIGHT JOYSTICK: LEFT {}".format(value))
        self.r3_left = value
    def on_R3_right(self, value):
        print("RIGHT JOYSTICK: RIGHT {}".format(value))
        self.r3_right = value
    def on_R3_at_rest(self):
        print("RIGHT JOYSTICK: AT REST")
        self.reset_r3()

    # Options button
    def on_options_press(self):
        pass
    def on_options_release(self):
        print("OPTIONS released")

    # Helpers
    def reset_l3(self):
        self.l3_up = 0
        self.l3_down = 0
        self.l3_left = 0
        self.l3_right = 0
    def reset_r3(self):
        self.r3_up = 0
        self.r3_down = 0
        self.r3_left = 0
        self.r3_right = 0
