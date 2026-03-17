import cv2
import numpy as np

cam = cv2.VideoCapture(0)
body_cascade = cv2.CascadeClassifier('haarcascade_fullbody.xml')

while True:

    ret, frame = cam.read()

    frame = cv2.flip(frame, 1)
    frame = cv2.resize(frame, (1000, 800))

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    bodies = body_cascade.detectMultiScale(
        gray,
        scaleFactor=1.05,
        minNeighbors=4,
        minSize=(80,160),
        maxSize=(400,700)
    )

    print(bodies)

    for (x, y, w, h) in bodies:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255,255,0), 2)

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()