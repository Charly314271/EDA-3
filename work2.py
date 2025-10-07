import time
import random
import timeit
import math

# --- Funciones Auxiliares del ejercicio anterior ---

def contar_con_sleep(n):
    """Cuenta de 1 a N con un retraso de 1 segundo entre cada número."""
    print(f"\n--- 1. Iniciando cuenta regresiva de {n} segundos (No medido con timeit) ---")
    for i in range(1, n + 1):
        print(f"Segundo: {i}")
        time.sleep(1)
    print("--- ¡Cuenta terminada! ---\n")
    return n

def crear_lista_enteros(n=100):
    """Crea una lista de N números enteros aleatorios."""
    return [random.randint(1, 1000) for _ in range(n)]

def crear_lista_mixta(n=100):
    """Crea una lista de N elementos con enteros y floats aleatorios."""
    lista_mixta = []
    # Creamos 50 enteros y 50 floats (para un total de 100)
    for _ in range(n // 2): 
        lista_mixta.append(random.randint(1, 1000))
        lista_mixta.append(random.uniform(0.01, 1000.00))
    return lista_mixta[:n] # Asegura exactamente N elementos

def sumar_lista(lista):
    """Función simple que solo realiza la suma (para que timeit la mida)."""
    return sum(lista)

def realizar_multiplicaciones(n):
    """Multiplica el valor de N (input) por 50, 100 y 1000."""
    print(f"\n--- 4. Multiplicaciones usando el 'input' (N={n}) ---")
    resultado_50 = n * 50
    resultado_100 = n * 100
    resultado_1000 = n * 1000
    
    print(f"{n} * 50 = {resultado_50}")
    print(f"{n} * 100 = {resultado_100}")
    print(f"{n} * 1000 = {resultado_1000}")
    print("--------------------------------------------------")

# --- Ejecución y Medición con timeit ---
N_SEGUNDOS = 5 # Reducimos N para no esperar tanto
N_ELEMENTOS = 100
N_REPETICIONES = 10000 # Número de veces que timeit ejecutará la suma

# 1. Conteo de tiempo (usando time.sleep)
n_final = contar_con_sleep(N_SEGUNDOS) 

# --- Preparar Listas para timeit ---
lista_enteros = crear_lista_enteros(N_ELEMENTOS)
lista_mixta = crear_lista_mixta(N_ELEMENTOS)

##
---
## 2. Medición de la Suma de 100 Enteros

# Usamos setup para importar la función y definir la lista en el entorno de timeit
SETUP_ENTEROS = f"""
from __main__ import sumar_lista
lista_enteros = {lista_enteros} 
"""
# Comando a medir
COMMAND_ENTEROS = "sumar_lista(lista_enteros)"

# Medir el tiempo total para N_REPETICIONES
tiempo_total_enteros = timeit.timeit(
    stmt=COMMAND_ENTEROS, 
    setup=SETUP_ENTEROS, 
    number=N_REPETICIONES
)

# Calcular el tiempo promedio por ejecución
tiempo_promedio_enteros = tiempo_total_enteros / N_REPETICIONES

print(f"--- 2. Suma de 100 Enteros (Medido con timeit) ---")
print(f"Suma calculada (una vez): {sum(lista_enteros)}")
print(f"Tiempo total para {N_REPETICIONES} ejecuciones: {tiempo_total_enteros:.6f} segundos")
print(f"Tiempo promedio por ejecución: {tiempo_promedio_enteros * 1e6:.3f} microsegundos (µs)\n")

##
---
## 3. Medición de la Suma de 100 Mixtos (Enteros y Floats)

SETUP_MIXTOS = f"""
from __main__ import sumar_lista
lista_mixta = {lista_mixta}
"""
COMMAND_MIXTOS = "sumar_lista(lista_mixta)"

tiempo_total_mixtos = timeit.timeit(
    stmt=COMMAND_MIXTOS, 
    setup=SETUP_MIXTOS, 
    number=N_REPETICIONES
)

tiempo_promedio_mixtos = tiempo_total_mixtos / N_REPETICIONES

print(f"--- 3. Suma de 100 Mixtos (Medido con timeit) ---")
print(f"Suma calculada (una vez): {sum(lista_mixta):.2f}")
print(f"Tiempo total para {N_REPETICIONES} ejecuciones: {tiempo_total_mixtos:.6f} segundos")
print(f"Tiempo promedio por ejecución: {tiempo_promedio_mixtos * 1e6:.3f} microsegundos (µs)\n")

##
---
## 4. Multiplicaciones

# Multiplicaciones del input (N=5)
realizar_multiplicaciones(n_final)