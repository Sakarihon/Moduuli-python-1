import random
numerot=[]
määrä=float(input("arpakuutioiden lukumäärä"))
while määrä>0:
    randomi=random.randint(1,6)
    numerot.append(randomi)
    määrä-=1
summa=sum(numerot)
print('summa',summa)
