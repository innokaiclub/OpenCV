import cv2
import numpy as np
cap = cv2.VideoCapture(0)

while cv2.waitKey(1) < 0 or False:
    hasframe, img = cap.read()
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    img_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)

    cv2.imshow('Original', img)
    cv2.imshow('img_rgb', img_rgb)
    cv2.imshow('img_gray', img_gray)
    cv2.imshow('img_hsv', img_hsv)
    cv2.imshow('img_yuv', img_yuv)
