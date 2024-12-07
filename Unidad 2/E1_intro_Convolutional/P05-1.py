from keras.api.utils import load_img, img_to_array #alternative 3
from keras.src.utils import array_to_img
import matplotlib.pyplot as plt

largo, alto = 250, 250
file = 'charles.jpg'

# Cargar imagen original en escala de grises
img_original = load_img(file, target_size=(largo, alto), color_mode="grayscale")
img_a_convolucinar = img_to_array(img_original)

print("Tamaño de la imagen:", img_a_convolucinar.shape)

# Colocamos kernel, en este caso 6
kernels = [

    # Identity (sin cambio)
    [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ],

    #Edge Detection V1
    [
        [0, -1, 0],
        [-1, 4, -1],
        [0, -1, 0]
    ],

    # Edge Detection V2
    [
        [-1, -1, -1],
        [-1, 8, -1],
        [-1, -1, -1]
    ],

    # Sharpen
    [
        [0, -1, 0],
        [-1, 5, -1],
        [0, -1, 0]
    ],
    # Box Blur (normalizado)
    [
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1]
    ],

    # Guissian Blur 3*3
    [
        [1, 2, 1],
        [2, 4, 2],
        [1, 2, 1]
    ],

]


# Función para aplicar la convolución con un kernel dado
def aplicar_convolucion(img_a_convolucinar, kernel):
    img_convolucionada = []  # nueva imagen
    for filas in range(1, alto - 1):  # recorrido omitiendo los bordes de la imagen
        new_fila = []
        for columnas in range(1, largo - 1):  # ignora los píxeles de la primera y última columna
            pixelConvulucionado = 0 #aqui se guarda el nuevo valor del pixel
            for f_kernel in range(len(kernel)):  # 0 1 2  #recorre el kernel (filas)
                for c_kernel in range(len(kernel)):  # 0 1 2 (columnas)
                    pixelConvulucionado += (kernel[f_kernel][c_kernel] * #hace la multiplicacion del valor del kernel por el pixel de la imagen
                                            img_a_convolucinar[filas + (f_kernel - 1)][columnas + (c_kernel - 1)])

            pixelConvulucionado = pixelConvulucionado * (1 / 9)  # ajustar la intensidad
            new_fila.append(pixelConvulucionado) #(se añade pixelConv ala nueva fila)

        img_convolucionada.append(new_fila)

    return array_to_img(img_convolucionada) #convierte la matriz a imagen denuevo


# Visualización imagenes
plt.figure(figsize=(15, 10)) #tamaño 10*15

# Mostrar la imagen original
plt.subplot(2, 4, 1) #2 filas 4 columnas 1=imagen original
plt.xticks([]), plt.yticks([])
plt.imshow(img_original, cmap='gray') #color gris
plt.title("Original")

# Aplicar y mostrar la convolución con cada kernel a la imagen
for i, kernel in enumerate(kernels): #enumera los kernels por llaves y hace un conteo de i++ y los aplica
    img_convolucionada = aplicar_convolucion(img_a_convolucinar, kernel) #aplica el metodo de convolucion

    # Mostrar cada imagen convolucionada de cada kernel
    plt.subplot(2, 4, i + 2)
    plt.xticks([]), plt.yticks([])
    plt.imshow(img_convolucionada, cmap='gray')
    plt.title(f'Kernel {i + 1}')

plt.tight_layout() #ajusta separacion para no amontonar imagenes
plt.show() #visualiza la imagen

# save_img('imagen_convolucionada.jpg', img_convolucionada)
