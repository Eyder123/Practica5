import math

def promedio(valores):
    return sum(valores) / len(valores)

def desviacion(valores):
    n = len(valores)
    prom = promedio(valores)
    suma = sum((x - prom) ** 2 for x in valores)
    return math.sqrt(suma / (n - 1))

# Entrada de datos
valores = list(map(float, input("Ingrese 10 números separados por espacio: ").split()))

# Cálculo y salida
prom = promedio(valores)
desv = desviacion(valores)

print(f"El promedio es {prom:.2f}")
print(f"La desviación estandar es {desv:.5f}")
