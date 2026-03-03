import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.resize(frame, (800, 600))
    frame = cv2.flip(frame, 1)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    corners = cv2.goodFeaturesToTrack(gray, 800, 0.01, 10)

    # Crear fondo negro
    black = np.zeros_like(frame)

    if corners is not None:
        corners = np.intp(corners)

        # Dibujar puntos
        for corner in corners:
            x, y = corner.ravel()
            cv2.circle(black, (x, y), 3, (255, 255, 255), -1)

    cv2.imshow('Frame', black)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()