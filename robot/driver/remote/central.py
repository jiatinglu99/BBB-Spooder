from pyPS4Controller.controller import Controller

class RemoteCentral:
    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)

remote_central = RemoteCentral(interface="/dev/input/js0", connecting_using_ds4drv=True)
remote_central.listen()