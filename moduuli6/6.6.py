import math
halkaisija=float(input("mikä on pyöreän pitsan halkaisija?"))
eurot=float(input("mikä on pitsan hinta?"))
halkaisija2=float(input("mikä on toisen pyöreän pitsan halkaisija?"))
eurot2=float(input("mikä on toisen pitsan hinta?"))
def i(halkaisija, eurot):
    pinta_ala=(halkaisija/100/2)**2*math.pi
    jokin=eurot/pinta_ala
    pinta_ala2 = (halkaisija2 / 100 / 2) ** 2 * math.pi
    jokin2 = eurot2 / pinta_ala2
    return jokin and jokin2
print(i(halkaisija, eurot))

