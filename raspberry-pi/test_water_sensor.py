import smbus
import time

address = 0x48
bus = smbus.SMBus(1)
A0 = 0x48

while True:
	value = bus.read_byte(address)
	print(value)
	time.sleep(0.5)
