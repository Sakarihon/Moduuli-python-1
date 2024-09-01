number=float(input("anna luku"))
maxnumber=minnumber=number

while number:
    if float(number)> float(maxnumber):
        maxnumber=number
    elif float(number)<float(minnumber):
        minnumber=number
    number = input("anna luku")
    if not number:
        print(maxnumber, minnumber)
