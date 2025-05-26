#8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el 
#programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son 
#negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad 
#menor, pero debe estar preparado para procesar 100 números con un solo cambio).

# Definimos cuántos números queremos ingresar (se puede cambiar a 100 fácilmente)
cantidad_de_numeros = 100

# Inicializamos los contadores en 0
pares = 0        # cuenta cuántos números son pares
impares = 0      # cuenta cuántos números son impares
positivos = 0    # cuenta cuántos números son positivos (>0)
negativos = 0    # cuenta cuántos números son negativos (<0)

# Bucle que se repite la cantidad de veces especificada
for cont in range(1, cantidad_de_numeros + 1):
    # Solicitamos al usuario un número entero
    numero = int(input(f"Ingrese el número {cont}: "))
    
    # Verificamos si es par o impar usando el módulo (%)
    if numero % 2 == 0:
        pares += 1  # si es par, incrementamos el contador de pares
    else:
        impares += 1  # si es impar, incrementamos el contador de impares
    
    # Verificamos si es positivo o negativo
    if numero > 0:
        positivos += 1  # si es mayor que cero, sumamos a positivos
    elif numero < 0:
        negativos += 1  # si es menor que cero, sumamos a negativos
    # Nota: el cero no cuenta ni como positivo ni como negativo

# Mostramos los resultados al usuario
print("Cantidad de pares:", pares)
print("Cantidad de impares:", impares)
print("Cantidad de positivos:", positivos)
print("Cantidad de negativos:", negativos)
