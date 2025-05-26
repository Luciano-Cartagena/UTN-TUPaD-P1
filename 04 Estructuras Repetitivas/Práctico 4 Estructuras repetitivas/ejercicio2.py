#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
#dígitos que contiene.

# Pedimos un número entero al usuario
numero = int(input("Ingrese un número: "))

# Convertimos el número a positivo con abs(), luego a cadena con str(), y contamos sus caracteres con len()
contador = len(str(abs(numero)))

# Mostramos la cantidad de dígitos
print("El número contiene", contador, "dígitos.")
