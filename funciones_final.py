import os
import csv
def mostrar_menu():
    print("Menú de opciones:")
    print("1 - cargar archivo y transformar en matriz 10x10")
    print("2 - ingresar número y buscar secuencias")
    print("3 - mostrar cuántas secuencias suman el número ingresado")
    print("4 - mostrar la secuencia con la cantidad mínima de elementos")
    print("5 - mostrar la secuencia con la cantidad máxima de elementos")
    print("6 - salir")

def get_path_actual(nombre_archivo):
    return os.path.join(os.path.dirname(__file__), nombre_archivo)

def cargar_archivo():
    ruta_archivo = get_path_actual("data_final_20250219.csv")
    matriz = []

    try:
        with open(ruta_archivo, "r", encoding="utf-8") as archivo:
            lector_csv = csv.reader(archivo, delimiter=";")
            for fila in lector_csv:
                if len(fila) != 10:  # Verificar que cada fila tenga 10 elementos
                    print("Error: El archivo no tiene el formato correcto.")
                    return None
                matriz.append([int(valor) for valor in fila])

                if len(matriz) == 10:  # Solo leer 10 filas
                    break 

        if len(matriz) != 10:
            print("Error: El archivo no tiene 10 filas.")
            return None

        print("Archivo cargado correctamente.")
        return matriz

    except FileNotFoundError:
        print("Error: Archivo no encontrado.")
    except ValueError:
        print("Error: El archivo contiene valores no numéricos.")
    except Exception as e:
        print(f"Error al cargar el archivo: {e}")

    return None

def encontrar_secuencias_consecutivas(matriz, numero):
    secuencias = []

    for fila in matriz:
        for inicio in range(len(fila)):
            suma = 0
            secuencia = []
            for k in range(inicio, len(fila)):
                secuencia.append(fila[k])
                suma += fila[k]
                if suma == numero:
                    secuencias.append(secuencia[:])  # Guardar copia de la secuencia
                    break  # No permite dividir en varias secuencias más cortas
                elif suma > numero:
                    break  # Si la suma se pasa, no tiene sentido seguir sumando

    return secuencias

    
def secuencia_minima(secuencias):
    return min(secuencias, key=len) if secuencias else None

def secuencia_maxima(secuencias):
    return max(secuencias, key=len) if secuencias else None

