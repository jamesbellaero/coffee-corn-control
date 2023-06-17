from mlx90614 import MLX90614
from smbus2 import SMBus
from time import sleep

bus = SMBus(1)
sensor = MLX90614(bus,address=0x5A)

while True:
    print("Ambient temperature: ",sensor.get_amb_temp())
    print("Object temperature: ",sensor.get_obj_temp())
    sleep(1)

#bus.close()













