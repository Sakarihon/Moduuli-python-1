import math
kuha=input("mikä on kuhan pituus sentteinä?")
kuha=float(kuha)
if(kuha<37):
    x=37-kuha
    print(f"kuha on {x} cm alimittainen laske takaisin järveen")
else:
    print("hyvä!")