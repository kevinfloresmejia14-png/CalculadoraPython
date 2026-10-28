def suma(num1, num2):
    return num1 + num2

def resta(num1, num2):
    return num1 - num2

def multiplicar(num1, num2):
    return num1 * num2

def dividir(num1, num2):
    if num2 == 0:
        return "Error: División por cero"
    return num1 / num2

def potencia(num1, num2):
    return num1 ** num2


num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

print("Suma:", suma(num1, num2))
print("Resta:", resta(num1, num2))
print("Multiplicación:", multiplicar(num1, num2))
print("División:", dividir(num1, num2))
print("Potencia:", potencia(num1, num2))