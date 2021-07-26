from multiprocessing import connection
from .behaviorFunctions import *
import time

from .AprilTag import *


class MessageInjectionInterface:
    def __init__(self, ActionLoopConnection: connection.Connection) -> None:
        self.connection = ActionLoopConnection

    def injectionLoop(self):

        print("Sending injection seconds")
        # time.sleep(1)
        self.connection.send(msg_Activation())
        self.connection.send(msg_Trot(interrupt = False))
        print("Injection sendt")
        print(AprilTag.XCord)
