from operator import truediv

luvut=[]
luku=input("anna numero")

while luku!="":
    luku = float(luku)
    luvut.append(luku)
    luku=input("anna numero")


käännetyt=sorted(luvut, reverse=True)

print(käännetyt[:5])