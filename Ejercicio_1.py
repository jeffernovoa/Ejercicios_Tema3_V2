def hanoi(n, origen, destino, auxiliar, movimientos):
    if n == 1:
        movimientos.append(f"Mover piedra de {origen} a {destino}")
        return
    hanoi(n - 1, origen, auxiliar, destino, movimientos)
    movimientos.append(f"Mover piedra de {origen} a {destino}")
    hanoi(n - 1, auxiliar, destino, origen, movimientos)

def resolver_piramide():
    print("Resolviendo el Puzzle de la Pirámide de Piedras Preciosas...")
    mostrar_todos = input("¿Desea ver todos los movimientos? (s/n): ").strip().lower() == 's'
    movimientos = []
    hanoi(74, 'A', 'C', 'B', movimientos)
    
    # Determinar cuántos movimientos mostrar
    movimientos_a_mostrar = movimientos if mostrar_todos else movimientos[-100:]
    for movimiento in movimientos_a_mostrar:
        print(movimiento)
