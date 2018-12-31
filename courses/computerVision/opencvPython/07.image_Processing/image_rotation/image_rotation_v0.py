#Usage:
# $ python3 image_rotation_v0.py --image ../../Image/traffic1.jpg

import argparse #argparse to handle parsing commandline
import cv2 #Import openCv Lib
import numpy as np #Import numpy package

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "path to the image")
args = vars(ap.parse_args())

#Load a image
img = cv2.imread(args["image"], cv2.IMREAD_UNCHANGED)

#Create a window
cv2.namedWindow("TestWindow", cv2.WINDOW_AUTOSIZE)

# Load the new image on Opencv Window
cv2.imshow("TestWindow", img)

#Get Rows and colums details
(h, w) = img.shape[:2]
print ("Rows:{} ".format(h))
print ("Colums:{} ".format(w))

#Find a center point of image
center = (w // 2, h // 2)
print ("Center:", center)

#Calculates an affine matrix of 2D rotation.
M = cv2.getRotationMatrix2D(center, 45, 1.0)

rotated = cv2.warpAffine(img, M, (w, h))

#Create a window
cv2.namedWindow("Rotated by 45 Degrees", cv2.WINDOW_AUTOSIZE)
cv2.imshow("Rotated by 45 Degrees", rotated)

#keyboard binding function
cv2.waitKey(0) & 0xFF
#simply destroys all the windows we created.
cv2.distroyAllWindow()


