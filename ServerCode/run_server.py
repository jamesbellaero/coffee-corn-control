import socket
import time
from controllers.controller import Controller
from controllers.closed_loop_controller import ClosedLoopController
from controllers.open_loop_controller import OpenLoopController
from controllers.direct_controller import DirectController



# Open port
udp_ip = "10.0.0.158"
udp_port = 1337

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind((udp_ip,udp_port))

closed = ClosedLoopController()
open = OpenLoopController()
direct = DirectController()

controllers = [direct,open,closed]
controller_index = 0

#  begin loop
t_start = time.time()
while time.time() - t_start < 60*30:
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
        pass
    elif data == 0 or data == 1:
        ## Send to the direct controller
        if(controller_index != 0):
            controllers[controller_index].shutdown()
        controller_index = 0
        controllers[controller_index].start()
        print("Mode changed to direct controller")
    elif data == 2:
        ## Use the open loop controller
        if(controller_index!=1):
            controllers[controller_index].shutdown()
        controller_index=1
        controllers[controller_index].start()
        print("Mode changed to open loop controller")
    elif data == 3 or data == 4:
        ## Use the closed loop controller
        print("Mode changed to closed loop controller")
        pass

controllers[controller_index].shutdown()
