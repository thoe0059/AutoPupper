from multiprocessing import connection
from .behaviorFunctions import *
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


class MessageInjectionInterface:
    def __init__(self, ActionLoopConnection: connection.Connection) -> None:
        self.connection = ActionLoopConnection


    def injectionLoop(self):
        # SLeep a second to prevent too much data sent at once.

        time.sleep(1)
        while True:
            coords = self.sensorLoop()
            if not coords:
                print("Waiting for tag")
            else:
                x, y, z = coords
                x, y, z = (1, 2, 3)
                #Test print to see if variables are loaded ok
                print(coords[2])
                if coords[2] < (-7):
                    print("Come closer")

    def sensorLoop(self):
        readData = ser.readline()
        if len(readData) > 0:
            msg = readData.split()
            XCord = float(msg[0])
            YCord = float(msg[1])
            ZCord = float(msg[2])
            return (XCord, YCord, ZCord)


    def injectionTest2Loop(self):
        # SLeep a second to prevent too much data sent at once.
        time.sleep(1)
        while True:
            coords = self.sensorLoop()
            if not coords:
                return print("No coordinates received")
                break
            else:
                x, y, z = coords
                x, y, z = (1, 2, 3)
                #Test print to see if variables are loaded ok
                print(coords)


    def injectionTest1Loop(self):
        coords = self.sensorLoop()
        if not coords:
            return print("No coordinates received")
        x, y, z = coords
        x, y, z = (1, 2, 3)
        #Test print to see if variables are loaded ok
        print(coords)
        print("Sending injection seconds")
        # time.sleep(1)
        self.connection.send(msg_Activation())
        self.connection.send(msg_Trot(interrupt = False))
        print("Injection sendt")
