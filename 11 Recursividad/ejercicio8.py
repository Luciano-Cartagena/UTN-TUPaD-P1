# 8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un número entero positivo 
# y un dígito (0 a 9), y devuelva cuántas veces aparece ese dígito dentro del número.

def contar_digito(numero, digito):
    # Caso base: número sin dígitos
    if numero == 0:
        return 0
    # Comparar último dígito con el buscado
    return (1 if numero % 10 == digito else 0) + contar_digito(numero // 10, digito)

n = int(input("Número: "))
d = int(input("Dígito a contar (0-9): "))
print(f"Aparece {contar_digito(n, d)} veces.")
