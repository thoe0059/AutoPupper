from multiprocessing import connection
from .behaviorFunctions import *
import time
import serial

ser = serial.Serial(
port = '/dev/ttyACM0', # ttyS0 for direct TX/RX on GPIO, ttyACM0 for USB
baudrate = 115200, #Earlier 115200
parity=serial.PARITY_NONE,
stopbits=serial.STOPBITS_ONE,
bytesize=serial.EIGHTBITS,
timeout=1
)
counter = 0
readData = []


class MessageInjectionInterface:
    def __init__(self, ActionLoopConnection: connection.Connection) -> None:
        #Call connection, so robot is ready for actions messages.
        self.connection = ActionLoopConnection


    def injectionLoop(self):
        self.connection.send(msg_Activation())
        #self.connection.send(msg_Wait(20))
        # Sleep a second to prevent too much data sent at once.
        time.sleep(2)
        while True:
            coords = self.sensorLoop()
            #print(coords)

            #Is coords None, turn around to look for tags.
            if not coords:
                print("Looking...")
                self.connection.send(msg_TrotModded(5))
                self.connection.send(msg_Turn_Left(100))
                self.connection.send(msg_Wait(20))
                time.sleep(2)
            else: # Coords = (x, y, z), meaning that something is in the list.
                x, y, z = coords
                x, y, z = (1, 2, 3)


                if coords[2] <= (-4):
                    print("The distance is: ", coords[2])
                    print("Come closer")
                    self.connection.send(msg_TrotModded(10))
                    self.connection.send(msg_Forwards(100))
                    self.connection.send(msg_Wait(20))
                    time.sleep(2)


    def sensorLoop(self):
        readData = ser.readline()
        #Delay read of sensor data
        #time.sleep(1)
        if len(readData) > 0:
            msg = readData.split()
            XCord = float(msg[0])
            YCord = float(msg[1])
            ZCord = float(msg[2])
            return (XCord, YCord, ZCord)
            
