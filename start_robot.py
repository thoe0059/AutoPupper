import multiprocessing
import time

from PupperAutomation.ActionLoop import ActionLoop
from PupperAutomation.MessageInjectionInterface import MessageInjectionInterface
import PupperAutomation.preLoadedQueues as Demos
from PupperAutomation.run_robot import run_robot as robotLoop
from queue import Queue




def main():

   if __name__ == "__main__":

        robot_conn, transLoop_conn = multiprocessing.Pipe()
        injection_conn, transLoop_reciever_conn = multiprocessing.Pipe()

        actionLoop = ActionLoop(transLoop_conn, transLoop_reciever_conn)

        injectionInterface = MessageInjectionInterface(injection_conn)

        #actionLoop.actionQueue = Demos.test()
        actionLoop.actionQueue = Queue()

        time.sleep(2)

        robot = multiprocessing.Process(target=robotLoop, args=(robot_conn, False,))
        transmission = multiprocessing.Process(target=actionLoop.start, args=())
        injecter = multiprocessing.Process(target=injectionInterface.injectionLoop, args=())
        sensor = multiprocessing.Process(target=injectionInterface.sensorLoop, args=())
        print("Injection done")


        # running processes
        robot.start()
        ## This sleep timer ensures that the robot is listening before the action transmission starts.
        time.sleep(1)

        transmission.start()
        injecter.start()
        sensor.start()

        # wait until processes finish
        robot.join()
        transmission.join()
        injecter.join()
        sensor.join()

        robot.terminate()
        transmission.terminate()
        injecter.terminate()
        sensor.terminate()



main()
