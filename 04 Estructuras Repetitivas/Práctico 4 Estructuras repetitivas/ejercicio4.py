#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
#secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
#un 0.

CORTE = 0            # Definimos que el valor 0 sirve para terminar el programa
total = 0             # Inicializamos el acumulador para sumar los números

# Pedimos el primer número
numero = int(input(f"Ingrese un número ({CORTE} para cortar): "))

# Mientras el número ingresado sea distinto de 0 (CORTE), seguimos sumando
while numero != CORTE:
    total += numero   # Sumamos el número al total acumulado
    numero = int(input(f"Ingrese otro número ({CORTE} para cortar): "))  # Pedimos otro número

# Cuando el usuario ingresa 0, salimos del ciclo y mostramos el total acumulado
print("El total acumulado es:", total)

