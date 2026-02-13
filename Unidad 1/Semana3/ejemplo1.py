import cv2;

#Carga y manipulacion de imagenes
myimage = cv2.imread('img/logo.png')

#redimensionar la imagen
redimensionada = cv2.resize(myimage, (400, 400))

#Mostrar la imagen
cv2.imshow('Mi imagen', myimage)
cv2.imshow('Imagen redimensionada', redimensionada)

#redimencionar con proporcion a la imagen original
redimensionada_proporcion = cv2.resize(myimage, None, fx=2, fy=2)

cv2.imshow('Imagen redimensionada proporcional', redimensionada_proporcion)


#Rotar imagen tenemos 3 opciones por grado en sentido horario y antihorario
rotar = cv2.rotate(myimage, cv2.ROTATE_90_CLOCKWISE)
rotar2 = cv2.rotate(myimage, cv2.ROTATE_90_COUNTERCLOCKWISE)

cv2.imshow('Imagen rotada 90 grados horario', rotar)
cv2.imshow('Imagen rotada 90 grados antihorario', rotar2)


#Guardar una imagen en el disco
cv2.imwrite('storage/img_save.png', rotar2)

#Esperar a que se pulse una tecla
cv2.waitKey(1000)  
#Cerrar la ventana
cv2.destroyAllWindows() 

