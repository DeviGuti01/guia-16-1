def invertir(cadena):
    if len(cadena) == 0:
        return ""

    return invertir(cadena[1:]) + cadena[0]


texto = input("Ingrese una palabra: ")

resultado = invertir(texto)

print("Palabra invertida:", resultado)