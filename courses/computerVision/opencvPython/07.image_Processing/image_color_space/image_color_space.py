#Usage:
# $ python3 image_splitting_merging_channels.py --image ../../images/beach.jpg

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
cv2.namedWindow("Orginal Image", cv2.WINDOW_AUTOSIZE)
# Load the new image on Opencv Window
cv2.imshow("Orginal Image", image)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#Create a window for Gray Scale image
cv2.namedWindow("Gray Scale image", cv2.WINDOW_AUTOSIZE)
# Load the new image on Opencv Window
cv2.imshow("Gray Scale image", gray)

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
#Create a window for hsv image
cv2.namedWindow("hsv image", cv2.WINDOW_AUTOSIZE)
# Load the new image on Opencv Window
cv2.imshow("hsv image", hsv)

lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
#Create a window for hsv image
cv2.namedWindow("lab image", cv2.WINDOW_AUTOSIZE)
# Load the new image on Opencv Window
cv2.imshow("lab image", lab)

#keyboard binding function
cv2.waitKey(0) & 0xFF
#simply destroys all the windows we created.
cv2.distroyAllWindow()