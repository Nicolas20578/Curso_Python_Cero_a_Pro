frutas = ["manzana", "banana", "cereza", "naranja"]
contador = 0

# Bucle for que itera sobre la lista de frutas
for fruta in frutas:
    contador += 1
    print(f"Fruta #{contador}: {fruta}")
    if contador == 1:
        break
   