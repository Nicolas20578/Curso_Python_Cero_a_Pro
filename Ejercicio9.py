#contador = 10

#while contador >= 1:
#    print(contador)
#    contador -= 1

#print("!Feliz Año Nuevo¡")

suma = 0

numero = int(input("Ingresa un numero positivo (o un numero negativo para salir):"))

while numero >= 0:
    suma += numero
    numero = int(input("Ingresa un numero positivo (o un numero negativo para salir):"))

print("La suma de los numeros ingresados es:", suma)