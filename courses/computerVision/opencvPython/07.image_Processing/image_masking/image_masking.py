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

mask = np.zeros(image.shape[:2], dtype = "uint8")

(cX, cY) = (image.shape[1] // 2, image.shape[0] // 2)

# cv.Rectangle(img, pt1, pt2, color, thickness=1, lineType=8, shift=0)
#img – Image.
#pt1 – Vertex of the rectangle.
#pt2 – Vertex of the rectangle opposite to pt1 .
#rec – Alternative specification of the drawn rectangle.
#color – Rectangle color or brightness (grayscale image).
#thickness – Thickness of lines that make up the rectangle. Negative values, like CV_FILLED , mean that the function has to draw a filled rectangle.
#lineType – Type of the line. See the line() description.
#shift – Number of fractional bits in the point coordinates.

cv2.rectangle(mask, (cX - 200, cY - 200), (cX + 200 , cY + 200), 
255, -1)
#Create a window for Mask
cv2.namedWindow("Mask", cv2.WINDOW_AUTOSIZE)
# Load the new image on Opencv Window
cv2.imshow("Mask", mask)

# Apply rectangle mask on original image
masked = cv2.bitwise_and(image, image, mask = mask)
#Create a window for final image
cv2.namedWindow("Final image", cv2.WINDOW_AUTOSIZE)
# Load the new image on Opencv Window
cv2.imshow("Final image", masked)

#keyboard binding function
cv2.waitKey(0) & 0xFF
#simply destroys all the windows we created.
cv2.distroyAllWindow()