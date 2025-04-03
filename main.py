from Ejercicio_1 import resolver_piramide
from Ejercicio_2 import resolver_cifra_magica
from Ejercicio_3 import resolver_rally_espacial
from Ejercicio_4 import resolver_encantamientos

if __name__ == "__main__":
    while True:
        print("\nSeleccione un ejercicio para ejecutar:")
        print("1. Puzzle de la Pirámide de Piedras Preciosas")
        print("2. Secreto de la Cifra Mágica")
        print("3. Gran Rally Espacial")
        print("4. Matemática de los Encantamientos")
        print("5. Salir")
        
        opcion = input("Ingrese el número de la opción deseada: ")
        
        if opcion == "1":
            resolver_piramide()
        elif opcion == "2":
            resolver_cifra_magica()
        elif opcion == "3":
            resolver_rally_espacial()
        elif opcion == "4":
            resolver_encantamientos()
        elif opcion == "5":
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")