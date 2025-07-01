# 4) Crear una función recursiva en Python que reciba un número entero positivo en base decimal 
# y devuelva su representación en binario como una cadena de texto.

def decimal_a_binario(n):
    # Caso base
    if n == 0:
        return ""
    # Paso recursivo: cociente y resto
    return decimal_a_binario(n // 2) + str(n % 2)

num = int(input("Número decimal a convertir: "))
binario = decimal_a_binario(num)
# Mostrar "0" si el número era 0
print(f"Binario: {binario if binario else '0'}")
