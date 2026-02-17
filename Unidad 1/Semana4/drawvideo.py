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

    # Dibujar una línea verde en el marco
    # frame es sobre donde estara la imagen
    # primer grupo es donde inicia en x Y y la linea
    # segundo grupo es donde termina la linea en x Y y
    # tercer grupo es el color de la linea en formato BGR (azul, verde, rojo)
    # cuarto grupo es el grosor de la linea
    frame = cv2.line(frame, (width//2, 0), (width//2, height), (0, 255, 0), 4)
    frame = cv2.line(frame, (0, height//2), (width, height//2), (0, 0, 255), 4)
    cv2.imshow('Frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

webcam.release()
cv2.destroyAllWindows()