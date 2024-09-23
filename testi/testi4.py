import random
own_makkaras=[]
secret_black_sausage=[1,2,3,4,5]
own_secret_black_sausage=[]
amount=0

def secret_black_sausage_chance(amount):
    secret_black_sausage_piece = int(random.randint(0, 5))
    if secret_black_sausage_piece==(1 or 2 or 3 or 4 or 5):
        amount+=1
        own_secret_black_sausage.append(amount)
        if own_secret_black_sausage==secret_black_sausage:
            own_makkaras.append("secret_black_sausage")
            got_black=print("Onnittelut löysit palan secret_black_sausagen!")
            return got_black
        #return
    #return
while own_secret_black_sausage!=secret_black_sausage:
    secret_black_sausage_chance(amount)
print(secret_black_sausage_chance(amount))
print("mustamakkara1")