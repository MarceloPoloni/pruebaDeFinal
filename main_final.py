from funciones_final import *
import os

def main():
    matriz = None
    numero_ingresado = None
    secuencias = []
    
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        mostrar_menu()
        opcion = input("seleccione una opción: ").strip()

        if opcion == "1":
            matriz = cargar_archivo()
            secuencias = []
            input("presione Enter para continuar.")
            
        elif opcion == "2":
            if matriz is None:
                print("error no se cargo la matriz. Use la opción 1.")
            else:
                while True:
                    try:
                        numero_ingresado = int(input("ingrese un número de 2 dígito: ").strip())
                        if 1 <= numero_ingresado <= 99:
                            break 
                        else:
                            print("error el número debe estar entre 1 y 99.")
                    except ValueError:
                        print("error ingrese un número válido.")
                
                secuencias = encontrar_secuencias_consecutivas(matriz, numero_ingresado)
                print("secuencias encontradas:", secuencias if secuencias else "ninguna secuencia encontrada.")
            input("presione Enter para continuar.")

        elif opcion == "3":
            if matriz is None or numero_ingresado is None:
                print("error Primero debe cargar el archivo y buscar un número.")
            elif not secuencias:
                print("no se han encontrado secuencias para el número ingresado.")
            else:
                print(f"se encontraron {len(secuencias)} secuencias cuya suma es {numero_ingresado}.")
            input("presione Enter para continuar.")

        elif opcion == "4":
            if not secuencias:
                print("no se encontraron secuencias. ingrese un número en la opción 2.")
            else:
                sec_min = secuencia_minima(secuencias)
                print(f"\nsecuencia con la cantidad mínima de elementos: {sec_min}")
            input("presione Enter para continuar.")

        elif opcion == "5":
            if not secuencias:
                print("no se encontraron secuencias. ingrese un número en la opción 2.")
            else:
                sec_max = secuencia_maxima(secuencias)
                print(f"secuencia con la cantidad máxima de elementos: {sec_max}")
            input("presione Enter para continuar.")

        elif opcion == "6":
            print("saliendo")
            break

        else:
            print("opción no válida.")
            input("presione Enter para continuar.")

if __name__ == "__main__":
    main()
