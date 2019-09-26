import cv2

img = cv2.imread('road_sign.jpg')
resized_img = cv2.resize(img, (300,100))

cv2.imshow('Original', img)
cv2.imshow('resized', resized_img)
cv2.waitKey(0)
