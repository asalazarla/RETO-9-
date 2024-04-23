# Solicitar al usuario que ingrese un número natural n
n = int(input("Ingrese un número natural para calcular su factorial: "))

# Definir una función lambda para calcular el factorial
factorial = (lambda x: 1 if x == 0 else x * factorial(x - 1))

# Imprimir el resultado
print(f"El factorial de {n} es {factorial(n)}")
