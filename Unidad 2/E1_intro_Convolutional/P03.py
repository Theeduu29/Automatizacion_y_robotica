
from keras.api.utils import load_img, img_to_array

largo, alto = 1000, 1000
file = '/E1_intro_Convolutional/wilches.jpg'
file1 = 'C:\\Python\\Unidad2-robotica\\eduardo.jpg'
file2 = 'C:\\Python\\Unidad2-robotica\\charles.jpg'

img = load_img(file, target_size=(largo, alto), color_mode="grayscale")
img1 = load_img(file1, target_size=(largo, alto), color_mode="grayscale")
img2 = load_img(file2, target_size=(largo, alto), color_mode="grayscale")

print(img.size)
print(img.mode)
print(img1.size)
print(img1.mode)
print(img2.size)
print(img2.mode)

imagen_en_array = img_to_array(img)
imagen_en_array1 = img_to_array(img1)
imagen_en_array2 = img_to_array(img2)

def guardar_imagen_csv(imagen_array, nombre_archivo):
    archivo = open(nombre_archivo, "w")
    for i in imagen_array:
        for j in i:
            archivo.write(str(j[0]) + ",")
        archivo.write("\n")
        archivo.flush()
    archivo.close()

guardar_imagen_csv(imagen_en_array, "./imagen_wilches.csv")
guardar_imagen_csv(imagen_en_array1, "./imagen_eduardo.csv")
guardar_imagen_csv(imagen_en_array2, "./imagen_charles.csv")

print("Archivos CSV creados correctamente.")