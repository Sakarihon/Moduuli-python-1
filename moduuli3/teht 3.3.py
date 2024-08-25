sukupuoli=input("mikä on biologinen sukupuolesi?")
arvo=input("hemoglobiini arvo?")
arvo=float(arvo)
if sukupuoli=="nainen" and arvo<=175 and arvo >=113:
     print("normaali")
elif sukupuoli=="nainen" and arvo>175:
     print("korkea")
elif sukupuoli == "nainen" and arvo < 113:
     print("alhainen")
elif sukupuoli=="mies" and arvo<=195 and arvo >=134:
     print("normaali")
elif sukupuoli == "mies" and arvo > 195:
     print("korkea")
elif sukupuoli == "mies" and arvo < 134:
    print("alhainen")
