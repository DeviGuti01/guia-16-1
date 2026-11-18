def invertir(cadena):
    if len(cadena) == 0:
        return ""

    return invertir(cadena[1:]) + cadena[0]


def es_palindromo(cadena):
    cadena = cadena.lower().replace(" ", "")

    if cadena == invertir(cadena):
        return True
    else:
        return False


texto = input("Ingrese una palabra o frase: ")

if es_palindromo(texto):
    print("La cadena es palíndroma")
else:
    print("La cadena no es palíndroma")