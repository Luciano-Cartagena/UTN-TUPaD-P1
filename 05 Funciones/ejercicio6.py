# 6. Crear una función llamada tabla_multiplicar(numero) que reciba un
# número como parámetro y imprima la tabla de multiplicar de ese
# número del 1 al 10. Pedir al usuario el número y llamar a la función.

# Definimos la función que toma un número como parámetro
def tabla_multiplicar(numero):
    # Verificamos que el número esté entre 1 y 10
    if numero >= 1 and numero <= 10:
        # Recorremos del 1 al 10
        for i in range(1, 11):
            # Imprimimos cada línea de la tabla de multiplicar
            print(f"{numero} x {i} = {numero * i}")
    else:
        # Si el número no está entre 1 y 10, mostramos un mensaje de error
        print("ERROR. Ingrese un número del 1 al 10")

# Pedimos al usuario el número para mostrar su tabla
num = int(input("Ingrese un número para ver su tabla de multiplicar: "))
# Llamamos a la función con el número ingresado
tabla_multiplicar(num)
