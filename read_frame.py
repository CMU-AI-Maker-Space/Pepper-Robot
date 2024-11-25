from PIL import Image
import traceback
import numpy as np

def get_frame_pepper(nameID, videoService, width = 320, height = 240):
	# return a frame from Pepper
	try:
		# grab next frame
		result = videoService.getImageRemote(nameID)
		image = None
		if result == None:
			print('cannot capture')
		elif result[6] == None:
			print('no image data string.')
		else:
			image_string = str(result[6])
			im = Image.frombytes("RGB", (width, height), image_string)
			im.show()
			image = np.asarray(im)
	except Exception as e:
		print(str(e))
		traceback.print_exc()
	return image