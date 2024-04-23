import time

def fibonacci_recursivo(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursivo(n-1) + fibonacci_recursivo(n-2)

def fibonacci_iterativo(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

# Probar el tiempo de ejecución para la versión recursiva de Fibonacci
start_time = time.time()
fib_recursivo = fibonacci_recursivo(30)  # Cambiar el número según lo que desees probar
end_time = time.time()

timer_recursivo = end_time - start_time
print(f"Tiempo para Fibonacci recursivo: {timer_recursivo} segundos")

# Probar el tiempo de ejecución para la versión iterativa de Fibonacci
start_time = time.time()
fib_iterativo = fibonacci_iterativo(10000)  # Cambiar el número según lo que desees probar
end_time = time.time()

timer_iterativo = end_time - start_time
print(f"Tiempo para Fibonacci iterativo: {timer_iterativo} segundos")