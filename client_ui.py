from pynput import keyboard
import socket
from math import inf
from time import sleep

class ClientUI:
    def __init__(self,socket):
        self.socket = socket

    def send_data(self,data):
        data = str(data)
        print("Sending data: " + data)
        self.socket.sendto(data.encode('utf-8'),("10.0.0.158",1337))
    
    def on_press(self,key):
        if key == keyboard.Key.esc:
            return False  # stop listener
        try:
            k = key.char  # single-char keys
        except:
            k = key.name  # other keys
            print("Weird key pressed: " + k + "\nPlease enter new key: ")

            return True
        if k in ['0','1', '2', '3', '4']:  # keys of interest
            # self.keys.append(k)  # store it in global-like variable
            k_int = int(k)
            if(k_int == 4):
                self.send_data("-1")
            else:
                self.send_data(k_int)
        
        print('Key pressed: ' + key.char + "\nPlease enter new key: ")
        
        return True


# Setup dict of indices to resistances
resistances = {0:2700,1:3333,2:5000,3:10000,4:inf}

# Setup UDP socket
udp_ip = "127.0.0.1"
udp_port = 1338
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#sock.bind((udp_ip,udp_port))

ui = ClientUI(sock)
# Wait for input


listener = keyboard.Listener(on_press=ui.on_press)
listener.start()  # start to listen on a separate thread

print("Please enter key: ")
while True:
    sleep(60)
    print("Still running...\n")


