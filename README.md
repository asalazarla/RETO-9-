# RETO 9
 
1. De los retos anteriores selecione 3 funciones y escribalas en forma de lambdas.
   -
* Como primer función, seleccioné la siguiente función: En 2022 el país A tendrá una población de 25 millones de habitantes y el país B de 18.9 millones. Las tasas de crecimiento anual de la población serán de 2% y 3% respectivamente. Desarrollar un algoritmo para informar en que año la población del país B superará a la de A. Extraída del **Reto 7, numeral 4**.

``` python
# Datos iniciales
poblacion_a = 25e6  # 25 millones
poblacion_b = 18.9e6  # 18.9 millones
tasa_a = 0.02  # 2%
tasa_b = 0.03  # 3%
año = 2022  # Año inicial

# Función de crecimiento anual
crecimiento_anual = lambda poblacion, tasa: poblacion + (poblacion * tasa)

# Ciclo while para calcular el crecimiento anual
while poblacion_b <= poblacion_a:
    # Crecimiento anual de la población
    poblacion_a = crecimiento_anual(poblacion_a, tasa_a)
    poblacion_b = crecimiento_anual(poblacion_b, tasa_b)
    # Incrementamos el año en cada iteración
    año += 1

# Al final del ciclo, se imprime el año en que la población de B supera a la de A
print("La población del país B superará a la del país A en el año", año)
```

* En segundo lugar, seleccioné la siguiente función: Imprimir el factorial de un número natural n dado. Extraída del **Reto 7, numeral 5**.
  
``` python
# Solicitar al usuario que ingrese un número natural n
n = int(input("Ingrese un número natural para calcular su factorial: "))

# Definir una función lambda para calcular el factorial
factorial = (lambda x: 1 if x == 0 else x * factorial(x - 1))

# Imprimir el resultado
print(f"El factorial de {n} es {factorial(n)}")

```

* Por último, seleccioné : Implementar un programa que ingrese un número de 2 a 50 y muestre sus divisores. Extraída del **Reto 7, numeral 7**
De los retos anteriores selecione 3 funciones y escribalas con argumentos no definidos (*args).
Escriba una función recursiva para calcular la operación de la potencia.
Utilice la siguiente plantilla de code para contar el tiempo:

``` python
# Se define lambda para verificar si un número está en el rango permitido
check_range = lambda x: True if 2 <= x <= 50 else False

# Se define lambda para imprimir los divisores de un número
print_divisors = lambda x: print(f"Los divisores de {x} son: {' '.join(str(i) for i in range(1, x + 1) if x % i == 0)}") if check_range(x) else print("Número fuera de rango. Por favor ingrese un número entre 2 y 50.")

# Solicitar al usuario que ingrese un número entre 2 y 50
numero = int(input("Ingrese un número entre 2 y 50: "))

# Llamar a la función para imprimir los divisores
print_divisors(numero)
```

2. De los retos anteriores selecione 3 funciones y escribalas con argumentos no definidos (*args).
   -
* Imprimir los números de 1 hasta un número natural n dado, cada uno con su respectivo factorial.  **Reto 8, numeral 4**.

``` python
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
```
  
* Diseñe un programa que muestre las tablas de multiplicar del 1 al 9. **Reto 8 , numeral 7**.

``` python
def tablas_de_multiplicar(*args):
    for numero in args:
        print(f"Tabla de multiplicar del {numero}:")
        for multiplicador in range(1, 11):
            producto = numero * multiplicador
            print(f"{numero} x {multiplicador} = {producto}")
        print("")

# Llamar a la función con los números del 1 al 9
tablas_de_multiplicar(*range(1, 10))
```

* Imprimir un listado con los números impares desde 1 hasta 999 y seguidamente otro listado con los números pares desde 2 hasta 1000.  **Reto 8, numeral 2**.
 
 ```python
def imprimir_numeros(*args):
    for inicio, fin in args:
        print(f"Números desde {inicio} hasta {fin}:")
        for numero in range(inicio, fin + 1):
            print(numero)
        print("")

# Llamar a la función con los rangos deseados
imprimir_numeros((1, 999), (2, 1000))
 ```
    
3. Escriba una función recursiva para calcular la operación de la potencia.
   -
``` python
def potencia(base, exponente):
    # Caso base
    if exponente == 0:
        return 1
    # Caso base para exponentes negativos
    elif exponente < 0:
        return 1 / potencia(base, -exponente)
    # Paso recursivo
    else:
        return base * potencia(base, exponente - 1)

# Ejemplo de uso
base = 2
exponente = 3
print(f"{base} elevado a la {exponente} es {potencia(base, exponente)}")
```
4. Utilice la siguiente plantilla de code para contar el tiempo:
   -
 ``` python
 import time

start_time = time.time()
# instrucciones sobre las cuales se quiere medir tiempo de ejecución
end_time = time.time()

timer = end_time - start_time
print(timer)
```
* Realice pruebas para calcular fibonacci con iteración o con recursión. Determine desde que número de la serie la diferencia de tiempo se vuelve significativa. Importante: Revisar este [hilo](https://stackoverflow.com/questions/8220801/how-to-use-timeit-module).

``` python
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
```

5. Crear cuenta en [stackoverflow](https://stackoverflow.com/) y adjuntar imagen en el repo:
   -
 [![Captura-de-pantalla-2024-04-22-162700.png](https://i.postimg.cc/WzVzgGWd/Captura-de-pantalla-2024-04-22-162700.png)](https://postimg.cc/cgDdNnNW)

6. Cosas de adultos....ir a [linkedin](https://www.linkedin.com/) y crear perfil....NO IMPORTA que estén iniciando, si tienen tiempo para redes poco útiles como fb, insta, o tiktok tienen tiempo para crear un perfil mamalón. Dejar enlace en el repo.
   -
https://www.linkedin.com/in/angie-carolina-salazar-lara-78665b305/
