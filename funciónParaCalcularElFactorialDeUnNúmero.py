def factorial(n):
    resultado = 1

    for i in range(1, n + 1):
        resultado = resultado * i

    return resultado


numero = int(input("Ingrese un número: "))

if numero < 0:
    print("No se puede calcular el factorial de un número negativo.")
else:
    resultado = factorial(numero)
    print("El factorial es:", resultado)