import random
kokonaislukuja=[]
määrä=random.randint(1,10000000)
maksimi=random.randint(1,10000000)
for i in range(1,määrä):
    kokonaisluku=random.randint(1,maksimi)
    kokonaislukuja.append(kokonaisluku)

def summataan(kokonaislukuja):
    sum = 0
    for i in kokonaislukuja:
        sum += i
    return sum
print(summataan(kokonaislukuja))

