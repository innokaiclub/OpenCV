import cv2
import imutils

img = cv2.imread('road_sign.jpg')

rotated = imutils.rotate(img, -45)
rotated_bound = imutils.rotate_bound(img, 45)

cv2.imshow('rotated', rotated)
cv2.imshow('rotated_bound', rotated_bound)
cv2.waitKey(0)
