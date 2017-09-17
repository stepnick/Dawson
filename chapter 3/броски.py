import random 
resh = 0
orel = 0
k = 0
while k != 100:
    k += 1 
    bros = random.randint(1, 2)
    if bros == 1 :
        resh += 1
    if bros == 2 :
        orel += 1
print("Орел выпал", orel,"раз")
print("Решка выпала", resh,"раз")
