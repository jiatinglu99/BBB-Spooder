
class CurrentSensor:
    def __init__(self, **kwargs):
        self.pin = kwargs["pin"]
    
    def getCurrent(self):
        temp = 0 #***************read(pin) + calculation
        return temp
