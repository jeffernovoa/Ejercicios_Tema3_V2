def hanoi(n, origen, destino, auxiliar, movimientos):
    if n == 1:
        movimientos.append(f"Mover piedra de {origen} a {destino}")
        return
    hanoi(n - 1, origen, auxiliar, destino, movimientos)
    movimientos.append(f"Mover piedra de {origen} a {destino}")
    hanoi(n - 1, auxiliar, destino, origen, movimientos)

def resolver_piramide():
    print("Resolviendo el Puzzle de la Pirámide de Piedras Preciosas...")
    
    # Validar entrada del usuario
    while True:
        respuesta = input("¿Desea ver todos los movimientos? (sí/no): ").strip().lower()
        if respuesta in ['sí', 'si', 'no']:
            mostrar_todos = respuesta in ['sí', 'si']
            break
        else:
            print("Por favor, responda con 'sí' o 'no'.")
    
    movimientos = []
    hanoi(10, 'A', 'C', 'B', movimientos)
    
    # Determinar cuántos movimientos mostrar
    movimientos_a_mostrar = movimientos if mostrar_todos else movimientos[-100:]
    for movimiento in movimientos_a_mostrar:
        print(movimiento)
