#Tarea:

# Escribe un programa Python que solicite al usuario ingresar un número entero y luego determine en qué rango se encuentra ese número utilizando la declaración match. El programa debe imprimir un mensaje que indique el rango al que pertenece el número.



# Instrucciones:

#     1.   Pídele al usuario que ingrese un número entero.

#     2.  Utiliza la declaración match para clasificar el número en uno de los siguientes rangos:

#              Rango 1: Números negativos (menores que 0).

#               Rango 2: Números entre 0 (incluido) y 10 (excluido).

#               Rango 3: Números mayores o iguales a 10.

#     3.  Imprime un mensaje que indique en qué rango se encuentra el número ingresado.



# Los estudiantes deben escribir el código completo, incluyendo la captura de entrada del usuario, la declaración match para clasificar el número y la impresión del mensaje resultante. Este ejercicio les permite practicar el uso de múltiples casos en una declaración match y tomar decisiones basadas en rangos numéricos.

#Solución

# Pídele al usuario que ingrese un número entero
numero = int(input("Ingresa un número entero: "))

# Utiliza la declaración match para clasificar el número en uno de los rangos
match numero:
    case negativo if numero < 0:
        mensaje = "El número pertenece al Rango 1: Números negativos."
    case rango_0_10 if 0 <= numero < 10:
        mensaje = "El número pertenece al Rango 2: Números entre 0 (incluido) y 10 (excluido)."
    case rango_10_o_mas if numero >= 10:
        mensaje = "El número pertenece al Rango 3: Números mayores o iguales a 10."
    case _:
        mensaje = "Número no clasificado en los rangos especificados."

# Imprime un mensaje que indique en qué rango se encuentra el número ingresado
print(mensaje)
