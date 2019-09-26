import cv2
import numpy as np

img = cv2.imread('water.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# equalize the histogram of the input image
histeq = cv2.equalizeHist(img)
cv2.imshow('Input', img)
cv2.imshow('Histogram equalized', histeq)
cv2.waitKey(0)
