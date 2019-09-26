import cv2
import numpy as np

img = cv2.imread('Halftone_Gaussian_Blur.jpg')
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
img_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)

cv2.imshow('Original', img)
cv2.imshow('img_rgb', img_rgb)
cv2.imshow('img_gray', img_gray)
cv2.imshow('img_hsv', img_hsv)
cv2.imshow('img_yuv', img_yuv)
cv2.waitKey(0)
