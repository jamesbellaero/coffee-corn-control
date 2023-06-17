from .controller import Controller
from time import sleep

class DirectController(Controller):
    def __init__(self):
        Controller.__init__(self)
    def run(self):
        self.startup_routine()
        while True:
            if self.turnoff:
                return
            # sample to see if pin is low or high. Pin high = low heat and vice versa. Don't worry about it.
            relay_value = self.relay.check_relay(0)
            # if high and pin is high, set to low
            if self.high and relay_value > .5:
                self.relay.deactivate_relay(0)
            # if low and pin is high, set to low 
            elif (not self.high) and relay_value < .5:
                self.relay.activate_relay(0)

            sleep(.05) # 20 hz
        



    
