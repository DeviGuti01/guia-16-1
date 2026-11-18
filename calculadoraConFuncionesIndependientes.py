def sumar(a, b):
    return a + b


def restar(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        return "Error: no se puede dividir entre cero"
    return a / b


def calculadora():
    numero1 = float(input("Ingrese el primer número: "))
    numero2 = float(input("Ingrese el segundo número: "))

    print("\nSeleccione una operación:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")

    opcion = int(input("Ingrese una opción: "))

    if opcion == 1:
        print("Resultado:", sumar(numero1, numero2))

    elif opcion == 2:
        print("Resultado:", restar(numero1, numero2))

    elif opcion == 3:
        print("Resultado:", multiplicar(numero1, numero2))

    elif opcion == 4:
        print("Resultado:", dividir(numero1, numero2))

    else:
        print("Opción no válida")


calculadora()