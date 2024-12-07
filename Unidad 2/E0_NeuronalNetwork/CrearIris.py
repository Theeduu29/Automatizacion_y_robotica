import random

# Definir los valores mínimos y máximos para las longitudes y anchuras
sepal_length_range = (4.3, 7.9)
sepal_width_range = (2.0, 4.4)
petal_length_range = (1.0, 6.9)
petal_width_range = (0.1, 2.5)

# Definir las clases de Iris
iris_classes = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']

# Este trozo generara los valores colocados en range entre los limites de arriba
data = []
for _ in range(1000):
    sepal_length = round(random.uniform(*sepal_length_range), 1)#Generan el valor entre el rango dado y coloca un decimal.
    sepal_width = round(random.uniform(*sepal_width_range), 1)
    petal_length = round(random.uniform(*petal_length_range), 1)
    petal_width = round(random.uniform(*petal_width_range), 1)
    iris_class = random.choice(iris_classes)
    data.append(f"{sepal_length},{sepal_width},{petal_length},{petal_width},{iris_class}")

# creara el archivo con el nombre que coloquemos
file_name = 'C:\\Python\\Unidad2-robotica\\E0_NeuronalNetwork\\iris.data'

# Guarda los datos en un .data con la especificacion solicitada.
with open(file_name, 'w') as file:
    file.write("sepal length (cm),sepal width (cm),petal length (cm),petal width (cm),class\n")
    file.write("\n".join(data))

file_name
