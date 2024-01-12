# En esta tarea, se te pide crear un programa en Python que cuente desde 1 hasta un número límite ingresado por el usuario. El programa debe utilizar un bucle while para llevar a cabo el conteo y mostrar los números en orden ascendente. Una vez que se alcance el número límite, el programa debe imprimir "Conteo completado".

# Instrucciones:

#     Solicita al usuario que ingrese un número entero positivo como límite para el conteo.

#     Inicializa una variable llamada contador en 1.

#     Utiliza un bucle while para realizar el conteo desde 1 hasta el número límite ingresado por el usuario.

#     En cada iteración del bucle, muestra el valor actual de contador en la pantalla.

#     Después de imprimir el número actual, incrementa el valor de contador en 1 para pasar al siguiente número.

#     Cuando el valor de contador alcance o supere el número límite ingresado por el usuario, el bucle while debe detenerse.

#     Imprime "Conteo completado" para indicar que el conteo ha terminado.


# Solucion

# Solicita al usuario que ingrese un número entero positivo como límite para el conteo.
limite = int(input("Ingresa un número entero positivo como límite para el conteo: "))

# Inicializa una variable llamada contador en 1.
contador = 1

# Utiliza un bucle while para realizar el conteo desde 1 hasta el número límite ingresado por el usuario.
while contador <= limite:
    # En cada iteración del bucle, muestra el valor actual de contador en la pantalla.
    print(contador)
    
    # Después de imprimir el número actual, incrementa el valor de contador en 1 para pasar al siguiente número.
    contador += 1

# Cuando el valor de contador alcance o supere el número límite ingresado por el usuario, el bucle while se detendrá.
# Imprime "Conteo completado" para indicar que el conteo ha terminado.
print("Conteo completado")
