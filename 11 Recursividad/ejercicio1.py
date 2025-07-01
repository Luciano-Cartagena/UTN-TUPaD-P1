# 1) Crea una función recursiva que calcule el factorial de un número.
# Luego, utiliza esa función para calcular y mostrar en pantalla el factorial de todos los números enteros entre 1 y el número que indique el usuario.

def factorial(n):
    # Caso base: factorial de 0 o 1 es 1
    if n == 0 or n == 1:
        return 1
    # Paso recursivo
    return n * factorial(n - 1)

# Entrada del usuario
num = int(input("Ingrese un número: "))
for i in range(1, num + 1):
    print(f"{i}! = {factorial(i)}")
