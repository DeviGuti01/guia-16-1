def celsius_fahrenheit(c):
    fahrenheit = (c * 9 / 5) + 32
    return fahrenheit


celsius = float(input("Ingrese los grados Celsius: "))

resultado = celsius_fahrenheit(celsius)

print("Temperatura en Fahrenheit:", resultado)