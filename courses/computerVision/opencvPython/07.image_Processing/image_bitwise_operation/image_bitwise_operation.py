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
cv2.namedWindow("Orginal Image", cv2.WINDOW_AUTOSIZE)
# Load the new image on Opencv Window
cv2.imshow("Orginal Image", image)

#Image bitwiseAnd
M = np.ones(image.shape, dtype= "uint8") * 150
bitwiseAnd = cv2.bitwise_and(image, M)

#Create a window
cv2.namedWindow("Image bitwiseAnd", cv2.WINDOW_AUTOSIZE)
# Load the new image on Opencv Window
cv2.imshow("Image bitwiseAnd", bitwiseAnd)

#Image bitwiseOR
bitwiseOR = cv2.bitwise_or(image, M)

#Create a window
cv2.namedWindow("Image bitwiseOR", cv2.WINDOW_AUTOSIZE)
# Load the new image on Opencv Window
cv2.imshow("Image bitwiseOR", bitwiseOR)

#Image bitwiseXOR
bitwiseXOR = cv2.bitwise_xor(image, M)

#Create a window
cv2.namedWindow("Image bitwiseXOR", cv2.WINDOW_AUTOSIZE)
# Load the new image on Opencv Window
cv2.imshow("Image bitwiseXOR", bitwiseXOR)

#Image bitwiseNot
bitwiseNot = cv2.bitwise_not(image, M)

#Create a window
cv2.namedWindow("Image bitwiseNot", cv2.WINDOW_AUTOSIZE)
# Load the new image on Opencv Window
cv2.imshow("Image bitwiseNot", bitwiseXOR)

#keyboard binding function
cv2.waitKey(0) & 0xFF
#simply destroys all the windows we created.
cv2.distroyAllWindow()