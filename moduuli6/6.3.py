galloona_määrä=float(input("Montako galloonaa?"))
def nii():
    litra=galloona_määrä*3.785
    return litra
määrä=0
while galloona_määrä>0:
    määrä=nii()
    print ("se on",määrä,"litraa")
    galloona_määrä = float(input("Montako galloonaa?"))
    




