#kod zaka 01
#12.10.26
#program jede kulicka tam a zpet
import time
import math

pocet = int(input("Zadej pocet radku od 5 do 15: "))

print("kulička jede")

for i in range(pocet):
    print(" " * i + "0")
    time.sleep(0.1)

for i in range(pocet):
    print(" " * (pocet - i) + "0")
    time.sleep(0.1)

for i in range(1, pocet + 1):
    print(i, i * i, math.sqrt(i))





