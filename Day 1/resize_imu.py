import cv2
import imutils

img = cv2.imread('road_sign.jpg')
resized_img = imutils.resize(img, 150)

cv2.imshow('Original', img)
cv2.imshow('resized_img', resized_img)
cv2.waitKey(0)
