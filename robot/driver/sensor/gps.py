# Source: https://learn.adafruit.com/adafruit-ultimate-gps/circuitpython-parsing
# GPS module behavior: https://cdn-shop.adafruit.com/datasheets/PMTK_A11.pdf
# Will wait for a fix and print a message every second with the current location and other details.
import time
import adafruit_gps
import serial

class GPSSensor:
    def __init__(self):
        self.uart = serial.Serial("/dev/ttyO2", baudrate=9600, timeout=3000)
        self.gps = adafruit_gps.GPS(self.uart, debug=False)
        # Turn on the basic GGA and RMC info (what you typically want)
        self.gps.send_command(b'PMTK314,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0')
        # Set update rate to once a second (1000).
        self.gps.send_command(b'PMTK220,1000')

    # lat, lng, alt (might be None)
    def get_position():
        if gps.has_fix:
            return (None, None, None)
        else:
            self.gps.update()
            return (self.gps.latitude, self.gps.longitude, self.gps.altitude_m)
