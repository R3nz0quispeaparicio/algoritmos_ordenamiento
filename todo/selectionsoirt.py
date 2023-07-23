import time
import os
cantidades = [100, 500, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]
z = []
for v in cantidades:
    with open(f'C:\\ADA\\todo\\{v}.txt', 'r') as f:
        lista_numeros = [int(numero) for numero in f.read().split()]
    def ordenar_selection(lista):
        n = len(lista)
        for i in range(n):
            minimo = i
            for j in range(i + 1, n):
                if lista[j] < lista[minimo]:
                    minimo = j
            lista[i], lista[minimo] = lista[minimo], lista[i]
    ini = time.time()
    ordenar_selection(lista_numeros)
    fin = time.time()
    b = fin - ini
    z.append(b)
    print(b)
d = os.path.abspath(os.path.dirname(__file__))
t = os.path.join(d,"tiempos_selectionpy.txt")
with open(t, "w") as f:
    for i in z:
        f.write(str(i) + " ")
print("Fin")
