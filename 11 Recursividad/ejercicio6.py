# 6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un número entero positivo
# y devuelva la suma de todos sus dígitos. No se puede convertir a string.

def suma_digitos(n):
    # Caso base: un solo dígito
    if n < 10:
        return n
    # Paso recursivo: suma último dígito + el resto
    return n % 10 + suma_digitos(n // 10)

numero = int(input("Ingrese un número: "))
print(f"Suma de sus dígitos: {suma_digitos(numero)}")
