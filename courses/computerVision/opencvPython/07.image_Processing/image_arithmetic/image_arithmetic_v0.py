#Usage:
# $ python3 image_arithmetic_v0.py --image ../../Image/traffic1.jpg

import argparse #argparse to handle parsing commandline
import cv2 #Import openCv Lib
import numpy as np #Import numpy package

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, 
    help = "path to the image")
args = vars(ap.parse_args())

#Load a image
image = cv2.imread(args["image"], cv2.IMREAD_UNCHANGED)

#Create a window
cv2.namedWindow("TestWindow", cv2.WINDOW_AUTOSIZE)
# Load the new image on Opencv Window
cv2.imshow("TestWindow", image)

#Image adddition 
M = np.ones(image.shape, dtype= "uint8") * 150
added = cv2.add(image, M)

#Create a window
cv2.namedWindow("Image addition", cv2.WINDOW_AUTOSIZE)
# Load the new image on Opencv Window
cv2.imshow("Image addition", added)

#Image subtraction
m = np.ones(image.shape, dtype= "uint8") * 25
subtraction = cv2.subtract(image, M)

#Create a window
cv2.namedWindow("Image subtraction", cv2.WINDOW_AUTOSIZE)
# Load the new image on Opencv Window
cv2.imshow("Image subtraction", subtraction)

#keyboard binding function
cv2.waitKey(0) & 0xFF
#simply destroys all the windows we created.
cv2.distroyAllWindow()