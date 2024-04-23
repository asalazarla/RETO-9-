def imprimir_numeros(*args):
   for inicio, fin in args:
       print(f"Números desde {inicio} hasta {fin}:")
       for numero in range(inicio, fin + 1):
           print(numero)
       print("")

# Llamar a la función con los rangos deseados
imprimir_numeros((1, 999), (2, 1000))