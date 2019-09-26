import numpy as np
import cv2
img = cv2.imread('input_boomerang_shapes.png')

img = cv2.bilateralFilter(img,9,75,75)
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#canny = cv2.Canny(img, 50, 240)
ret, thresh = cv2.threshold(imgray, 127, 255, 0)
im2, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE,
cv2.CHAIN_APPROX_SIMPLE)

cnt = contours[2]
cv2.drawContours(img, cnt, -1, (0,255,255), 10)

print "number of contour is " + str(len(contours))
print (hierarchy)

cv2.imshow("img",img)
cv2.imshow("canny",thresh)
cv2.waitKey(0)
