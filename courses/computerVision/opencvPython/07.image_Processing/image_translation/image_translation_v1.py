#Usage:
# $ image_translation_v1.py --image ../../Image/traffic1.jpg

import argparse #argparse to handle parsing commandline
import cv2 #Import openCv Lib
import imutils

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "path to the image")
args = vars(ap.parse_args())

#Load a image
img = cv2.imread(args["image"], cv2.IMREAD_UNCHANGED)

#Create a window
cv2.namedWindow("TestWindow", cv2.WINDOW_AUTOSIZE)

# Load the new image on Opencv Window
cv2.imshow("TestWindow", img)

shifted = imutils.translate(img, 25, 50)

#Create a window
cv2.namedWindow("Shifted Down and Right", cv2.WINDOW_AUTOSIZE)
# Load the new image on Opencv Window
cv2.imshow("Shifted Down and Right", shifted)

#keyboard binding function
cv2.waitKey(0) & 0xFF
#simply destroys all the windows we created.
cv2.distroyAllWindow()
