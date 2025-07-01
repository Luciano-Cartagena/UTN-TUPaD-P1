# Ejercicio 10
# Invertir diccionario país -> capital a capital -> país

original = {
    "Argentina": "Buenos Aires",
    "Chile": "Santiago",
    "Brasil": "Brasilia"
}

invertido = {capital: pais for pais, capital in original.items()}

print("Original:", original)
print("Invertido:", invertido)
