def calcular_factorial(*args):
    for numero in args:
        if numero >= 1:
            factorial = 1
            for i in range(2, numero + 1):
                factorial *= i
            print(f"{numero}! = {factorial}")
        else:
            print("El número debe ser positivo y mayor que cero.")

if __name__ == "__main__":
    while True:
        try:
            n = int(input("Introduce un número natural n: "))
            if n >= 1:
                break
            else:
                print("El número debe ser positivo y mayor que cero.")
        except ValueError:
            print("No has ingresado un número válido. Por favor, introduce un número natural.")

    calcular_factorial(n)
