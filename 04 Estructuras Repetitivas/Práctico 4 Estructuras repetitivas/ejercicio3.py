#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
#dados por el usuario, excluyendo esos dos valores.

# Pedimos al usuario el primer número
numero_minimo = int(input("Ingrese el primer número: "))

# Pedimos al usuario el segundo número
numero_maximo = int(input("Ingrese el último número: "))

# Si el primer número es mayor que el segundo, los intercambiamos para que el rango funcione bien
if numero_minimo > numero_maximo:
    numero_minimo, numero_maximo = numero_maximo, numero_minimo

# Inicializamos la variable para acumular la suma
suma = 0

# Recorremos los números entre numero_minimo y numero_maximo, excluyendo los extremos
for contador in range(numero_minimo + 1, numero_maximo):
    suma += contador  # Sumamos cada número al acumulador

# Mostramos el resultado final
print("La suma de los números enteros entre", numero_minimo, "y", numero_maximo, "(excluyendo extremos) es:", suma)
