import random
pisteet=float(input("montako pistettä?"))
N=pisteet
määrä=pisteet
n=0

while määrä>0:
    x=random.uniform(0,1)
    y=random.uniform(0,1)
    if x**2+y**2<1:
        n+=1
    määrä-=1

pii=4*float(n)/N
print("piin likiarvo on",pii)

