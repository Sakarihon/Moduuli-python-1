tunnus=input("käyttäjätunnus?")
salasana=input("salasana?")
kerrat=0
while kerrat<5:


    if tunnus=="python" and salasana=="rules":
        print("tervetuloa")
        break
    elif tunnus!="python" or salasana!="rules":
        print("pääsy evätty")
        kerrat+=1
    if float(kerrat)<5:
        tunnus = input("käyttäjätunnus?")
        salasana= input("salasana?")
    else:
        break