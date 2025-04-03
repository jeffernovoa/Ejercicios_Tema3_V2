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
    
    naves_ordenadas_por_nombre = sorted(naves, key=lambda x: (x.nombre))
    print("Naves ordenadas por nombre:", naves_ordenadas_por_nombre)
    
    naves_ordenadas_por_longitud = sorted(naves, key=lambda x: x.longitud, reverse=True)
    print("Naves ordenadas por longitud descendente:", naves_ordenadas_por_longitud)
    
    print("Info de Cometa Veloz y Titán del Cosmos:", [n for n in naves if n.nombre in ["Cometa Veloz", "Titán del Cosmos"]])
    
    print("Cinco naves con más pasajeros:", sorted(naves, key=lambda x: x.pasajeros, reverse=True)[:5])
    
    print("Nave con más tripulantes:", max(naves, key=lambda x: x.tripulantes))
    
    print("Naves cuyo nombre comienza con GX:", [n for n in naves if n.nombre.startswith("GX")])
    
    print("Naves con 6 o más pasajeros:", [n for n in naves if n.pasajeros >= 6])
    
    print("Nave más pequeña:", min(naves, key=lambda x: x.longitud))
    print("Nave más grande:", max(naves, key=lambda x: x.longitud))