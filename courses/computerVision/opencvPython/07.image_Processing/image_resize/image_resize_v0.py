#Usage:
# $ python3 image_resize_v0.py --image ../../Image/traffic1.jpg

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

#Calculate aspect ratio
aspect_ration = 150.0 / img.shape[1]

dim = (150, int(img.shape[0] * aspect_ration))

#Resize the Image
# img -> The image we want to resize
# dim -> Computed dimension for the new image
# interpolation -> Algorithm which does the resize
resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

#Create a window
cv2.namedWindow("Resized (Width)", cv2.WINDOW_AUTOSIZE)

# Load the new image on Opencv Window
cv2.imshow("Resized (Width)", resized)

#keyboard binding function
cv2.waitKey(0) & 0xFF
#simply destroys all the windows we created.
cv2.distroyAllWindow()