import time
import os
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

cantidades = [100, 500, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]
z = []
for v in cantidades:
    with open(f'C:\\ADA\\todo\\{v}.txt', 'r') as f:
        lista_numeros = [int(numero) for numero in f.read().split()]
    ini = time.time()
    insertion_sort(lista_numeros)
    fin = time.time()
    b = fin - ini
    z.append(b)
    print(b)
d = os.path.abspath(os.path.dirname(__file__))
t = os.path.join(d,"tiempos_insertionpy.txt")
with open(t, "w") as f:
    for i in z:
        f.write(str(i) + " ")
print("Fin")
