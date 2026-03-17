import cv2

webcam = cv2.VideoCapture(0)

while True:
    ret, frame = webcam.read()
    if not ret:
        break

    frame = cv2.rotate(frame, cv2.ROTATE_180)

    cv2.imshow('Webcam', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break   

webcam.release()
cv2.destroyAllWindows()
