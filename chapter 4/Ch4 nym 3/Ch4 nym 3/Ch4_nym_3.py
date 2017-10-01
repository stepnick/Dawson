import random
WORDS = ("питон", "анаграма", "простая", "сложная", "ответ", "постаканник")
word = random.choice(WORDS)
word_true = word
correct = word
jumble = ""
choice = None
Max_points = 10
while word:
    position = random. randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]
    word_pod = word 
print(
    """
        Добро пожаловать в игру 'Анаграммы'!
    Надо переставить буквы так , чтобы получилось осмысленное слово.
    """)
print("Вот анаграмма:", jumble)
guess = input("\nПопробуйте отгадать исходное слово: ")
while guess != correct and guess != "":
    print("Вы не правы")
    print(
        """Вы можете использовать подсказку, если хотите.
           Нажмите:
           1 - если хотите получить подсказку
           2 - если хотите найти слово самостоятельно
           """)
    if choice == "1":
        word = 
        print("Буква по номером", "стоит на своем месте: ")
    guess = input("\nПопробуйте отгадать исходное слово: ")
    if guess == correct :
        print("Да, вы угадали!")
input("Введите enter")

