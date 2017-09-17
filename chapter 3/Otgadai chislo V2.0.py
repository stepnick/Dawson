import random
print("Постарайтесь отгадать число(от 1 до 100) за минимальное количесвто попыток ")
print("У вас есть 10 попыток")
the_number = random.randint(1, 100)
guess = int(input("Ваше предположение"))
tries = 1
k = 1 
while guess != the_number and tries != 10 :
    if guess > the_number:
        print("Меньше")
    else:
        print("Больше")
    guess = int(input("Ваше предположение: "))
    tries += 1
if guess == the_number:
    print("Вы угадали за", tries,"попыток")
else :
    print("Вам не удалось угадать число с 10 попыток")
input
