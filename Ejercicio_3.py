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
    naves_ordenadas_por_nombre = sorted(naves, key=lambda x: x.nombre)
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
    print("Naves ordenadas por nombre:", naves_ordenadas_por_nombre)
    print("Naves ordenadas por longitud descendente:", naves_ordenadas_por_longitud)
    print("Info de Cometa Veloz y Titán del Cosmos:", info_cometa_titan)
    print("Cinco naves con más pasajeros:", cinco_mas_pasajeros)
    print("Nave con más tripulantes:", nave_mas_tripulantes)
    print("Naves cuyo nombre comienza con GX:", naves_con_gx)
    print("Naves con 6 o más pasajeros:", naves_con_mas_seis_pasajeros)
    print("Nave más pequeña:", nave_mas_pequena)
    print("Nave más grande:", nave_mas_grande)