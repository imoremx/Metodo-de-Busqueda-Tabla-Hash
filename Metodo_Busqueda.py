import time

# --- Configuración ---
ARCHIVO_ENTRADA = "Datos.txt"
ARCHIVO_ORDENADO = "datos_ordenados.txt"
TAMANIO_TABLA = 5000  # Cubetas disponibles

def cargar_y_ordenar():
    try:
        with open(ARCHIVO_ENTRADA, "r") as f:
            # Convertir cada línea en entero
            numeros = [int(linea.strip()) for linea in f if linea.strip()]
        
        print(f"--- Datos cargados: {len(numeros)} números ---")
        
        # Ordenar los números
        numeros.sort()
        
        # Guardar en datos_ordenados.txt
        with open(ARCHIVO_ORDENADO, "w") as f_ord:
            for n in numeros:
                f_ord.write(f"{n}\n")
        
        print(f"--- Datos ordenados guardados en {ARCHIVO_ORDENADO} ---")
        return numeros
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {ARCHIVO_ENTRADA}")
        return []

def construir_tabla_hash(lista_numeros):
    # Crear tabla con sublistas vacías (Encadenamiento)
    tabla = [[] for _ in range(TAMANIO_TABLA)]
    
    for num in lista_numeros:
        # Función Hash: clave = numero % tamanio
        posicion = num % TAMANIO_TABLA
        tabla[posicion].append(num)
    
    print(f"--- Tabla Hash construida con {TAMANIO_TABLA} cubetas ---")
    return tabla

def buscar_en_hash(tabla, numero_buscado):
    # 1. Aplicar función hash para saber en qué cubeta buscar
    posicion = numero_buscado % TAMANIO_TABLA
    cubeta = tabla[posicion]
    
    # 2. Iniciar medición de tiempo
    inicio = time.perf_counter()
    
    encontrado = False
    # 3. Buscar dentro de la cubeta (encadenamiento)
    if numero_buscado in cubeta:
        encontrado = True
    
    fin = time.perf_counter()
    
    # Calcular tiempo en milisegundos
    tiempo_ms = (fin - inicio) * 1000
    return encontrado, posicion, tiempo_ms

def main():
    # Paso 1 y 2: Leer y Ordenar
    datos = cargar_y_ordenar()
    if not datos:
        return

    # Paso 3: Construir Tabla
    tabla_hash = construir_tabla_hash(datos)

    while True:
        print("\n" + "="*30)
        try:
            opcion = input("Introduce el número a buscar (o 's' para salir): ")
            if opcion.lower() == 's':
                break
            
            numero = int(opcion)
            
            # Realizar búsqueda
            encontrado, pos, duracion = buscar_en_hash(tabla_hash, numero)
            
            # Desplegar resultados (basado en tu imagen)
            if encontrado:
                print(f"Resultado: El número {numero} SI se encuentra.")
            else:
                print(f"Resultado: El número {numero} NO se encuentra.")
                
            print(f"Posición (Cubeta): {pos}")
            print(f"Tiempo de búsqueda: {duracion:.6f} ms")
            
        except ValueError:
            print("Por favor, introduce un número entero válido.")

if __name__ == "__main__":
    main()