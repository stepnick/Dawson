print("\tЭксклюзивная компьютерная сеть")
print("\tТолько для зарегистрированных пользователей!\n")
security = 0
username = ""
while not username :
    username = input("логин")
password = input("Пароль: ")
if username == "nick" and password == "secret":
    print("Привет, Никита.")
    security = 5
elif username == "S.Meier" and password == "civilization":
    print("Здраствуй, Сид")
    security = 3
elif username == "S.Miyamoto" and password == "thesims":
    print("Доброго время суток, Сигеру")
    security = 3
elif username == "W.WRIGHT" and password == "themist":
    print("Как дела, Уилл?")
    security = 3
elif username == "quest" and password == "quest":
    print("Добро пожаловать к нам в гсти")
    security = 1
else:
    print("Войти в систему не удалось. Должно быть, вы не очень-то экслюзивый гражданин.\n")
input
