# Will learn cv2.VideoCapture(), cv2.videoWriter()
#cap.isOpened() is used to verify the cap init
#Saving Video:
#       So we capture a video, process it frame-by-frame and we want to save that video. For images, it is very simple, just
#       use cv2.imwrite(). Here a little more work is required
#
#       We have to create a videoWriter object with codec information to store the video frame by frame.

import numpy as np
import cv2

cap = cv2.VideoCapture(0)
#Define the codec and create videoWriter objects
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))
#out = cv2.videoWriter("Simple.avi", fourcc, 20.0, (640,480))
#cv2.videoWriter - first arg    = output file name
#                - second arg   = codec
#                - Third arg    = The number of frames per seconds(fps)
#                - Fourth arg   = frame size

while(cap.isOpened()):
    # Capture frame by frame
    ret, frame = cap.read()
    if ret == True:
        
        # write the flipped frame
        out.write(frame)
        #Display the Original Frame
        cv2.imshow('org_frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break;
cap.release()
cap.destroyAllWindow()
