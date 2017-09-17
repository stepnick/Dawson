import random
print("Постарайтесь отгадать число(от 1 до 100) за минимальное количесвто попыток ")
the_number = random.randint(1, 100)
guess = int(input("Ваше предположение"))
tries = 1
while guess != the_number :
    if guess > the_number:
        print("Меньше")
    else:
        print("Больше")
    guess = int(input("Ваше предположение: "))
    tries += 1
print("Вы угадали за", tries,"попыток")
input
