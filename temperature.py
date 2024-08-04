#import board
# import analogio
import sys
# ~ import analogio #Ne fonctionne pas pour sur le raspberry 3B, impossible d'importer la librairie
sys.path.insert(1,"/home/pi/SCAMPI/Management") #Utils is in another folder have to give the path
from Utils import Logger

class Temperature:    
    def __init__(self):
        self.log = Logger()
        #self.tmp36 = analogio.AnalogIn(board.A0)
    def get_temperature(self):
        self.temperature = 25
        #self.voltage = self.tmp36.value * 3.3 / 65536
        #self.temperature = (self.voltage - 0.5) * 100
        self.log.log_values("tmp36_temperature",self.temperature)
    
