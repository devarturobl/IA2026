# Trabajando con video y creando ventanas

# Crear ventanas numpy
    import numpy as np

## Capturar video codigo base

    import cv2
    import numpy as np

    webcam = cv2.VideoCapture(0)
        while True:
            ret, frame = webcam.read()
            
            if not ret:
                break   

            cv2.imshow('Webcam', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    webcam.release()
    cv2.destroyAllWindows()


webcam es un objeto que captura la informacion de mi cámara
el Ciclo While permite la captua constante y condicionada de la camara
ret y frame son dos objetos 1 que detecta la activacion de la camara y el otro la captura

    if not ret
es una condicion que finaliza el ciclo cuando la camara no es detectada

    cv2.imshow
nos muesta el contenido capturado en frame

    if cv2.waitKey(1) & 0xFF == ord('q'):
                break
Es una condicion de cierre para el ciclo cuando se precione la techa q minuscula

    webcam.release()
    cv2.destroyAllWindows()
Se ocupan para liberar el buffer de memoria ram de la variable y cerrar la aplicacion

### Complemento
Usamos flip para invertir la camara y que no se vea como espejo
    
    frame = cv2.flip(frame, 1)


