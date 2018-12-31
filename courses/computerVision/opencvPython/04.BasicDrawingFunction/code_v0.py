import numpy as np
import cv2

#Load an image without change in pixel
img_color = cv2.imread('../Image/testImage.jpeg', cv2.IMREAD_UNCHANGED)
# Draw a diagonal blue line with thickness of 5 px
img = cv2.line(img_color,(0,0),(511,511),(255,0,0),5)

#Drawing Rectangle
img = cv2.rectangle(img,(384,0),(510,128),(0,255,0),3)

#Drawing Circle
img = cv2.circle(img,(447,63), 63, (0,0,255), -1)

#Drawing Ellipse
img = cv2.ellipse(img,(256,256),(100,50),0,0,180,255,-1)

#Drawing Polygon
pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
pts = pts.reshape((-1,1,2))
img = cv2.polylines(img,[pts],True,(0,255,255))

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'OpenCV',(10,100), font, 4,(255,255,255),2,cv2.LINE_AA)

# Load the new image on Opencv Window
cv2.imshow('Test_Image_Gray', img)
#keyboard binding function
cv2.waitKey(0) & 0xFF
#simply destroys all the windows we created.
cv2.distroyAllWindow()
