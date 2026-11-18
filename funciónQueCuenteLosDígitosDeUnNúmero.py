def contar_digitos(n):
    n = abs(n)

    if n == 0:
        return 1

    contador = 0

    while n > 0:
        n = n // 10
        contador = contador + 1

    return contador


numero = int(input("Ingrese un número entero: "))

resultado = contar_digitos(numero)

print("Cantidad de dígitos:", resultado)
