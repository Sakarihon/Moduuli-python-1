import random
def noppa():
    for i in range(1,6):
        noppaheitto=random.randint(1,6)
    return noppaheitto
noppa_tulos =0
while noppa_tulos<6:
    noppa_tulos = noppa()
    print(noppa_tulos)




