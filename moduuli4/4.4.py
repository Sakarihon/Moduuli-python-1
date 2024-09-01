import random
randomi=random.randint(1,10)
luku=input("arvaa numero 1-10?")

while luku:
    if float(randomi)==float(luku):
        print("oikein")
        break
    elif float(randomi) < float(luku):
        print("liian suuri arvaus!")
    elif float(randomi) > float(luku):
        print("liian pieni arvaus!")
    luku = input("arvaa numero 1-10?")