talvella=(12,1,2)
keväällä=(3,4,5)
kesällä=(6,7,8)
syksyllä=(9,10,11)
vuodenajat=(1,2,3,4,5,6,7,8,9,10,11,12)

kuu=int(input("Mikä on kuukauden numero?"))


if kuu not in vuodenajat:
    print("ei ole kuukauden numero")

if kuu in kesällä:
    print("kesä")
if kuu in syksyllä:
    print("syksy")
if kuu in talvella:
    print("talvi")
if kuu in keväällä:
    print("kevät")
