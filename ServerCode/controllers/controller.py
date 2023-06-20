from .relay import Relay
from threading import Thread
from time import sleep


class Controller(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.high = False
        self.turnoff = False
        if('relay' not in globals()):
            globals()['relay'] = Relay()
        self.relay = globals()['relay']
        self.relay_dict = self.relay.get_relay_dict()
        pass
    def mode_low(self):
        self.high = False
        
    def mode_high(self):
        self.high = True
        
    def shutdown(self):
        self.turnoff = True
        
    def startup_routine(self):
        # deactivate all relays for good measure
        for d in self.relay_dict:
            self.relay.deactivate_relay(d)

        # activate default relay
        self.relay.activate_relay(0)

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
            elif self.low and relay_value < .5:
                self.relay.activate_relay(0)

            sleep(.05) # 20 hz
        





