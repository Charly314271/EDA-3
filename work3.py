from memory_profiler import profile

@profile
def crear_lista(n):
    return [i for i in range(n)]

@profile
def generador(n):
    for i in range(n):
        yield i

def main():
    n = 1000000

    lista = crear_lista(n)
    print(f"Lista creada con {len(lista)} elementos.")

    gen = generador(n)
    print("Primeros 10 elementos del generador:", [next(gen) for _ in range(10)])

if _name_ == "_main_":
    main()