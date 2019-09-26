import cv2
import numpy as np
cap = cv2.VideoCapture(0)

while cv2.waitKey(1) < 0 or False:
    hasframe, img = cap.read()
    for x in range(100):
        cv2.circle(img, (x,100),80,(0,20,200),10)

    cv2.imshow("came",img)
