import qi
import argparse
import sys
import time


def main(session):
    """
    This example uses the loadApplication method.
    To Test ALTabletService, you need to run the script ON the robot.
    """
    # Get the service ALTabletService.

    try:
        tabletService = session.service("ALTabletService")
        tabletService.cleanWebview()
        tabletService.loadApplication("shape-game")
        #tabletService.loadApplication("robot-page")
        # tabletService.showWebview("http://198.18.0.1/apps/shape-game/index.html")
        #tabletService.showWebview("http://www.google.com")
        tabletService.showWebview()

        # Ensure that the tablet wifi is enable
        # tabletService.enableWifi()

        # Display a web page on the tablet
        # tabletService.showWebview("http://www.google.com")
        #tabletService.showWebview("http://198.18.0.1/apps/boot-config/preloading_dialog.html")
        
        time.sleep(3)

        # Hide the web view
        # tabletService.hideWebview()
    except Exception, e:
        print "Error was: ", e


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="128.237.236.27",
                        help="Robot IP address. On robot or Local Naoqi: use '128.237.236.27'.")
    parser.add_argument("--port", type=int, default=9559,
                        help="Naoqi port number")

    args = parser.parse_args()
    session = qi.Session()
    try:
        session.connect("tcp://" + args.ip + ":" + str(args.port))
    except RuntimeError:
        print ("Can't connect to Naoqi at ip \"" + args.ip + "\" on port " + str(args.port) +".\n"
               "Please check your script arguments. Run with -h option for help.")
        sys.exit(1)
    main(session)