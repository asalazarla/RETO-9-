# Se define lambda para verificar si un número está en el rango permitido
check_range = lambda x: True if 2 <= x <= 50 else False

# Se define lambda para imprimir los divisores de un número
print_divisors = lambda x: print(f"Los divisores de {x} son: {' '.join(str(i) for i in range(1, x + 1) if x % i == 0)}") if check_range(x) else print("Número fuera de rango. Por favor ingrese un número entre 2 y 50.")

# Solicitar al usuario que ingrese un número entre 2 y 50
numero = int(input("Ingrese un número entre 2 y 50: "))

# Llamar a la función para imprimir los divisores
print_divisors(numero)