# 2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición indicada.
# Posteriormente, muestra la serie completa hasta la posición que el usuario especifique.

def fibonacci(pos):
    # Casos base
    if pos == 0:
        return 0
    elif pos == 1:
        return 1
    # Paso recursivo
    return fibonacci(pos - 1) + fibonacci(pos - 2)

n = int(input("Ingrese la cantidad de términos de la serie Fibonacci: "))
for i in range(n):
    print(fibonacci(i), end=" ")
