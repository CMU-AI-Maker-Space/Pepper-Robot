import qi
import time
import face_recognition
import cv2
import time
import os
import sys
import numpy as np
import pickle
import argparse
import vision_definitions
import traceback
from PIL import Image

# Define Pepper IP address
IP = "128.237.236.27"
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

def get_frame_pepper(nameID, videoService, width = 320, height = 240):
	# return a frame from Pepper
	try:
		# grab next frame
		result = videoService.getImageRemote(nameID)
		image = None
		if result == None:
			print 'cannot capture'
		elif result[6] == None:
			print 'no image data string.'
		else:
			image_string = str(result[6])
			im = Image.frombytes("RGB", (width, height), image_string)
			im.show()
			image = np.asarray(im)
	except Exception as e:
		print(str(e))
		traceback.print_exc()
	return image


def update_faces(frame, known_face_names, match_threshold, known_face_encodings, greeted, width = 320, height = 240):
	# for each input frame, recognise all the faces and for each face, update the list of known faces and encodings
	# for each face, either greet the known person or befriend the unknown person


	this_face_encodings = face_recognition.face_encodings(frame)
	this_face_locations = face_recognition.face_locations(frame)

	blank_image = blank_image = np.zeros((width,height,3), np.uint8)

	if not this_face_encodings is None:
		# found some faces in the frame
		for face_encoding in this_face_encodings:
			# begin by assuming the face has never been seen before
			name = "Unknown" # unknown face
			blank_image[:,:] = (0,0,255) # blank red image

			# compute distance between current face and all known faces
			distances = face_recognition.api.face_distance(known_face_encodings, face_encoding)
			# get the lowest distance
			distance_min_index = np.argmin(distances) # get index of best match
			distance_min = np.amin(distances) # get best match error

			# check if face matches any of the known face(s) by thresholding the lowest distance
			if distance_min < match_threshold:
				# face is a match, greet the known person
				name = known_face_names[distance_min_index] # get corresponding name
				blank_image[:,:] = (0,255,0) # set blank image to green        
				if not name in greeted: # greet the recognized person if not greeted already
					say("Nice to see you again, ", name)
			else:
				# face is not a match befriend the unknown person
				say("Hi! I've never met you before, I'm Pepper!")
				name = raw_input("What is your name?")
				greeted.append(name)
				known_face_names.append(name) # add to list of names
				known_face_encodings.append(face_encoding) # add to list of face encodings
		
	else:
		# no faces found
		print "No faces found"
	
	return known_face_encodings, known_face_names


def say_hi(name=""):
	# add specific animations, change voice?
	configuration = {"bodyLanguageMode":"contextual"}
	animated_speech_service.say("Hello!"+name, configuration)

def say_bye(name):
	# add specific animations, change voice?
	configuration = {"bodyLanguageMode":"contextual"}
	animated_speech_service.say("Bye "+str(name)+", it was nice to have you here at the AI Makerspace! Hope to see you again soon!", configuration)

def say_welcome():
	# add specific animations, change voice?
	configuration = {"bodyLanguageMode":"contextual"}
	# animated_speech_service.say("Welcome to CMU! Happy to have you here", configuration, _async=True)
	future = animation_service.run("animations/Stand/Gestures/Hey_3", _async=True)
	animated_speech_service.say("welcome to Carnegie Mellon University! We are glad you are here!", configuration)

def say(text):
	text_to_speech_service.setParameter("pitchShift", 1.0)
	# text_to_speech_service.setVoice("Kenny22Enhanced")
	# text_to_speech_service.say(text)
	configuration = {"bodyLanguageMode":"contextual"}
	animated_speech_service.say(text, configuration)

def pause(duration):
	time.sleep(duration)
	return