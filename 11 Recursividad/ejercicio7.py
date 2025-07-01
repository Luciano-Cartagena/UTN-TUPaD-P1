# 7) Un niño construye una pirámide de bloques colocando n en la base, n-1 en el siguiente nivel, etc.
# Escribí una función recursiva contar_bloques(n) que calcule el total necesario.

def contar_bloques(n):
    # Caso base: un solo bloque
    if n == 1:
        return 1
    # Paso recursivo: bloques del nivel actual + resto
    return n + contar_bloques(n - 1)

niveles = int(input("Bloques en el nivel más bajo: "))
print(f"Total de bloques: {contar_bloques(niveles)}")
