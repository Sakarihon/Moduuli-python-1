icao_koodit={"EFET":"Enontekiö",
             "EFHK":"Helsinki-Vantaa",
             "EFIV":"Ivalo",
             "EFJO":"Joensuu",
             "EFKI":"Kajaani"}
teko=input("Haluatko syötää uuden lentoaseman? Haluatko syötää jo olemassa olevan lentoaseman? vai haluatko lopettaa?")

while teko!="lopeta":
    if teko=="uusi lentoasema":
        icao=input("icao koodi?")
        nimi=input("lentoaseman nimi?")
        icao_koodit[icao]=nimi
    teko = input(
        "Haluatko syötää uuden lentoaseman? Haluatko syötää jo olemassa olevan lentoaseman? vai haluatko lopettaa?")
    if teko=="olemassa oleva":
        ICAO=input("mikä Icao")
        print(icao_koodit[icao])
if teko=="lopeta":
    print("")


