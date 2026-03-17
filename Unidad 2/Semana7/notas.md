# Uso del Clasificador
Sintaxis básica
```python
objetos = clasificador.detectMultiScale(
    imagen,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30,30)
)
```
# Parámetros principales

| Parámetro | Explicación |
|---|---|
| imagen | Imagen donde se buscarán los objetos (generalmente en escala de grises). |
| scaleFactor | Factor de reducción de la imagen en cada escala. Ej: 1.1. |
| minNeighbors | Número mínimo de vecinos para aceptar una detección. |
| minSize | Tamaño mínimo del objeto a detectar. |

📌 Resumen de los 3 programas (cómo se hicieron, qué hacen y cómo trabajan)
1) detectordecara.py — detector de caras
Cómo se hizo:
Usa OpenCV (cv2) y un clasificador en cascada Haar (haarcascade_frontalface_default.xml).
Abre la cámara con VideoCapture(0) y procesar cada cuadro.
Qué hace:
Detecta caras en la imagen en tiempo real.
Dibuja un rectángulo amarillo sobre cada cara detectada.
Cómo trabaja:
Lee un frame de cámara.
Voltea horizontalmente y redimensiona.
Convierte a escala de grises.
Aplica detectMultiScale en el clasificador de cara.
Para cada cara encontrada, dibuja un rectángulo.
Muestra el frame en cv2.imshow y sale al presionar q.

2) detectacuerpo.py — detector de cuerpo completo
Cómo se hizo:
Similar al de cara, pero usa haarcascade_fullbody.xml.
Qué hace:
Detecta cuerpos completos (personas) en la cámara.
Dibuja rectángulos sobre cada cuerpo detectado.
Cómo trabaja:
Captura video y prepara frame.
Convierte a gris.
Llama body_cascade.detectMultiScale con parámetros scaleFactor=1.05, minNeighbors=4, minSize=(80,160), maxSize=(400,700).
Dibuja rectángulos en cada cuerpo detectado.
Muestra video en ventana y cierra con q.
3) detectordeojoizq.py — detector de ojo izquierdo
Cómo se hizo:
Usa haarcascade_lefteye_2splits.xml (clasificador Haar específico para ojo izquierdo).
Qué hace:
Detecta ojos (enfoque izquierdo) en tiempo real.
Dibuja rectángulos sobre las regiones detectadas.
Cómo trabaja:
Captura y prepara frame como los demás.
Convierte a gris.
Ejecuta eye_cascade.detectMultiScale con scaleFactor=1.1, minNeighbors=3, minSize=(30,30), maxSize=(120,120).
Dibuja rectángulos para los ojos detectados.
Muestra ventana y sale con q.
✅ Nota general
Los 3 programas son casi idénticos en estructura; cambian solo el archivo de cascada Haar y los parámetros de detección. Se usan para visión computacional básica con detección en tiempo real de patrones preentrenados (cara/cuerpo/ojo) a partir de la webcam.

Si quieres, te hago también un mini código común que pueda ejecutar los tres con un argumento (cara/cuerpo/ojo) para no tener 3 scripts separados.