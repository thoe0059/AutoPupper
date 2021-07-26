#Earlier UART_test_7.py

import time
import serial
ser = serial.Serial(
port = '/dev/ttyS0',
baudrate = 115200,
parity=serial.PARITY_NONE,
stopbits=serial.STOPBITS_ONE,
bytesize=serial.EIGHTBITS,
timeout=1
)
counter = 0
readData = []



while 1:
	#print ("While loop started")
	readData = ser.readline()
	#Checking if something is in the list. readData == 1
	if len(readData) > 0:
		msg = readData.split()
		XCord = float(msg[0])
		YCord = float(msg[1])
		ZCord = float(msg[2])
		print (XCord, YCord, ZCord)

		#print (msg)
