import cv2
#Inicia a captura de vídeo da webcam en una variable 
#Nota el numero de videoCapture puede variar dependiendo de la cantidad de cámaras conectadas a tu computadora, si tienes una cámara externa conectada, es posible que debas usar 1 o 2 en lugar de 0.
cap_video = cv2.VideoCapture(0)
#importante si queremos capturar video tenemos que crear un bucle infinito para que el programa no se cierre después de capturar un solo frame
#Este codigo se usa por default para mostrar el video en tiempo real, si quieres capturar un solo frame puedes usar el método read() de la variable cap_video y luego guardar ese frame como una imagen usando cv2.imwrite()
while True:
    #Lee un frame de la captura de video
    ret, frame = cap_video.read() 
    #Si se ha leído correctamente el frame, lo mostramos en una ventana
    if ret:
        cv2.imshow('Webcam', frame)   
    #Si el usuario presiona la tecla 'q', salimos del bucle
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
#Liberamos la captura de video y cerramos todas las ventanas
cap_video.release()
cv2.destroyAllWindows()
