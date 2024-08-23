import math
eka=input("paljonko massa on leivisköinä?")
toka=input("paljon nauloina?")
kolmas=input("paljon luoteina?")
eka=float(eka)
toka=float(toka)
kolmas=float(kolmas)
luoti=13.3
naula=32*luoti
leiviskä=20*naula
kokonaismassagrammoina=(leiviskä*eka)+(naula*toka)+(kolmas*luoti)
kg=int(kokonaismassagrammoina/1000)
grammoina=kokonaismassagrammoina-kg*1000
#print(kokonaismassagrammoina)
#print(f"Kiloina {int(kg)}, grammoina {grammoina:.2f}")
print(f"kiloina, {kg} , grammoina,{grammoina:.2f}")