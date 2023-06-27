import smbus
import time
import subprocess

address = 0x48
bus = smbus.SMBus(1)
A0 = 0x48

GOOD_WATER_LEVEL = 160

SERVER_URL = "http://10.0.0.61:8000/"

value = bus.read_byte(address)
if value < GOOD_WATER_LEVEL:
		print("Water is too low!, Requesting for an audio file")

		# get request from server
		subprocess.run(['rm', 'water.wav'])
		print("Communicating with server...")
		url = SERVER_URL + "water.wav"
		wget_proc = subprocess.run(['wget', url])

		# play the .wav file
		print("Success! Playing audio file...")
		subprocess.run(['aplay','water.wav'])

		# request a new wav file to play
		print("Prompting AI to make a new monologue...")
		url = SERVER_URL + "WATER"
		wget_proc = subprocess.run(['curl', url] )
