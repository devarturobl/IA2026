import numpy as np
import cv2

img = cv2.VideoCapture(0)
while True:
    ret, frame = img.read()
    frame = cv2.resize(frame, (800, 600))
    frame = cv2.flip(frame, 1)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    corners = cv2.goodFeaturesToTrack(gray, 400, 0.01, 10)
    corners = np.intp(corners)

    for corner in corners:
        x, y = corner.ravel()
        cv2.circle(frame, (x, y), 3, (255, 255, 255), -1)

    for i in range(len(corners)):
       for j in range(i + 1, len(corners)):
          corner1 = tuple(corners[i][0])
          corner2 = tuple(corners[j][0])
          color = tuple(map(lambda x: int(x), np.random.randint(0, 255, size=3)))
          cv2.line(frame, corner1, corner2, color, 1)
        
    cv2.imshow('Frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

img.release()
cv2.destroyAllWindows() 