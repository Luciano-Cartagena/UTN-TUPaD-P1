# 7. Crear una función llamada operaciones_basicas(a, b) que reciba
# dos números como parámetros y devuelva una tupla con el resultado de sumarlos, 
# restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara

def operaciones_basicas(a, b):
    # Calcula la suma de a y b
    suma = a + b
    # Calcula la resta de a y b
    resta = a - b
    # Calcula la multiplicación de a y b
    multiplicacion = a * b
    # Calcula la división de a entre b
    division = a / b
    # Devuelve los cuatro resultados en una tupla
    return (suma, resta, multiplicacion, division)

# Pide al usuario que ingrese el primer número y lo convierte a float
num1 = float(input("Ingrese el primer número: "))
# Pide al usuario que ingrese el segundo número y lo convierte a float
num2 = float(input("Ingrese el segundo número: "))
# Llama a la función operaciones_basicas con los números ingresados y desempaqueta los resultados
suma, resta, multiplicacion, division = operaciones_basicas(num1, num2)

# Imprime el resultado de la suma
print(f"Suma: {suma}")
# Imprime el resultado de la resta
print(f"Resta: {resta}")
# Imprime el resultado de la multiplicación
print(f"Multiplicación: {multiplicacion}")
# Imprime el resultado de la división
print(f"División: {division}")

