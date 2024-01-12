#Tarea

# En este ejercicio, los estudiantes deben crear un programa en Python que verifique si una palabra ingresada por el usuario está presente en una tupla predefinida de palabras. El programa debe informar al usuario si la palabra está o no en la tupla.

# Instrucciones:

#     Crear una tupla llamada palabras que contenga varias palabras, por ejemplo, "manzana", "banana" y "cereza".

#     Solicitar al usuario que ingrese una palabra mediante la función input(). La palabra ingresada será almacenada en la variable palabra_buscar.

#     Utilizar una estructura condicional (un if y un else) para verificar si palabra_buscar está presente en la tupla palabras.

#     Si la palabra está en la tupla, imprimir "La palabra está en la tupla."

#     Si la palabra no está en la tupla, imprimir "La palabra no está en la tupla."

# Este ejercicio permite a los estudiantes practicar la creación y el uso de tuplas en Python, así como la utilización de estructuras condicionales para tomar decisiones en base a los datos ingresados por el usuario. También les enseña cómo comparar cadenas de texto y cómo utilizar la estructura if-else para manejar diferentes casos. Puedes alentar a los estudiantes a probar diferentes palabras para comprobar si están en la tupla y a experimentar con la lógica del programa.


# Solucion

# Crear una tupla llamada palabras que contenga varias palabras.
palabras = ("manzana", "banana", "cereza")

# Solicitar al usuario que ingrese una palabra mediante la función input().
palabra_buscar = input("Ingresa una palabra para buscar en la tupla: ")

# Utilizar una estructura condicional (if-else) para verificar si palabra_buscar está presente en la tupla palabras.
if palabra_buscar in palabras:
    # Si la palabra está en la tupla, imprimir "La palabra está en la tupla."
    print("La palabra está en la tupla.")
else:
    # Si la palabra no está en la tupla, imprimir "La palabra no está en la tupla."
    print("La palabra no está en la tupla.")
