import cv2
import numpy as np
cap = cv2.VideoCapture(0)

while cv2.waitKey(1) < 0 or False:
    hasframe, img = cap.read()
    cv2_blur = cv2.blur(img, (3,3))

    GaussianBlur = cv2.GaussianBlur(img,(5,5),0)

    medianBlur = cv2.medianBlur(img,5)

    bilateralFilter = cv2.bilateralFilter(img,9,75,75)

    cv2.imshow('Original', img)
    cv2.imshow('cv2 Blur', cv2_blur)
    cv2.imshow('GaussianBlur', GaussianBlur)
    cv2.imshow('medianBlur', medianBlur)
    cv2.imshow('bilateralFilter', bilateralFilter)
