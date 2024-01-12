personas = (("Juan", 25), ("Maria", 16), ("Carlos", 20))
for nombre, edad in personas:
    if edad < 18:
        print(nombre, edad)
        

numeros = (10, 20, 30, 40, 50, 100, 5000, 100000)

suma = sum(numeros)

print("La suma de los numeros es:", suma)