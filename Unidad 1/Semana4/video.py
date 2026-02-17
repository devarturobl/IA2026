import cv2
import numpy as np

webcam = cv2.VideoCapture(0)
while True:
    ret, frame = webcam.read()
    width = int(webcam.get(3))
    height = int(webcam.get(4))
    
    if not ret:
        break   
    
    frame = cv2.flip(frame, 1)
    #cv2.imshow('Webcam', frame)

    ventana = np.zeros(frame.shape, np.uint8)
    small = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
    ventana[:height//2, :width//2] = cv2.rotate(small, cv2.ROTATE_180) #parte superior izquierda
    ventana[:height//2, width//2:] = cv2.rotate(small, cv2.ROTATE_180) #parte superior derecha
    ventana[height//2:, :width//2] = small #parte inferior izquierda
    ventana[height//2:, width//2:] = small #parte inferior derecha

    cv2.imshow('Interface', ventana)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

webcam.release()
cv2.destroyAllWindows()
