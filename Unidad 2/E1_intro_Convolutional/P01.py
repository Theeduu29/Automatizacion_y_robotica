import os
from keras.api.utils import load_img

largo, alto = 1000, 1000
file = '/E1_intro_Convolutional/wilches.jpg'
file1 = 'C:\\Python\\Unidad2-robotica\\eduardo.jpg'
file2 = 'C:\\Python\\Unidad2-robotica\\charles.jpg'

# checan si los archovos existen
if os.path.exists(file) and os.path.exists(file1) and os.path.exists(file2):
    print(f"El archivo {file} existe.")
    print(f"El archivo {file1} existe.")
    print(f"El archivo {file2} existe.")

    # Cargar las imágenes
    img = load_img(file, target_size=(largo, alto), color_mode="grayscale")
    img1 = load_img(file1, target_size=(largo, alto), color_mode="grayscale")
    img2 = load_img(file2, target_size=(largo, alto), color_mode="grayscale")

    # imprime el roceso de las imagnees
    print(img.size)
    print(img.mode)
    print(img1.size)
    print(img1.mode)
    print(img2.size)
    print(img2.mode)

    # Mostrar las imágenes (en teoria)
    img.show()
    img1.show()
    img2.show()
else:
    if not os.path.exists(file):
        print(f"El archivo {file} no existe.")
    if not os.path.exists(file1):
        print(f"El archivo {file1} no existe.")
    if not os.path.exists(file2):
        print(f"El archivo {file2} no existe.")
