import argparse #argparse to handle parsing commandline
import cv2 #Import openCv Lib
import numpy as np

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "path to the image")
args = vars(ap.parse_args())

#Load a image
img = cv2.imread(args["image"], cv2.IMREAD_UNCHANGED)

#Create a window
cv2.namedWindow("TestWindow", cv2.WINDOW_AUTOSIZE)

# Load the new image on Opencv Window
cv2.imshow("TestWindow", img)

# Floating point array Matrix
M = np.float32( [[1, 0, 25], [0, 1, 50]] )

#Transformation function
shifted = cv2.warpAffine(img, M, (img.shape[1], img.shape[0]))

#Create a window
cv2.namedWindow("Shifted Down and Right", cv2.WINDOW_AUTOSIZE)
# Load the new image on Opencv Window
cv2.imshow("Shifted Down and Right", shifted)

# Floating point array Matrix
M = np.float32( [[1, 0, -50], [0, 1, -90]] )
shifted = cv2.warpAffine(img, M, (img.shape[1], img.shape[0]))

#Create a window
cv2.namedWindow("Shifted up and Left", cv2.WINDOW_AUTOSIZE)
# Load the new image on Opencv Window
cv2.imshow("Shifted up and Left", shifted)

#keyboard binding function
cv2.waitKey(0) & 0xFF
#simply destroys all the windows we created.
cv2.distroyAllWindow()

#Note:
###############################################################
# Our translation matrix M is defined as a floating point
# array – this is important because OpenCV expects this ma-
# trix to be of floating point type. The first row of the matrix
# is [ 1, 0, t x ] , where t x is the number of pixels we will shift
# the image left or right. Negative values of t x will shift the
# image to the left and positive values will shift the image to
# the right.
#
# Then, we define the second row of the matrix as [ 0, 1, t y ] ,
# where t y is the number of pixels we will shift the image up
# or down. Negative value of t y will shift the image up and
# positive values will shift the image down.

# Translation is the shifting of object’s location. If you know the shift in (x,y) direction, let it be (t_x,t_y)
# OpenCV provides two transformation functions, cv2.warpAffine and cv2.warpPerspective, with which you can have all kinds of transformations.

# OpenCV Reference - https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_imgproc/py_geometric_transformations/py_geometric_transformations.html
#################################################################

