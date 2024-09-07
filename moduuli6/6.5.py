import random
kokonaislukuja=[]
parilliset=[]
määrä=random.randint(1,100)
maksimi=random.randint(1,10000000)
for i in range(1,määrä):
    kokonaisluku=random.randint(1,maksimi)
    kokonaislukuja.append(kokonaisluku)

def joo(kokonaislukuja):
    for i in kokonaislukuja:
        jokin = 0
        if i%2==0:
            jokin+=i
            parilliset.append(jokin)
    return parilliset
print("parillisia kokonaislukuja", joo(kokonaislukuja))
print("kaikki",kokonaislukuja)