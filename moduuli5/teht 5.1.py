import random
numerot=[]
määrä=int(input("arpakuutioiden lukumäärä"))
for i in range(1,määrä):
    randomi=random.randint(1,6)
    numerot.append(randomi)
    määrä-=1
summa=sum(numerot)
print('arpakuutioiden silmälukujen summa',summa)
