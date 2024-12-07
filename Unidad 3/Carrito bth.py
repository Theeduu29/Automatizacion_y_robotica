import serial

# Crear un objeto serial
ser = serial.Serial('COM4', 9600)  # Reemplaza 'COM7' con el número de puerto de tu módulo HC05

def enviar(letra):
    ser.write(chr(letra).encode())
    print("Letra Enviada:", letra)

def menu():
    print("Seleccione una opción:")
    print("A. Izquierda (A)")
    print("D. Derecha (D)")
    print("S. Reversa (S)")
    print("W. Avanzar (W)")
    print("X. Detenerse (X)")
    print("V. Salir")

# Ciclo principal
while True:
    menu()
    opcion = input("Ingrese el número de la opción deseada: ")

    if opcion == 'A':
        enviar(65)  # Envía el número correspondiente a la letra 'A'
    elif opcion == 'D':
        enviar(68)  # Envía el número correspondiente a la letra 'D'
    elif opcion == 'S':
        enviar(87)  # Envía el número correspondiente a la letra 'S'
    elif opcion == 'W':
        enviar(83)  # Envía el número correspondiente a la letra 'W'
    elif opcion == 'X':
        enviar(88)  # Envía el número correspondiente a la letra 'X'
    elif opcion == 'V':
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Por favor, ingrese un número válido del menú.")

# Cerrar la conexión serial
ser.close()