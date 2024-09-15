nimet=set()
nimi=input("anna nimi")

while nimi != (""):
    if nimi not in nimet:
        nimet.add(nimi)
        print("uusi nimi")
    nimi = input("anna nimi")
    if nimi in nimet:
        print("aiemmin syötetty nimi")

if nimi== (""):
    for nimi in nimet:
        print(nimi)


