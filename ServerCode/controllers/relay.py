import gpiozero
# List of circuits and their resistances

# 100 + 60 ohm - GPIO 14
# 60 ohm only - GPIO 15, 18, 23
# 60 ohm only - Turn on all GPIOs

class Relay:
    def __init__(self,relay_dict = {0:14,1:15,2:18,3:23}):
        if('relay' in globals()):
            globals()['relay'].shutdown()

        self.relay_dict = relay_dict
        self.relays = []    

        # committing a sin by putting a loop in the constructor
        for d in self.relay_dict:
            self.relays.append(gpiozero.LED(relay_dict[d]))

        globals()['relay'] = self

    def get_relay_dict(self):
        return self.relay_dict
    
    # Function to activate the relay    
    def activate_relay(self,relay_num):
        self.relays[relay_num].on()
        print("Turn on pin ", self.relay_dict[relay_num])
        return

    # Function to deactivate the relay
    def deactivate_relay(self,relay_num):
        self.relays[relay_num].off()
        print("Turn off pin ", self.relay_dict[relay_num])
        return

    # Function to check the status of the relay
    def check_relay(self,relay_num):
        return self.relays[relay_num].value
    
    def shutdown(self):
        for d in self.relay_dict:
            self.relays[d].off()
