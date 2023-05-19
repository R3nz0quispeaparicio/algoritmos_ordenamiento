import os
import time
from heapq import heappush, heappop
cantidades = [100, 500, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]
z = []
def heap_sort(lista):
    n = len(lista)
    heap = []
    for i in range(n):
        heappush(heap, lista[i])
    ordered = []
    for i in range(n):
        ordered.append(heappop(heap))
    return ordered
for v in cantidades:
    ini = time.time()
    with open(f'C:\\ADA\\todo\\{v}.txt', 'r') as f:
        lista_numeros = [int(numero) for numero in f.read().split()]
    ordenada = heap_sort(lista_numeros)
    fin = time.time()
    tiempo = fin - ini
    z.append(tiempo)
    print(tiempo)
d = os.path.abspath(os.path.dirname(__file__))
t = os.path.join(d, "tiempos_heappy.txt")
with open(t, "w") as f:
    for i in z:
        f.write(str(i) + " ")
print("Fin")