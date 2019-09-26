import cv2
import numpy as np
cap = cv2.VideoCapture(0)

while cv2.waitKey(1) < 0 or False:
    hasframe, img = cap.read()
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.bilateralFilter(img,9,75,75)

    canny = cv2.Laplacian(img, cv2.CV_64F)

    cv2.imshow('canny', canny)
