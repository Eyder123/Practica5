import math

# Función que calcula el discriminante
def Discriminante(a, b, c):
    return b**2 - 4*a*c

# Función que devuelve la primera raíz
def Raiz1(a, b, discriminante):
    return (-b + math.sqrt(discriminante)) / (2 * a)

# Función que devuelve la segunda raíz
def Raiz2(a, b, discriminante):
    return (-b - math.sqrt(discriminante)) / (2 * a)

def resolverEcuacionCuadratica(a, b, c):
    discriminante = Discriminante(a, b, c)
    
    if discriminante > 0:
        r1 = Raiz1(a, b, discriminante)
        r2 = Raiz2(a, b, discriminante)
        print(f"La ecuación tiene dos raíces {r1:.5f} y {r2:.5f}")
    elif discriminante == 0:
        r = Raiz1(a, b, discriminante)
        print(f"La ecuación tiene una raíz {r:.0f}")
    else:
        print("La ecuación no tiene raíces reales")

# Proceso para ingresar varios valores de a, b y c
for _ in range(3):
    entrada = input("Ingrese a, b, c: ").split()
    a, b, c = map(float, entrada)
    resolverEcuacionCuadratica(a, b, c)