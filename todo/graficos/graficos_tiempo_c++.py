import matplotlib.pyplot as plt
with open("C:\\ADA\\todo\\tiempos_bubble_sort.txt", 'r') as f:
    tb = [float(numero) for numero in f.read().split()]
with open("C:\\ADA\\todo\\tiempos_counting_sort.txt", 'r') as f:
    tc = [float(numero) for numero in f.read().split()]
with open("C:\\ADA\\todo\\tiempos_heap_sort.txt", 'r') as f:
    th = [float(numero) for numero in f.read().split()]
with open("C:\\ADA\\todo\\tiempos_insertion_sort.txt", 'r') as f:
    ti = [float(numero) for numero in f.read().split()]
with open("C:\\ADA\\todo\\tiempos_merge_sort.txt", 'r') as f:
    tm = [float(numero) for numero in f.read().split()]
with open("C:\\ADA\\todo\\tiempos_quick_sort.txt", 'r') as f:
    tq = [float(numero) for numero in f.read().split()]
with open("C:\\ADA\\todo\\tiempos_selection_sort.txt", 'r') as f:
    ts = [float(numero) for numero in f.read().split()]


fig, ax = plt.subplots(figsize=(8, 6))


ax.plot(range(len(tb)),tb, label='Bubble sort')
ax.plot(range(len(tc)),tc, label='Counting sort')
ax.plot(range(len(th)),th, label='Heap sort')
ax.plot(range(len(ti)),ti, label='Insertion sort')
ax.plot(range(len(tm)),tm, label='Merge sort')
ax.plot(range(len(tq)),tq, label='Quick sort')
ax.plot(range(len(ts)),ts, label='Selection sort')

ax.set_xlabel('Datos a ordenar')
ax.set_ylabel('Tiempo de procesamiento (s)')
ax.set_title('Comparación de tiempos de procesamiento en C++')
ax.legend()
valores_y = [10,20,30,40,50,60,70,80,90,100]

plt.yticks(valores_y)
ax.set_xticks(range(len(tb)))
ax.set_xticklabels([str(x) for x in [100,500,1000,2000,3000,4000,5000,6000,7000,8000,9000,10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]])
ax.tick_params(axis='x', rotation=45)


plt.show()
plt.tight_layout()

fig.savefig('graficotodoC++.pdf', bbox_inches='tight', pad_inches=0.5, dpi=900)