import cv2
import numpy as np

cam = cv2.VideoCapture(0)
eye_cascade = cv2.CascadeClassifier('haarcascade_lefteye_2splits.xml')

while True:

    ret, frame = cam.read()

    frame = cv2.flip(frame, 1)
    frame = cv2.resize(frame, (1000, 800))

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    eyes = eye_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=3,
        minSize=(30,30),
        maxSize=(120,120)
    )

    for (x, y, w, h) in eyes:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255,255,0), 2)

    cv2.imshow("frame", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()