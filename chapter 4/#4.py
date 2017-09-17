import random
words = ("дота", "игра", "школа", "егэ")
word = random.choice(words)
correct = word
print("Кол-во букв в слове", len(word))
i = 1
URword = ""
print("У вас есть 5 попыток")
while i <= 5:
    a = input("Введите преполагаемую букву: ")
    if a in word :
        print("Такая буква есть")
    else :
        print("Такой буквы нет")
    i += 1
print("Теперь попробуй угадать все слово: ")
guess = input(("Введите ваше слово"))
while guess != correct and guess != "":
    print("Вы не правы")
    guess = input("\nПопробуйте отгадать исходное слово: ")
    if guess == correct :
        print("Да, вы угадали!")
input("Введите enter")
