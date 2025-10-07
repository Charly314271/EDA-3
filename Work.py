import time
import random

# 1. Algoritmo de conteo con time.sleep(1)
def contar_con_sleep(n):
    """Cuenta de 1 a N con un retraso de 1 segundo entre cada número."""
    print(f"\n--- 1. Iniciando cuenta regresiva de {n} segundos... ---")
    for i in range(1, n + 1):
        print(f"Segundo: {i}")
        time.sleep(1)
    print("--- ¡Cuenta terminada! ---\n")
    return n # Devolvemos N para usarlo en la multiplicación

# 2. Sumar una lista de 100 enteros
def sumar_lista_enteros():
    """Crea y suma una lista de 100 números enteros aleatorios."""
    # Creamos una lista de 100 enteros aleatorios entre 1 y 1000
    lista_enteros = [random.randint(1, 1000) for _ in range(100)]
    suma_enteros = sum(lista_enteros)
    
    # print(f"Lista de 100 enteros (primeros 5): {lista_enteros[:5]}...") # Descomentar para ver la lista
    print(f"--- 2. Suma de la lista de 100 enteros: {suma_enteros} ---\n")
    return suma_enteros

# 3. Sumar una lista de 100 elementos que contiene enteros y floats
def sumar_lista_mixta():
    """Crea y suma una lista de 100 elementos que contiene enteros y floats aleatorios."""
    # Creamos una lista de 100 elementos: 50 enteros y 50 floats
    lista_mixta = []
    for _ in range(50):
        lista_mixta.append(random.randint(1, 1000))        # Entero
        lista_mixta.append(random.uniform(0.01, 1000.00))  # Float

    # Nos aseguramos que sean 100 elementos, aunque el método de arriba garantiza 100 (50+50)
    lista_mixta = lista_mixta[:100]
    
    suma_mixta = sum(lista_mixta)
    
    # print(f"Lista mixta de 100 elementos (primeros 5): {lista_mixta[:5]}...") # Descomentar para ver la lista
    print(f"--- 3. Suma de la lista mixta (enteros y floats): {suma_mixta:.2f} ---\n")
    return suma_mixta

# 4. Multiplicaciones del input (N=10)
def realizar_multiplicaciones(n):
    """Multiplica el valor de N (input) por 50, 100 y 1000."""
    print(f"--- 4. Multiplicaciones usando el 'input' (N={n}) ---")
    
    resultado_50 = n * 50
    resultado_100 = n * 100
    resultado_1000 = n * 1000
    
    print(f"{n} * 50 = {resultado_50}")
    print(f"{n} * 100 = {resultado_100}")
    print(f"{n} * 1000 = {resultado_1000}")
    print("--------------------------------------------------")


# --- Ejecución del Algoritmo ---
N = 10 # El número de segundos para el conteo

# Ejecutar las funciones
n_final = contar_con_sleep(N) # 1. Conteo de tiempo
suma_enteros = sumar_lista_enteros() # 2. Suma de enteros
suma_mixta = sumar_lista_mixta() # 3. Suma de mixtos

# 4. Multiplicaciones
realizar_multiplicaciones(n_final)