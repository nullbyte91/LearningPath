import numpy as np
import cv2

def rotate(image, angle, center = None, scale = 1.0):
    #Get Rows and colums details
    (h, w) = image.shape[:2]
    
    #Find a center point of image
    center = (w // 2, h // 2)

    #Calculates an affine matrix of 2D rotation.
    M = cv2.getRotationMatrix2D(center, angle, scale)

    return cv2.warpAffine(image, M, (w, h))