import cv2
import numpy as np

img = cv2.imread('road_sign.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = cv2.bilateralFilter(img,9,75,75)

canny = cv2.Canny(img, 50, 240)

cv2.imshow('Original', img)
cv2.imshow('canny', canny)
cv2.waitKey(0)
