# Will learn cv2.VideoCapture(), cv2.videoWriter()
#Convert BGR to HSV
#cap.isOpened() is used to verify the cap init

import numpy as np
import cv2

cap = cv2.VideoCapture(0)
while(cap.isOpened()):
    # Capture frame by frame
    ret, frame = cap.read()

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #Display the Original Frame
    cv2.imshow('org_frame', frame)
    #Display the hsv frame
    cv2.imshow('hsv_frame', hsv)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break;
cap.release()
cap.destroyAllWindow()
