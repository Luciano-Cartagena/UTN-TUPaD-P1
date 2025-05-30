#10.Crear una función llamada calcular_promedio(a, b, c) que reciba
# tres números como parámetros y devuelva el promedio de ellos.
# Solicitar los números al usuario y mostrar el resultado usando esta función

# Definimos la función calcular_promedio que recibe tres números
def calcular_promedio(a, b, c):
    # Calculamos el promedio sumando los tres números y dividiendo entre 3
    return (a + b + c) / 3

# Solicitamos al usuario que ingrese la primera calificación
a = float(input("Ingrese la primer calificación: "))

# Solicitamos al usuario que ingrese la segunda calificación
b = float(input("Ingrese la segunda calificación: "))

# Solicitamos al usuario que ingrese la tercera calificación
c = float(input("Ingrese la tercera calificación: "))

# Llamamos a la función calcular_promedio con los tres valores ingresados
promedio = calcular_promedio(a, b, c)

# Mostramos el promedio calculado, formateado a dos decimales
print("El promedio de las calificaciones es: {:.2f}".format(promedio))
