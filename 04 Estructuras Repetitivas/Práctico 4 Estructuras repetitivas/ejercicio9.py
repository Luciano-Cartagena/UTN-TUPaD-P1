#9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la 
#media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe 
#poder procesar 100 números cambiando solo un valor). 

# Definimos cuántos números queremos ingresar
cantidad_de_numeros = 100

# Inicializamos la variable suma en 0, donde vamos a acumular todos los números ingresados
suma = 0

# Bucle for que se ejecuta desde 1 hasta cantidad_de_numeros (inclusive)
for cont in range(1, cantidad_de_numeros + 1):
    # Pedimos al usuario que ingrese un número y lo convertimos a entero
    numero = int(input(f"Ingrese el número {cont}: "))
    
    # Sumamos ese número al acumulador 'suma'
    suma += numero

# Calculamos la media (promedio) dividiendo la suma total entre la cantidad de números
media = suma / cantidad_de_numeros

# Mostramos el resultado al usuario, indicando cuántos números se ingresaron y cuál es la media calculada
print(f"La media de los {cantidad_de_numeros} números ingresados es: {media}")


