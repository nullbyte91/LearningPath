#Usage:
# $ python3 image_flip_v0.py --image ../../Image/traffic1.jpg

import argparse #argparse to handle parsing commandline
import cv2 #Import openCv Lib
import numpy as np #Import numpy package

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "path to the image")
args = vars(ap.parse_args())

#Load a image
image = cv2.imread(args["image"], cv2.IMREAD_UNCHANGED)

#Create a window
cv2.namedWindow("TestWindow", cv2.WINDOW_AUTOSIZE)
# Load the new image on Opencv Window
cv2.imshow("TestWindow", image)

#Flipped Horizontally
flipped = cv2.flip(image, 1)
#Create a window
cv2.namedWindow("Flipped Horizontally", cv2.WINDOW_AUTOSIZE)
cv2.imshow("Flipped Horizontally", flipped)

#Flipped Vertically
flipped = cv2.flip(image, 0)
#Create a window
cv2.namedWindow("Flipped Vertically", cv2.WINDOW_AUTOSIZE)
cv2.imshow("Flipped Vertically", flipped)

#Flipped Horizontally & Vertically
flipped = cv2.flip(image, -1)
#Create a window
cv2.namedWindow("Flipped Horizontally & Vertically", cv2.WINDOW_AUTOSIZE)
cv2.imshow("Flipped Horizontally & Vertically", flipped)

#keyboard binding function
cv2.waitKey(0) & 0xFF
#simply destroys all the windows we created.
cv2.distroyAllWindow()