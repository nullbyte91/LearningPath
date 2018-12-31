# Will learn cv2.imread, cv2.namedWindow, cv2.imshow, cv2.imwrite, cv2.waitKey and cv2.distroyAllWindow
# using Matplotlib
import numpy as np  #Import Numpy Package
import cv2          #Import opencv Package
from matplotlib import pyplot as plt

#Load an image without change in pixel
img_color = cv2.imread('../Image/testImage.jpeg', cv2.IMREAD_UNCHANGED)

# Creates a window
cv2.namedWindow('Test_Image_Color',cv2.WINDOW_AUTOSIZE)
plt.imshow(img_color, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([]) # to hide tick values on X and Y axis
plt.show()

#Load an color image in grayscale
img_gray = cv2.imread('../Image/testImage.jpeg', cv2.IMREAD_GRAYSCALE)
# Creates a window
cv2.namedWindow('Test_Image_Gray ',cv2.WINDOW_AUTOSIZE)
plt.imshow(img_gray, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([]) # to hide tick values on X and Y axis
plt.show()
