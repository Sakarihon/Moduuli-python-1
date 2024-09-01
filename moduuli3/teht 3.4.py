vuosiluku=float(input("kerro vuosiluku"))
if (vuosiluku%4==0):
    if (vuosiluku%100==0):
        if (vuosiluku%400==0):
            print("karkausvuosi")
        else:
             print("vuosi ei ole karkausvuosi")
    else:
         print("vuosi on karkausvuosi")
else:
     print("vuosi ei ole karkausvuosi")