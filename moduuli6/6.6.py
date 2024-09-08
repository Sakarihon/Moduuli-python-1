import math

def euroaperneliömetri(säde, euros):
    pinta_ala=(säde/100/2)**2*math.pi
    euroapm2=euros/pinta_ala

    return euroapm2
halkaisija=float(input("mikä on pyöreän pitsan halkaisija sentteinä?"))
eurot=float(input("mikä on pitsan hinta?"))
halkaisija2=float(input("mikä on toisen pyöreän pitsan halkaisija sentteinä?"))
eurot2=float(input("mikä on toisen pitsan hinta?"))
pizza1=euroaperneliömetri(halkaisija, eurot)
pizza2=euroaperneliömetri(halkaisija2, eurot2)

if pizza1 > pizza2:
    print(f"Toisella pizzalla on enemmän vastinetta rahalle, koska se on {pizza2:.2f} euroa per neliömetri kun taas ensimmäinen on {pizza1:.2f} euroa per neliömetri.")
elif pizza2==pizza1:
    print("Yhtäpaljon vastinetta rahalle")

else:
    print(f"Ensimmäisellä pizzalla on enemmän vastinetta rahalle, koska se on {pizza1:.2f}euroa per neliömetri kun taas toinen on {pizza2:.2f} euroa per neliömetri.")


