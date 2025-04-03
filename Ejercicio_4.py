class Polinomio:
    def __init__(self, coeficientes):
        self.coeficientes = coeficientes  # Lista de coeficientes ordenados por grado descendente

    def __str__(self):
        return " + ".join(f"{coef}x^{i}" if i > 0 else str(coef) for i, coef in enumerate(self.coeficientes[::-1]))

    def restar(self, otro):
        max_len = max(len(self.coeficientes), len(otro.coeficientes))
        coef1 = [0] * (max_len - len(self.coeficientes)) + self.coeficientes
        coef2 = [0] * (max_len - len(otro.coeficientes)) + otro.coeficientes
        return Polinomio([a - b for a, b in zip(coef1, coef2)])

    def dividir(self, otro):
        if len(otro.coeficientes) == 0 or otro.coeficientes == [0]:
            return "División no válida"
        resultado = []
        dividendo = self.coeficientes[:]
        while len(dividendo) >= len(otro.coeficientes):
            coeficiente = dividendo[0] / otro.coeficientes[0]
            resultado.append(coeficiente)
            resta = [coeficiente * b for b in otro.coeficientes] + [0] * (len(dividendo) - len(otro.coeficientes))
            dividendo = [a - b for a, b in zip(dividendo, resta)]
            dividendo.pop(0)  # Eliminar el término más alto (ya procesado)
        return Polinomio(resultado)

    def eliminar_termino(self, grado):
        if 0 <= grado < len(self.coeficientes):
            self.coeficientes[-(grado + 1)] = 0  # Ajustar índice para grado descendente

    def existe_termino(self, grado):
        if 0 <= grado < len(self.coeficientes):
            return self.coeficientes[-(grado + 1)] != 0
        return False

def resolver_encantamientos():
    p1 = Polinomio([1, 0, 2, 1])  # Representa x^3 + 2x + 1
    p2 = Polinomio([1, 1])  # Representa x + 1
    
    print("Resta de polinomios:", p1.restar(p2))
    print("División de polinomios:", p1.dividir(p2))
    p1.eliminar_termino(1)
    print("Polinomio después de eliminar término x:", p1)
    print("¿Existe término x^1 en p1?:", p1.existe_termino(1))