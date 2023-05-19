import time
import os
def counting_sort(arr):
    max_val = max(arr)
    m = max_val + 1
    count = [0] * m
    for a in arr:
        count[a] += 1
    i = 0
    for a in range(m):
        for c in range(count[a]):
            arr[i] = a
            i += 1
cantidades = [100, 500, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]
z = []
for v in cantidades:
    with open(f'C:\\ADA\\todo\\{v}.txt', 'r') as f:
        lista_numeros = [int(numero) for numero in f.read().split()]
    ini = time.time()
    counting_sort(lista_numeros)
    fin = time.time()
    b = fin - ini
    z.append(b)
    print(b)
d = os.path.abspath(os.path.dirname(__file__))
t = os.path.join(d,"tiempos_countingpy.txt")
with open(t, "w") as f:
    for i in z:
        f.write(str(i) + " ")
print("Fin")
