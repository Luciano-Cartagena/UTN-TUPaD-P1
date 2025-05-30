# 8. Crear una función llamada calcular_imc(peso, altura) que reciba el
# peso en kilogramos y la altura en metros, y devuelva el índice de
# masa corporal (IMC). Solicitar al usuario los datos y llamar a la función 
# para mostrar el resultado con dos decimales.

# Definimos la función calcular_imc que recibe el peso y la altura como parámetros
def calcular_imc(peso, altura):
    # Calcula el IMC usando la fórmula: peso dividido por altura al cuadrado
    return peso / (altura ** 2)

# Solicitamos al usuario que ingrese su peso en kilogramos
peso = float(input("Ingrese su peso en Kg: "))

# Solicitamos al usuario que ingrese su altura en metros
altura = float(input("Ingrese su altura en metros: "))

# Llamamos a la función calcular_imc pasando los datos ingresados
imc = calcular_imc(peso, altura)

# Imprimimos el resultado del IMC formateado con dos decimales
print("Su Índice de Masa Corporal (IMC) es de: {:.2f}".format(imc))
