galloona_määrä=float(input("Montako galloonaa?"))
def litroiksi():
    litra=galloona_määrä*3.785
    return litra
määrä=0
while galloona_määrä>0:
    määrä=litroiksi()
    print ("se on",määrä,"litraa")
    galloona_määrä = float(input("Montako galloonaa?"))
    




