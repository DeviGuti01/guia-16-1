def maximo_de_tres(a, b, c):
    if a >= b and a >= c:
        return a

    elif b >= a and b >= c:
        return b

    else:
        return c


numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))
numero3 = float(input("Ingrese el tercer número: "))

resultado = maximo_de_tres(numero1, numero2, numero3)

print("El número mayor es:", resultado)