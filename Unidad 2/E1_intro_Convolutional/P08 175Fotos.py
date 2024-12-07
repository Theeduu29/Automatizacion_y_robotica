# pylint: disable=no-member

import cv2
import os

# Crear la carpeta "1" si no existe
folder_name = "Fotos//Eduardo"
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

# Iniciar la videocámara0
cam = cv2.VideoCapture(0)  # videcámara (0 para la cámara predeterminada)

# Contador de fotos00
contFotos = 00
totalFotos = 175  # Número total de fotos que deseas capturar

while contFotos < totalFotos:
    result, image = cam.read()  # Captura el frame
    if result:
        cv2.imshow("Camara_Principal", image)  # Muestra el video en una ventana

        # Guardar la imagen en la carpeta "1"
        file_name = os.path.join(folder_name, f"foto_{contFotos}.png")
        cv2.imwrite(file_name, image)
        contFotos += 1

        # Esperar brevemente entre fotos (ajusta si es necesario)
        cv2.waitKey(100)  # 100 milisegundos entre cada captura
    else:
        print("No image detected. Please try again")
        break

# Liberar la cámara y cerrar la ventana
cam.release()
cv2.destroyAllWindows()