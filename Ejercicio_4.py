class Polinomio:
    def __init__(self, coeficientes):
        self.coeficientes = coeficientes  # Lista de coeficientes ordenados por grado descendente

    def __str__(self):
        return " + ".join(
            f"{coef}x^{i}" if i > 0 else str(coef)
            for i, coef in enumerate(self.coeficientes[::-1]) if coef != 0
        )

    def restar(self, otro):
        max_len = max(len(self.coeficientes), len(otro.coeficientes))
        coef1 = [0] * (max_len - len(self.coeficientes)) + self.coeficientes
        coef2 = [0] * (max_len - len(otro.coeficientes)) + otro.coeficientes
        return Polinomio([a - b for a, b in zip(coef1, coef2)])

    def dividir(self, otro):
        if not otro.coeficientes or all(c == 0 for c in otro.coeficientes):
            raise ValueError("División no válida: el divisor no puede ser cero.")
        
        resultado = []
        dividendo = self.coeficientes[:]
        divisor_grado = len(otro.coeficientes) - 1

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
        return 0 <= grado < len(self.coeficientes) and self.coeficientes[-(grado + 1)] != 0

def resolver_encantamientos():
    p1 = Polinomio([1, 0, 2, 1])  # Representa x^3 + 2x + 1
    p2 = Polinomio([1, 1])  # Representa x + 1

    print("\nPolinomio 1:", p1)
    print("Polinomio 2:", p2)
    
    print("\nResta de polinomios:", p1.restar(p2))
    print("\nDivisión de polinomios:", p1.dividir(p2))
    p1.eliminar_termino(1)
    print("\nPolinomio después de eliminar término x:", p1)
    print("\n¿Existe término x^1 en p1?:", p1.existe_termino(1))