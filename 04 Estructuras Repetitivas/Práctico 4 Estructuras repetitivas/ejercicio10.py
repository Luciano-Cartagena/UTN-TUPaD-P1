#10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el 
#usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745. 

# Solicitamos al usuario que ingrese un número y lo convertimos a entero
numero = int(input("Ingrese un número para invertir: "))

# Convertimos el número a cadena (str), invertimos los caracteres con [::-1], 
# y luego lo volvemos a convertir a entero para eliminar ceros a la izquierda
numero_invertido = int(str(numero)[::-1])

# Mostramos en pantalla el número original ingresado por el usuario
print("Número original:", numero)

# Mostramos en pantalla el número invertido (con los dígitos al revés)
print("Número invertido:", numero_invertido)

