#Usage:
# $ python3 code_v0.py 

from __future__ import print_function #Will be using print_function from __future__ rather than print statement
import cv2      #Opencv Lib
import numpy as np #Numpy package

#Load a image
img = cv2.imread("../images/traffic1.jpg")

#Create a Window
cv2.namedWindow('Test_Image', cv2.WINDOW_AUTOSIZE)

#Get the Image information
print ("height[Rows]: {} pixels".format(img.shape[0]))
print ("width[Column]: {} pixels".format(img.shape[1]))
print ("channels: {}".format(img.shape[2]))

"""We can access a pixel by it rows and column. And it returns 
an array of Blue, Green and Red values(BGR)."""

px = img[100,100]
print (px)

# accessing only blue pixel
blue = img[100,100,0]
print (blue)