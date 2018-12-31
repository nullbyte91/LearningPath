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

zeros = np.zeros(image.shape[:2], dtype = "uint8")

#Create a window for Red Channel
cv2.namedWindow("Red channel", cv2.WINDOW_AUTOSIZE)
# Load the new image on Opencv Window
cv2.imshow("Red channel", cv2.merge([zeros, zeros, R]))

#Create a window for Green Channel
cv2.namedWindow("Green Channel", cv2.WINDOW_AUTOSIZE)
# Load the new image on Opencv Window
cv2.imshow("Green Channel", cv2.merge([zeros, G, zeros]))

#Create a window for Blue Channel
cv2.namedWindow("Blue Channel", cv2.WINDOW_AUTOSIZE)
# Load the new image on Opencv Window
cv2.imshow("Blue Channel", cv2.merge([B, zeros, zeros]))

#keyboard binding function
cv2.waitKey(0) & 0xFF
#simply destroys all the windows we created.
cv2.distroyAllWindow()