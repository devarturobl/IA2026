#Primer programa deteccion de puntos de mano con mediapipe
import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

cam = cv2.VideoCapture(0)
cv2.namedWindow('MediaPipe Hands', cv2.WINDOW_NORMAL)
cv2.resizeWindow('MediaPipe Hands', 1200, 900)

def is_finger_extended(hand_landmarks, tip_id, pip_id):
    wrist = hand_landmarks.landmark[0]
    tip = hand_landmarks.landmark[tip_id]
    pip = hand_landmarks.landmark[pip_id]
    d_tip = (tip.x - wrist.x)**2 + (tip.y - wrist.y)**2
    d_pip = (pip.x - wrist.x)**2 + (pip.y - wrist.y)**2
    return d_tip > d_pip

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
        all_hands = []
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(
                    frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                all_hands.append(hand_landmarks)

        # Si detecta exactamente 2 manos, conectar las puntas de los dedos con lineas
        # solo si el dedo está estirado en ambas manos
        if len(all_hands) == 2:
            h, w, _ = frame.shape
            finger_pairs = [
                (4, 2),   # pulgar: tip, pip
                (8, 6),   # indice
                (12, 10), # medio
                (16, 14), # anular
                (20, 18), # meñique
            ]
            for tip_id, pip_id in finger_pairs:
                extended0 = is_finger_extended(all_hands[0], tip_id, pip_id)
                extended1 = is_finger_extended(all_hands[1], tip_id, pip_id)
                if extended0 and extended1:
                    lm1 = all_hands[0].landmark[tip_id]
                    lm2 = all_hands[1].landmark[tip_id]
                    x1, y1 = int(lm1.x * w), int(lm1.y * h)
                    x2, y2 = int(lm2.x * w), int(lm2.y * h)
                    cv2.line(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)

        # Mostrar la imagen con las detecciones
        cv2.imshow('MediaPipe Hands', frame)

        # Salir con la tecla 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cam.release()
cv2.destroyAllWindows()




