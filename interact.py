import qi

# Define Pepper IP address
IP = "128.237.236.27" # Press button on chest to get IP
PORT = 9559 # DO NOT CHANGE THIS!

# Define and connect main session
main_session = qi.Session()
main_session.connect("tcp://"+IP+":"+str(PORT))

# Animated speech
animated_speech_service = main_session.service("ALAnimatedSpeech")

# Text to Speech
text_to_speech_service = main_session.service("ALTextToSpeech")

# Animation
animation_service = main_session.service("ALAnimationPlayer")

# Basic Awareness
awareness_service = main_session.service("ALBasicAwareness")

# Motion
motion_service = main_session.service("ALMotion")

# Photocaputre and Tablet
tabletService = main_session.service("ALTabletService")
photoService = main_session.service("ALPhotoCapture")

# Define contextual configuration
configuration = {"bodyLanguageMode": "contextual"}


def say_welcome():
    # add specific animations, change voice?
    configuration = {"bodyLanguageMode":"contextual"}
    # animated_speech_service.say("Welcome to CMU! Happy to have you here", configuration, _async=True)
    future = animation_service.run("animations/Stand/Gestures/Hey_1", _async=True)
    animated_speech_service.say("Welcome to the AI Makerspace! It's great to have you here!", configuration)

def say(text):
    text_to_speech_service.setParameter("pitchShift", 1.0)
    configuration = {"bodyLanguageMode":"contextual"}
    animated_speech_service.say(text, configuration)

def say_bye():
    # add specific animations, change voice?
    configuration = {"bodyLanguageMode":"contextual"}
    future = animation_service.run("animations/Stand/Gestures/Hey_3", _async=True)
    animated_speech_service.say("Goodbye! It was nice to meet you!", configuration)

def main():

    #tabletService.showImage("https://www.drupal.org/files/styles/grid-4-2x/public/CMU_Logo_Stack_Red.png?itok=z-anp9I_")

    while True:
        text = raw_input("What should I say?\n")

        if text == "w":
            say_welcome()
        elif text == "b":
            say_bye()
        else:
            say(text)

if __name__ == '__main__':
    main()