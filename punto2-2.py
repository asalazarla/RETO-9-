def tablas_de_multiplicar(*args):
    for numero in args:
        print(f"Tabla de multiplicar del {numero}:")
        for multiplicador in range(1, 11):
            producto = numero * multiplicador
            print(f"{numero} x {multiplicador} = {producto}")
        print("")

# Llamar a la función con los números del 1 al 9
tablas_de_multiplicar(*range(1, 10))