import random
import os
cantidades = [100, 500, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 
            8000, 9000, 10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]
for x in cantidades:
    d = os.path.abspath(os.path.dirname(__file__))
    t = os.path.join(d, f"{x}.txt")
    with open(t, "w") as f:
        for i in range(x):
            num = random.randint(0,99) 
            f.write(str(num)+" ") 
