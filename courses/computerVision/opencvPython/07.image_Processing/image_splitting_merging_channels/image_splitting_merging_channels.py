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

# Get BGR(Blue, Green and Red) Value
(B, G, R) = cv2.split(image)

#Create a window for Red Channel
cv2.namedWindow("Red channel", cv2.WINDOW_AUTOSIZE)
# Load the new image on Opencv Window
cv2.imshow("Red channel", R)

#Create a window for Green Channel
cv2.namedWindow("Green Channel", cv2.WINDOW_AUTOSIZE)
# Load the new image on Opencv Window
cv2.imshow("Green Channel", G)

#Create a window for Blue Channel
cv2.namedWindow("Blue Channel", cv2.WINDOW_AUTOSIZE)
# Load the new image on Opencv Window
cv2.imshow("Blue Channel", B)

#Merge all the Red, Green and Blue channel 
merged = cv2.merge([B, G, R])
#Create a window for Merge BGR
cv2.namedWindow("BGR", cv2.WINDOW_AUTOSIZE)
# Load the new image on Opencv Window
cv2.imshow("BGR", merged)

#keyboard binding function
cv2.waitKey(0) & 0xFF
#simply destroys all the windows we created.
cv2.distroyAllWindow()