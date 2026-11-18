def mcd(a, b):
    a = abs(a)
    b = abs(b)

    while b != 0:
        residuo = a % b
        a = b
        b = residuo

    return a


def mcm(a, b):
    if a == 0 or b == 0:
        return 0

    resultado = abs(a * b) // mcd(a, b)

    return resultado


numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))

print("MCD:", mcd(numero1, numero2))
print("MCM:", mcm(numero1, numero2))