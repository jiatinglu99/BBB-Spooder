from pyPS4Controller.controller import Controller

class MyController(Controller):
    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)

    def on_triangle_release(self):
           print("TRIANGLE released")

    def on_circle_release(self):
           print("CIRCLE released")

    def on_x_release(self):
           print("X released")

    def on_square_release(self):
           print("SQUARE released")

controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=True)
# controller.listen()