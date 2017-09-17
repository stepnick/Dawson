
import random
words = ("дота", "игра", "школа", "егэ")
word = random.choice(words)
correct = word
ScreenWord = len(word) * "*"
print("Вот ваше слово", ScreenWord)
i = 1
URword = ""
print("У вас есть 5 попыток")
while i <= 5:
    a = input("Введите преполагаемую букву: ")
    if a in word :
        print("Такая буква есть")
        for j in range(0,len(word)):
            if a == word[j]:
                ScreenWord = ScreenWord[0:j] + word[j] + ScreenWord[j+1:len(word)]
        print(ScreenWord)
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
