#from tensorflow.keras.utils import load_img, img_to_array
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

import matplotlib.pyplot as plt
plt.imshow(img, cmap='gray')
plt.imshow(img)
plt.xticks([]), plt.yticks([])
plt.show()

plt.imshow(img1, cmap='gray')
plt.imshow(img1)
plt.xticks([]), plt.yticks([])
plt.show()

plt.imshow(img2, cmap='gray')
plt.imshow(img2)
plt.xticks([]), plt.yticks([])
plt.show()