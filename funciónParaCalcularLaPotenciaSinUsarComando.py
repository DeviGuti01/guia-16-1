def potencia(base, exponente):
    resultado = 1

    if exponente >= 0:
        for i in range(exponente):
            resultado = resultado * base

        return resultado

    else:
        for i in range(abs(exponente)):
            resultado = resultado * base

        return 1 / resultado


base = float(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente: "))

if base == 0 and exponente < 0:
    print("Error: no se puede dividir entre cero")
else:
    resultado = potencia(base, exponente)
    print("Resultado:", resultado)