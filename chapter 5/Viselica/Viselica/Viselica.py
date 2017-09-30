import random 
HANGMAN = (
    """
    ------
    |    |
    |
    |
    |
    |
    |
    |
  -----------
  """,
  """
     ------
    |    |
    |    O
    |  
    |    
    |   
    |   
    |
  -----------
  """,
  """
    ------
    |    |
    |    O
    |   -+-
    |    
    |   
    |   
    |
  -----------
  """,
  """
    ------
    |    |
    |    O
    |   -+-\
    |    
    |   
    |   
    |
  -----------
  """,
  """
   ------
    |    |
    |    O
    |  /-+-\
    |    
    |   
    |   
    |
  -----------
  """,
  """
    ------
    |    |
    |    O
    |  /-+-\
    |    |
    |   
    |   
    |
  -----------
  """,
  """
    ------
    |    |
    |    O
    |  /-+-\
    |    |
    |   | 
    |   | 
    |
  -----------
  """,
  """
    ------
    |    |
    |    O
    |  /-+-\
    |    |
    |   | |
    |   | |
    |
  -----------
  """)
MAX_WRONG = len(HANGMAN) - 1 
WORDS = ("ПИТОН", "ДОТА", "ЭКЗАМЕНЫ", "ЕЩКЕРЕ", "ОНО", "ИНФОРМАТИКА")
word = random.choice(WORDS)
so_far = "-" * len(word)
wrong = 0
used = []
print("Добро пажаловать в игру 'Виселица'!")
while wrong < MAX_WRONG and so_far != word: 
    print(HANGMAN[wrong])
    print("\nВы уже предлагали следующие буквы:\n", used)
    print("\nОтгаданное вами в слове выглядит так: \n",so_far)
    guess = input("\n\nВведите букву: ")
    guess = guess.upper()
    while guess in used : 
        print("Вы уже предлагали эту букву", guess)
        guess = input("\n\nВведите букву: ")
        guess = guess.upper()
    used.append(guess)
    if guess in word: 
        print("\nДа, буква", guess,"есть в слове")
        new = ""
        for i in range(len(word)):
            if guess == word[i]:
                new += guess
            else: 
                new += so_far[i]
        so_far = new
    else :
        print("К сожалению, буквы", guess,"нет в слове")
        wrong += 1
if wrong == MAX_WRONG:
    print(HANGMAN[wrong])
    print("Вас повесели.")
else : 
    print("Вы отгадали!")
print("\nБыло загаданно слово", word)
input("Введите Enter")