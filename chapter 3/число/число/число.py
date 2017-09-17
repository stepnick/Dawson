import random
number = int(input("число"))

x = 2
y = 50

tries = 0
if y == number:
    tries = 1    

while y != number:
    if number > y :
        y = y + 50//x 
        x += 2
    else: 
        y = y - 50//x 
        x += 2
    print(y)
    tries += 1

print("Компьютер отгадал число с ", tries,"попыток")

