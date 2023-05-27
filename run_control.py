import gpiozero
import socket
import time

# Function to activate the relay

def activate_relay(relay_num):
    relay = gpiozero.LED(relay_num)
    relay.on()
    return

# Function to deactivate the relay
def deactivate_relay(relay_num):
    relay = gpiozero.LED(relay_num)
    relay.off()
    return

# Function to check the status of the relay

def check_relay(relay_num):
    relay = gpiozero.LED(relay_num)
    return relay.value

# List of circuits and their resistances
relay_dict = {0:14,1:15,2:18,3:23}#4:24,5:25,6:8,7:7,8:12,9:16,10:20,11:21}
# 2700 ohm - GPIO xx
# 3333 ohm - GPIO xx
# 5000 ohm - GPIO xx
# 10000 ohm - GPIO xx
# Off - Turn on all GPIOs

# default is 2700 ohm
active_relay = 0

# deactivate all relays for good measure
for d in relay_dict:
    deactivate_relay(list(d.values())[0])

# activate default relay
activate_relay(relay_dict[0])

# Open port
udp_ip = "127.0.0.1"
udp_port = 1337

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind((udp_ip,udp_port))

#  begin loop
t_start = time.time()
while time.time()-t_start < 60*10:
    #  read port
    data, addr = sock.recvfrom(8)
    data = data.decode('utf-8')
    try:
        data = int(data)
    except:
        data = -1
    #  switch by port value
    if data<0:
        deactivate_relay(relay_dict[active_relay])
    elif data>=0:
        if data == active_relay:
            pass
        deactivate_relay(relay_dict[active_relay])
        activate_relay(relay_dict[data])











