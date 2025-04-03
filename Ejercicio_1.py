def hanoi(n, origen, destino, auxiliar):
    if n == 1:
        print(f"Mover piedra de {origen} a {destino}")
        return
    hanoi(n - 1, origen, auxiliar, destino)
    print(f"Mover piedra de {origen} a {destino}")
    hanoi(n - 1, auxiliar, destino, origen)

def resolver_piramide():
    print("Resolviendo el Puzzle de la Pirámide de Piedras Preciosas...")
    hanoi(74, 'A', 'C', 'B')