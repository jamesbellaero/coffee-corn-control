from .controller import Controller
import time 

class OpenLoopController(Controller):
    def __init__(self):
        Controller.__init__(self)

    def startup_routine(self):
        # default is 2700 ohm
        active_relay = 0

        # deactivate all relays for good measure
        for d in self.relay_dict:
            self.relay.deactivate_relay(d)

        # activate default relay
        self.relay.activate_relay(0)

    def run(self):
        self.startup_routine()
        time_switched = time.time()
        self.high = True
        while True:
            if self.turnoff:
                self.relay.deactivate_relay(0)
                return
            
            time_since_switched = time.time() - time_switched
            if time_since_switched > 5:
                self.high = not self.high
                time_switched = time.time()
                #print("Switched to " + str(self.high) + " at " + str(time_switched)+ " and relay value is " + str(self.relay.check_relay(0)))
            # sample to see if pin is low or high. Pin high = low heat and vice versa. Don't worry about it.
            relay_value = self.relay.check_relay(0)
            # if high and pin is high, set to low
            if self.high and relay_value > .5:
                self.relay.deactivate_relay(0)
            # if low and pin is high, set to low 
            elif (not self.high) and relay_value < .5:
                self.relay.activate_relay(0)

            time.sleep(.05) # 20 hz
