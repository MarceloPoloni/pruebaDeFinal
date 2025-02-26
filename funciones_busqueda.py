
import os

def mostrar_menu():
    print("Menú de opciones:")
    print("1 - Cargar archivo y transformar en matriz 10x20")
    print("2 - Buscar palabras y mostrar modo")
    print("3 - Contar cantidad de palabras horizontales y verticales")
    print("4 - Analizar palabra con más y menos caracteres")
    print("5 - Salir")

def get_path_actual(nombre_archivo):
    return os.path.join(os.path.dirname(__file__), nombre_archivo)

def cargar_archivo():
    ruta_archivo = get_path_actual("data_final.csv")
    
    matriz = []
    try:
        with open(ruta_archivo, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                fila = linea.strip().split(";")
                matriz.append(fila)
        
        if len(matriz) != 10 or any(len(fila) != 20 for fila in matriz):
            print("Error: la matriz no tiene el tamaño correcto (10x20).")
            return None
        
        print("Archivo cargado correctamente.")
        return matriz
    except FileNotFoundError:
        print("Error: archivo no encontrado.")
    except Exception as e:
        print(f"Error al cargar el archivo: {e}")
    return None

def buscar_palabras(matriz):
    palabras_buscadas = ["LENGUAJE", "PYTHON", "PROGRAMACION", "UTNFRA"]
    palabras_encontradas = []
    
    # Buscar en horizontal
    for fila in matriz:
        fila_str = "".join(fila)
        for palabra in palabras_buscadas:
            if palabra in fila_str:
                palabras_encontradas.append((palabra, "Horizontal"))
    
    # Buscar en vertical
    for col in range(len(matriz[0])):
        columna_str = "".join(matriz[fila][col] for fila in range(len(matriz)))
        for palabra in palabras_buscadas:
            if palabra in columna_str:
                palabras_encontradas.append((palabra, "Vertical"))
    
    return palabras_encontradas

def contar_palabras(palabras_encontradas):
    horizontal = sum(1 for _, modo in palabras_encontradas if modo == "Horizontal")
    vertical = sum(1 for _, modo in palabras_encontradas if modo == "Vertical")
    print(f"Horizontal | {horizontal}")
    print(f"Vertical | {vertical}")

def analizar_palabras(palabras_encontradas):
    if not palabras_encontradas:
        print("No hay palabras para analizar.")
        return
    
    palabra_max = max(palabras_encontradas, key=lambda x: len(x[0]))[0]
    palabra_min = min(palabras_encontradas, key=lambda x: len(x[0]))[0]
    
    vocales = "AEIOU"
    cant_vocales = sum(1 for c in palabra_max if c in vocales)
    cant_consonantes = sum(1 for c in palabra_min if c not in vocales)
    
    print(f"Palabra con más caracteres: {palabra_max} - Vocales: {cant_vocales}")
    print(f"Palabra con menos caracteres: {palabra_min} - Consonantes: {cant_consonantes}")
