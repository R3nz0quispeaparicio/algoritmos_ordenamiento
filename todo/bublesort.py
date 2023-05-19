import time
import os
cantidades = [100, 500, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]
z=[]
for v in cantidades:
    with open(f'C:\\ADA\\todo\\{v}.txt', 'r') as f:
        lista_numeros = [int(numero) for numero in f.read().split()]
    def ordenar_burbuja(lista):
        n = len(lista)
        for i in range(n):
            for j in range(0, n-i-1):
                if lista[j] > lista[j+1]:
                    lista[j], lista[j+1] = lista[j+1], lista[j] 
    ini=time.time()
    ordenar_burbuja(lista_numeros)
    fin=time.time()
    b=fin-ini
    z.append(b)
    print(b)
d = os.path.abspath(os.path.dirname(__file__))
t = os.path.join(d,"tiempos_bubblepy.txt")
with open(t, "w") as f:
    for tiempo in z:
        f.write(str(tiempo) + " ")
print("Fin")
