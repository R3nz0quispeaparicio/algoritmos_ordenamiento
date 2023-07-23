import time
import os
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

cantidades = [100, 500, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]
z=[]
for v in cantidades:
    with open(f'C:\\ADA\\todo\\{v}.txt', 'r') as f:
        lista_numeros = [int(numero) for numero in f.read().split()]
    ini = time.time()
    merge_sort(lista_numeros)
    fin = time.time()
    b = fin - ini
    z.append(b)
    print(b)
d = os.path.abspath(os.path.dirname(__file__))
t = os.path.join(d,"tiempos_mergepy.txt")
with open(t, "w") as f:
    for i in z:
        f.write(str(i) + " ")
print("Fin")
