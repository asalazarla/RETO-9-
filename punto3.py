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
