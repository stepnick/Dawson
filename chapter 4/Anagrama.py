import random
WORDS = ("питон", "анаграма", "простая", "сложная", "ответ", "постаканник")
word = random.choice(WORDS)
correct = word
jumble = ""
while word:
    position = random. randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]
print(
    """
        Добро пожаловать в игру 'Анаграммы'!
    Надо переставить буквы так , чтобы получилось осмысленное слово.
    """)
print("Вот анаграмма:", jumble)
guess = input("\nПопробуйте отгадать исходное слово: ")
while guess != correct and guess != "":
    print("Вы не правы")
    guess = input("\nПопробуйте отгадать исходное слово: ")
    if guess == correct :
        print("Да, вы угадали!")
input("Введите enter")
