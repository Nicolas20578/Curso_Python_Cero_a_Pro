nombre = "marco"
apellido = "MENDOZA"
frace = "Hola Esta Es una Frace"

longitud = len(frace)
print(longitud)

print(apellido[6])

palabras = frace.split()
print(palabras)
mayusculas = frace.upper()
print(mayusculas)
texto = apellido.lower()
print(texto)

mensaje = "Hola, Mundo"
print(mensaje)
cambio = mensaje.replace("Hola", "Marco")
print(cambio)

for x in apellido:
    print(x)
