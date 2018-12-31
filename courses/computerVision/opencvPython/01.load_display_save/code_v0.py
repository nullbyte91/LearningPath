#Usage:
# $ python3 code_v0.py --image ../Image/testImage.jpeg

from __future__ import print_function #Will be using print_function from __future__ rather than print statement
import argparse   #argparse to handle parsing commandline
import cv2      #Opencv Lib

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "path to the image")
args = vars(ap.parse_args())

#Load a image
img = cv2.imread(args["image"])
print ("height: {} pixels".format(img.shape[0]))
print ("width: {} pixels".format(img.shape[1]))
print ("channels: {}".format(img.shape[2]))

# Creates a window
cv2.namedWindow('Test_Image',cv2.WINDOW_AUTOSIZE)
# Load the new image on Opencv Window
cv2.imshow('Test_Image', img)

#keyboard binding function
cv2.waitKey(0) & 0xFF
