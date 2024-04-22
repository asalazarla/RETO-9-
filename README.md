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

3. Escriba una función recursiva para calcular la operación de la potencia.
   -

5. Crear cuenta en stackoverflow y adjuntar imagen en el repo
   -
 [![Captura-de-pantalla-2024-04-22-162700.png](https://i.postimg.cc/WzVzgGWd/Captura-de-pantalla-2024-04-22-162700.png)](https://postimg.cc/cgDdNnNW)

6. Cosas de adultos....ir a linkedin y crear perfil....NO IMPORTA que estén iniciando, si tienen tiempo para redes poco útiles como fb, insta, o tiktok tienen tiempo para crear un perfil mamalón. Dejar enlace en el repo.
   -
https://www.linkedin.com/in/angie-carolina-salazar-lara-78665b305/
