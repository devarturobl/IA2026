#Primer programa deteccion de puntos de mano con mediapipe
import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

cam = cv2.VideoCapture(0)

with mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=2,
    min_detection_confidence=0.5) as hands:

    while True:
        ret, frame = cam.read()
        if not ret:
            break

        # Convertir la imagen a RGB
        image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Procesar la imagen y detectar las manos
        results = hands.process(image_rgb)

        # Dibujar los puntos de referencia de las manos
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(
                    frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

        # Mostrar la imagen con las detecciones
        cv2.imshow('MediaPipe Hands', frame)

        # Salir con la tecla 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cam.release()
cv2.destroyAllWindows()




