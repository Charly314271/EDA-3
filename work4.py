import tracemalloc

def crear_lista(n):
    return [i for i in range(n)]

def generador(n):
    for i in range(n):
        yield i

def medir_memoria(func, *args, **kwargs):
    tracemalloc.start()
    resultado = func(*args, **kwargs)
    memoria_actual, memoria_max = tracemalloc.get_traced_memory()
    print(f"{func._name_} -> Memoria usada: {memoria_actual / (1024*3):.6f} GiB; Pico: {memoria_max / (1024*3):.6f} GiB")
    tracemalloc.stop()
    return resultado

def main():
    n = 1000000

    lista = medir_memoria(crear_lista, n)
    print(f"Lista creada con {len(lista)} elementos.")

    gen = medir_memoria(generador, n)
    print("Primeros 10 elementos del generador:", [next(gen) for _ in range(10)])

if _name_ == "_main_":
    main()