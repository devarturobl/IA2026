import cv2
import numpy as np
import imutils

cap = cv2.VideoCapture('pista.mp4')

#Substraccion de fondo
fgbg = cv2.bgsegm.createBackgroundSubtractorMOG()
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))

#Contador
car_counter = 0

while True:
    ret, frame = cap.read()
    if ret == False: 
        break

    frame = imutils.resize(frame, width=640)

    area_pts = np.array([[330,216], [frame.shape[1]-80,216], [frame.shape[1]-80, 271], [330,271]])

    #visualizar
    cv2.drawContours(frame, [area_pts], -1, (255,0,255), 2)
    cv2.line(frame, (450,216), (450,271), (0,255,255), 1)
    cv2.imshow('Frame', frame)

    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

cap.release()
cv2.destroyWindow()