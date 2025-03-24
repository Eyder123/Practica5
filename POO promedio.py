import math

class Estadisticas:
    def __init__(self, valores):
        self.valores = valores

    def promedio(self):
        return sum(self.valores) / len(self.valores)

    def desviacion(self):
        prom = self.promedio()
        n = len(self.valores)
        suma = sum((x - prom) ** 2 for x in self.valores)
        return math.sqrt(suma / (n - 1))

# Entrada de datos
valores = list(map(float, input("Ingrese 10 números separados por espacio: ").split()))

# Cálculo y salida
estadistica = Estadisticas(valores)
print(f"El promedio es {estadistica.promedio():.2f}")
print(f"La desviación estandar es {estadistica.desviacion():.5f}")
