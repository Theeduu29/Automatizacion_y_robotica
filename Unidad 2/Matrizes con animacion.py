import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from prettytable import PrettyTable


# Función para generar nodos con coordenadas únicas
def generar_nodos(n):
    nodos = []  # Lista para almacenar los nodos
    coordenadas_generadas = set()  # Usamos un set para asegurar que las coordenadas no se repitan
    xPoints = []  # Lista para almacenar las coordenadas X de los nodos
    yPoints = []  # Lista para almacenar las coordenadas Y de los nodos

    for i in range(n):
        while True:  # Bucle para generar coordenadas únicas
            x = round(random.uniform(0.0, 10.0), 1)  # Coordenada X aleatoria entre 0.0 y 10.0
            y = round(random.uniform(0.0, 10.0), 1)  # Coordenada Y aleatoria entre 0.0 y 10.0
            if (x, y) not in coordenadas_generadas:  # Verificamos si la coordenada ya fue generada
                coordenadas_generadas.add((x, y))  # Añadimos la coordenada al set para evitar duplicados
                nodos.append((i + 1, x, y))  # Añadimos el nodo a la lista con ID, X e Y
                xPoints.append(x)  # Añadimos la coordenada X a la lista
                yPoints.append(y)  # Añadimos la coordenada Y a la lista
                break

    return nodos, xPoints, yPoints  # Retornamos la lista de nodos y las coordenadas X e Y


# Función para mostrar nodos en una tabla
def mostrar_nodos(nodos):
    tabla = PrettyTable()  # Creamos una tabla con PrettyTable
    tabla.field_names = ["Nodo", "X", "Y"]  # Definimos los encabezados de las columnas
    for nodo in nodos:
        tabla.add_row([nodo[0], nodo[1], nodo[2]])  # Añadimos cada nodo a la tabla
    print(tabla)  # Mostramos la tabla en la consola


# Función para calcular la matriz de distancias entre nodos
def calcular_matriz_distancias(xPoints, yPoints, n):
    puntos = np.array(list(zip(xPoints, yPoints)))  # Convertimos las coordenadas en un array de puntos
    distancias = np.zeros((n, n))  # Inicializamos una matriz de ceros para las distancias

    for i in range(n):
        for j in range(n):
            distancias[i, j] = np.linalg.norm(puntos[i] - puntos[j])  # Calculamos la distancia entre los nodos i y j

    print("Matriz de distancias:")
    print(distancias)  # Mostramos la matriz de distancias en la consola
    return distancias  # Retornamos la matriz de distancias


# Función para seleccionar aleatoriamente un nodo de inicio
def seleccionar_nodo_inicio(nodos):
    nodo_inicio = random.choice(nodos)  # Seleccionamos un nodo al azar de la lista de nodos
    print(f"Nodo de inicio seleccionado aleatoriamente: {nodo_inicio[0]}")  # Mostramos el nodo seleccionado
    return nodo_inicio  # Retornamos el nodo seleccionado


# Función para generar un recorrido aleatorio que pase por todos los nodos y vuelva al inicio
def generar_recorrido(nodos, nodo_inicio):
    ids_nodos = list(range(len(nodos)))  # Lista con los índices de todos los nodos
    random.shuffle(ids_nodos)  # Barajamos los índices para crear un recorrido aleatorio
    ids_nodos.remove(nodo_inicio[0] - 1)  # Removemos el nodo inicial de la lista (para que sea el primero y último)
    recorrido = [nodo_inicio[0] - 1] + ids_nodos + [
        nodo_inicio[0] - 1]  # Creamos el recorrido incluyendo el regreso al nodo inicial

    # Mostramos el recorrido generado
    inicio = recorrido[0] + 1  # Nodo inicial
    fin = recorrido[-1] + 1  # Nodo final
    ruta = [r + 1 for r in recorrido[1:-1]]  # Ruta intermedia entre nodos
    print(f"Recorrido generado:")
    print(f"Inicio en Nodo {inicio} → Ruta: {ruta} → Fin en Nodo {fin}")

    return recorrido  # Retornamos la lista del recorrido


# Función para mostrar los nodos de forma estática (Gráfico de Nodos)
def mostrar_grafico_nodos(fig1, xPoints, yPoints, nodos):
    ax1 = fig1.add_subplot(111)  # Añadimos un subplot (gráfico) a la figura 1
    ax1.set_title('Nodos')  # Título del gráfico
    ax1.set_xlabel('X')  # Etiqueta del eje X
    ax1.set_ylabel('Y')  # Etiqueta del eje Y
    ax1.grid()  # Activamos la cuadrícula
    ax1.set_xlim(0, 10)  # Limites del eje X
    ax1.set_ylim(0, 10)  # Limites del eje Y
    ax1.axhline(0, color='black', linewidth=0.5, ls='--')  # Línea horizontal en Y=0
    ax1.axvline(0, color='black', linewidth=0.5, ls='--')  # Línea vertical en X=0
    ax1.scatter(xPoints, yPoints, color='red')  # Dibujamos los nodos como puntos rojos

    # Añadimos etiquetas a los nodos
    for nodo in nodos:
        ax1.annotate(f"{nodo[0]}", (nodo[1], nodo[2]), textcoords="offset points", xytext=(-10, -10), ha='center')


# Función para animar el recorrido en otro gráfico
def animar_recorrido(fig2, recorrido, xPoints, yPoints):
    ax2 = fig2.add_subplot(111)  # Añadimos un subplot (gráfico) a la figura 2
    ax2.set_title('Recorrido Animado')  # Título del gráfico
    ax2.set_xlabel('X')  # Etiqueta del eje X
    ax2.set_ylabel('Y')  # Etiqueta del eje Y
    ax2.grid()  # Activamos la cuadrícula
    ax2.set_xlim(0, 10)  # Limites del eje X
    ax2.set_ylim(0, 10)  # Limites del eje Y
    ax2.axhline(0, color='black', linewidth=0.5, ls='--')  # Línea horizontal en Y=0
    ax2.axvline(0, color='black', linewidth=0.5, ls='--')  # Línea vertical en X=0

    # Dibujamos los nodos como puntos rojos
    ax2.scatter(xPoints, yPoints, color='red')

    # Etiquetamos los nodos en el gráfico
    for i in range(len(recorrido)):
        ax2.annotate(f"{recorrido[i] + 1}", (xPoints[recorrido[i]], yPoints[recorrido[i]]),
                     textcoords="offset points", xytext=(-10, -10), ha='center')

    # Punto azul que se moverá durante la animación
    point, = ax2.plot([], [], 'bo', markersize=10)

    # Línea azul que muestra el recorrido
    line, = ax2.plot([], [], 'b-', lw=2)

    # Función para actualizar la animación en cada frame
    def actualizar(frame):
        # Obtener las coordenadas del recorrido hasta el frame actual
        x_data = [xPoints[i] for i in recorrido[:frame + 1]]
        y_data = [yPoints[i] for i in recorrido[:frame + 1]]

        # Actualizar la posición del punto
        point.set_data([xPoints[recorrido[frame]]], [yPoints[recorrido[frame]]])

        # Actualizar la línea que une los nodos recorridos
        line.set_data(x_data, y_data)

        return point, line

    # Crear la animación con la función `FuncAnimation`
    anim = FuncAnimation(fig2, actualizar, frames=len(recorrido), interval=1000, repeat=False)

    # Retornar la animación para que no sea eliminada por el recolector de basura
    return anim


# Programa Principal
if __name__ == "__main__":
    # Paso 1: Generar los nodos
    numero_nodos = int(input("Valores: "))  # Pedimos el número de nodos al usuario
    nodos, xPoints, yPoints = generar_nodos(numero_nodos)  # Generamos los nodos y sus coordenadas

    # Mostrar los nodos generados en la consola
    mostrar_nodos(nodos)

    # Crear dos figuras distintas para los dos gráficos
    fig1 = plt.figure()  # Figura para mostrar los nodos estáticos
    fig2 = plt.figure()  # Figura para mostrar el recorrido animado

    # Mostrar el gráfico de los nodos estáticos
    mostrar_grafico_nodos(fig1, xPoints, yPoints, nodos)

    # Calcular la matriz de distancias entre los nodos
    calcular_matriz_distancias(xPoints, yPoints, numero_nodos)

    # Paso 2: Seleccionar un nodo de inicio y generar el recorrido
    nodo_inicio = seleccionar_nodo_inicio(nodos)  # Seleccionamos un nodo inicial al azar
    recorrido = generar_recorrido(nodos, nodo_inicio)  # Generamos el recorrido que pasa por todos los nodos

    # Animar el recorrido en una segunda figura
    anim = animar_recorrido(fig2, recorrido, xPoints, yPoints)

    # Mostrar ambas figuras al mismo tiempo
    plt.show()  # Muestra las dos gráficas (una estática y otra animada)
