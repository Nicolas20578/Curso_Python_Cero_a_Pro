# Tarea

# Escribe un programa en Python que calcule el promedio de una lista de números. Debes seguir estos pasos:


#     Crea una lista llamada numeros que contenga al menos cinco números enteros.

#     Inicializa una variable llamada suma en 0.

#     Utiliza un ciclo for para iterar a través de la lista numeros y suma cada número a la variable suma.

#     Después del ciclo for, divide la variable suma entre la cantidad de números en la lista (que puedes obtener usando la función len(numeros)).

#     Imprime el resultado como el promedio de los números en la lista.

# Este ejercicio te ayudará a practicar la utilización de ciclos for, variables y operaciones matemáticas básicas en Python. ¡Buena suerte!

# Solucion

# Crea una lista llamada numeros que contenga al menos cinco números enteros.
numeros = [7, 15, 22, 18, 10]

# Inicializa una variable llamada suma en 0.
suma = 0

# Utiliza un ciclo for para iterar a través de la lista numeros y suma cada número a la variable suma.
for numero in numeros:
    suma += numero

# Después del ciclo for, divide la variable suma entre la cantidad de números en la lista.
cantidad_numeros = len(numeros)
promedio = suma / cantidad_numeros

# Imprime el resultado como el promedio de los números en la lista.
print("El promedio de los números en la lista es:", promedio)
