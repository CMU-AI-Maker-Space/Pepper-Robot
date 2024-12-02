import qi
from naoqi import ALProxy, ALBroker, ALModule
import time
import sys

robotIP = "127.0.0.1"
port = 9559

global humanEventWatcher
humanEventWatcher = None
memory = None

class HumanTrackedEventWatcher(ALModule):
    def __init__(self):
        ALModule.__init__(self, "humanEventWatcher")
        global memory
        memory = ALProxy("ALMemory", robotIP, port)
        memory.subscribeToEvent("ALBasicAwareness/HumanTracked",
                                "humanEventWatcher",
                                "onHumanTracked")
        
    def onHumanTracked(self, key, value, msg):
        if value >= 0:
            motion_service.setAngles("RShoulderPitch", -0.25, 0.2)
            motion_service.setAngles("RShoulderRoll", -0.5, 0.1)
            motion_service.setAngles("RElbowRoll", 1.5, 0.1)
            motion_service.setAngles("RWristYaw", -1.0, 0.1)
            time.sleep(1)
            motion_service.openHand("RHand")
            motion_service.openHand("RHand")


if __name__ == "__main__":
    session = qi.Session()
    session.connect("tcp://" + robotIP + ":" + str(port))
    event_broker = ALBroker("event_broker", "0.0.0.0", 0, robotIP, port)
    humanEventWatcher = HumanTrackedEventWatcher()
    basic_awareness = ALProxy("ALBasicAwareness", robotIP, port)
    motion = ALProxy("ALMotion", robotIP, port)
    motion_service = session.service("ALMotion")
    motion.wakeUp()
    basic_awareness.setEngagementMode("Unengaged")
    basic_awareness.startAwareness()
    # basic_awareness.setStimulusDetectionEnabled("Sound", False)
    try:
            while True:
                    time.sleep(1)
    except KeyboardInterrupt:
            event_broker.shutdown()
            sys.exit(0)
