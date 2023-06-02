import gpiozero
import socket
import time


class Relay:
    def __init__(self,relay_dict):
        self.relay_dict = relay_dict
        self.relays = []    

        # committing a sin by putting a loop in the constructor
        for d in relay_dict:
            self.relays.append(gpiozero.LED(relay_dict[d]))

    # Function to activate the relay
    def activate_relay(self,relay_num):
        self.relays[relay_num].on()
        print("Turn on relay ", self.relay_dict[relay_num])
        return

    # Function to deactivate the relay
    def deactivate_relay(self,relay_num):
        self.relays[relay_num].off()
        print("Turn on relay ", self.relay_dict[relay_num])
        return

    # Function to check the status of the relay
    def check_relay(self,relay_num):
        return self.relays[relay_num].value

# List of circuits and their resistances
relay_dict = {0:14,1:15,2:18,3:23}#4:24,5:25,6:8,7:7,8:12,9:16,10:20,11:21}
relay = Relay(relay_dict)
# 2700 ohm - GPIO 14
# 3333 ohm - GPIO 15
# 5000 ohm - GPIO 18
# 10000 ohm - GPIO 23
# Off - Turn on all GPIOs

# default is 2700 ohm
active_relay = 0

# deactivate all relays for good measure
for d in relay_dict:
    relay.deactivate_relay(relay_dict[d])

# activate default relay
relay.activate_relay(relay_dict[0])

# Open port
udp_ip = "10.0.0.158"
udp_port = 1337

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind((udp_ip,udp_port))

#  begin loop
t_start = time.time()
while time.time() - t_start < 60*20:
    #  read port
    data, addr = sock.recvfrom(8)
    data = data.decode('utf-8')
    print("Received: ", data)
    try:
        data = int(data)
    except:
        data = -1
    #  switch by port value
    if data<0:
        relay.deactivate_relay(active_relay)
    elif data>=0 and data<=3:
        if data == active_relay:
            pass
        relay.deactivate_relay(active_relay)
        relay.activate_relay(data)
        active_relay = data

for d in relay_dict:
    relay.deactivate_relay(d)

