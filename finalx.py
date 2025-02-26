
from funciones_busqueda import *
import os

def main():
    matriz = None
    palabras_encontradas = []
    
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            matriz = cargar_archivo()
            palabras_encontradas = []
            input("Presione Enter para continuar.")
        
        elif opcion == "2":
            if matriz is None:
                print("Error: No se ha cargado la matriz. Use la opción 1.")
            else:
                palabras_encontradas = buscar_palabras(matriz)
                for palabra, modo in palabras_encontradas:
                    print(f"{palabra} | {modo}")
            input("Presione Enter para continuar.")
        
        elif opcion == "3":
            if not palabras_encontradas:
                print("No se encontraron palabras. Use la opción 2.")
            else:
                contar_palabras(palabras_encontradas)
            input("Presione Enter para continuar.")
        
        elif opcion == "4":
            if not palabras_encontradas:
                print("No se encontraron palabras. Use la opción 2.")
            else:
                analizar_palabras(palabras_encontradas)
            input("Presione Enter para continuar.")
        
        elif opcion == "5":
            print("Saliendo...")
            break
        
        else:
            print("Opción no válida.")
            input("Presione Enter para continuar.")

if __name__ == "__main__":
    main()