# Ejercicio 5
# Solicitar frase y mostrar palabras únicas y recuento de aparición

frase = input("Ingrese una frase: ")

palabras = frase.split()

# Palabras únicas usando set
palabras_unicas = set(palabras)

# Diccionario con cantidad de apariciones
recuento = {}
for palabra in palabras:
    recuento[palabra] = recuento.get(palabra, 0) + 1

print("Palabras únicas:", palabras_unicas)
print("Recuento:", recuento)
