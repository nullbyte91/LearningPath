#Usage:
# $ python3 image_cropping_v0.py --image ../../Image/traffic1.jpg

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

# Cropping 
cropped = image[30:120 , 240:335]
cv2.imshow("Cropped", cropped)

#keyboard binding function
cv2.waitKey(0) & 0xFF
#simply destroys all the windows we created.
cv2.distroyAllWindow()

#Notes:
################################################################
# We can accomplish image cropping by using NumPy array slicing.
# In order to perform our cropping, NumPy expects four indexes:
# 1. Start y: The starting y coordinate. In this case, we start at y = 30.
# 2. End y: The ending y coordinate. We will end our crop at y = 120.
# 3. Start x: The starting x coordinate of the slice. We start
#    the crop at x = 240.
# 4. End x: The ending x-axis coordinate of the slice. Our
#    slice ends at x = 335.
