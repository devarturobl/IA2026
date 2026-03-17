import cv2
from ultralytics import YOLO

# cargar modelo
model = YOLO("yolov8n.pt")

# ancho real aproximado de una lata (cm)
REAL_WIDTH = 6.5

# distancia focal aproximada (ajustable)
FOCAL_LENGTH = 700

cap = cv2.VideoCapture(0)

while True:

    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.resize(frame,(960,720))

    results = model(frame, conf=0.25)

    for r in results:

        boxes = r.boxes

        for box in boxes:

            cls = int(box.cls[0])
            label = model.names[cls]

            if label in ["bottle","cup","vase"]:

                x1,y1,x2,y2 = map(int, box.xyxy[0])

                width_pixels = x2 - x1

                if width_pixels > 0:
                    distance = (REAL_WIDTH * FOCAL_LENGTH) / width_pixels
                else:
                    distance = 0

                cx = int((x1+x2)/2)
                cy = int((y1+y2)/2)

                # dibujar caja
                cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),2)

                # centro
                cv2.circle(frame,(cx,cy),5,(0,0,255),-1)

                # etiqueta
                text = f"{label} {distance:.1f} cm"

                cv2.putText(
                    frame,
                    text,
                    (x1,y1-10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.7,
                    (0,255,0),
                    2
                )

    cv2.imshow("Detector con distancia",frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()