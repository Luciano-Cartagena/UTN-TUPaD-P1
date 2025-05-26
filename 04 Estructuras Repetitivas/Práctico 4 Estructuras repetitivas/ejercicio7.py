#7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un 
#número entero positivo indicado por el usuario.

# Inicializamos el acumulador (contador) en 0
contador = 0

# Pedimos al usuario que ingrese un número entero positivo
numero = int(input("Ingrese un número: "))

# Usamos un bucle for que recorra desde 0 hasta el número ingresado (inclusive)
for suma in range(0, numero + 1, 1):
    # Sumamos el valor actual (suma) al acumulador (contador)
    contador = suma + contador

# Mostramos el resultado final: la suma total de los números desde 0 hasta el número dado
print("La suma de los números entre 0 y", numero, "es:", contador)
 