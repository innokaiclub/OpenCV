import cv2
import numpy as np

img = cv2.imread('road_sign.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = cv2.bilateralFilter(img,9,75,75)
laplacian = cv2.Laplacian(img, cv2.CV_64F)

cv2.imshow('Original', img)
cv2.imshow('laplacian', laplacian)
cv2.waitKey(0)
