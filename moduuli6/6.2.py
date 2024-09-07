import random
tahkojen_määrä=int(input("Mikä on nopan maksimi silmäluku?"))
def noppa():
    for i in range(1,tahkojen_määrä):
        noppaheitto=random.randint(1,tahkojen_määrä)
    return noppaheitto
noppa_tulos =0
while noppa_tulos<tahkojen_määrä:
    noppa_tulos = noppa()
    print("nopan tahkojen määrä",noppa_tulos)