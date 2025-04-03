from collections import namedtuple

Nave = namedtuple('Nave', ['nombre', 'longitud', 'tripulantes', 'pasajeros'])

def resolver_rally_espacial():
    naves = [
        Nave("Cometa Veloz", 30, 5, 20),
        Nave("Titán del Cosmos", 50, 10, 35),
        Nave("Estrella Fugaz", 20, 3, 10),
        Nave("GX-200", 40, 8, 50),
        Nave("GX-100", 25, 6, 60)
    ]
    
    # Ordenaciones
    naves_ordenadas_por_nombre = sorted(naves, key=lambda x: x.nombre, reverse=True)
    naves_ordenadas_por_longitud = sorted(naves, key=lambda x: x.longitud, reverse=True)
    cinco_mas_pasajeros = sorted(naves, key=lambda x: x.pasajeros, reverse=True)[:5]
    
    # Máximos y mínimos
    nave_mas_tripulantes = max(naves, key=lambda x: x.tripulantes)
    nave_mas_pequena = min(naves, key=lambda x: x.longitud)
    nave_mas_grande = max(naves, key=lambda x: x.longitud)
    
    # Filtros
    info_cometa_titan = [n for n in naves if n.nombre in ["Cometa Veloz", "Titán del Cosmos"]]
    naves_con_gx = [n for n in naves if n.nombre.startswith("GX")]
    naves_con_mas_seis_pasajeros = [n for n in naves if n.pasajeros >= 6]
    
    # Impresiones
    print("\n--- Naves ordenadas por nombre (ascendente) ---")
    for nave in naves_ordenadas_por_nombre:
        print(nave)
    
    print("\n--- Naves ordenadas por longitud (descendente) ---")
    for nave in naves_ordenadas_por_longitud:
        print(nave)
    
    print("\n--- Info de Cometa Veloz y Titán del Cosmos ---")
    for nave in info_cometa_titan:
        print(nave)
    
    print("\n--- Cinco naves con más pasajeros ---")
    for nave in cinco_mas_pasajeros:
        print(nave)
    
    print("\n--- Nave con más tripulantes ---")
    print(nave_mas_tripulantes)
    
    print("\n--- Naves cuyo nombre comienza con GX ---")
    for nave in naves_con_gx:
        print(nave)
    
    print("\n--- Naves con 6 o más pasajeros ---")
    for nave in naves_con_mas_seis_pasajeros:
        print(nave)
    
    print("\n--- Nave más pequeña ---")
    print(nave_mas_pequena)
    
    print("\n--- Nave más grande ---")
    print(nave_mas_grande)