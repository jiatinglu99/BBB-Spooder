from esc import ESC

class ESCCentral:
    def __init__(self):
        self.all_escs = ESC(0)
        self.all_escs.wakeup()

        self.esc1 = ESC(1)
        self.esc2 = ESC(2)
        self.esc3 = ESC(3)
        self.esc4 = ESC(4)
