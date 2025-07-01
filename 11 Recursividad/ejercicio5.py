# 5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una cadena de texto sin espacios ni tildes,
# y devuelva True si es un palíndromo o False si no lo es. No se debe usar [::-1] ni reversed().

def es_palindromo(palabra):
    # Caso base: una letra o ninguna, es palíndromo
    if len(palabra) <= 1:
        return True
    # Si los extremos no coinciden
    if palabra[0] != palabra[-1]:
        return False
    # Paso recursivo: comparar lo que queda
    return es_palindromo(palabra[1:-1])

texto = input("Ingrese una palabra (sin espacios ni tildes): ").lower()
print("Es palíndromo" if es_palindromo(texto) else "No es palíndromo")
