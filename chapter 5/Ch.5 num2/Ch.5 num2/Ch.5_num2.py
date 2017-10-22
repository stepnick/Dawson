char = {"" : "",
        "" : "",
        "" : "",
        "" : ""}
Power = 0
Agility = 0
Health = 0 
Knowlage = 0
choice = None
choice1 = None
while choice != 0:
    print(
    """
    0 - Выйти
    1 - Добавить характеристку
    2 - Убрать пункты характреристики
    3 - Посмотреть характеристику
    """)
    choice = input("Введите цифру: ")
    if choice == "1":
        print(
            """
            0 - Ловкость
            1 - Сила 
            2 - Здоровье 
            3 - Мудрость
            """)
        choice = input("К какой характеристике вы хотите добавить очки?")
        if choice == "0":
            Agility += 1 
            points -= 1 
            print("Ловкость - ", Agility * "*")
        if choice == "1":
            Power += 1 
            points -= 1 
            print("Сила - ", Power * "*")
        if choice == "2":
            Health += 1 
            points -= 1 
            print("Здоровье - ", Health * "*")
        if choice == "3":
            Knowlage += 1 
            points -= 1 
            print("Мудрость - ", Knowlage * "*")
    elif choice == "2":
        print(
            """
            0 - Ловкость
            1 - Сила 
            2 - Здоровье 
            3 - Мудрость
            """)
        choice = input("У какой характеристике вы хотите убрать очки?")
        if choice == "0":
            Agility -= 1 
            points += 1
            print("Ловкость - ", Agility * "*")
        if choice == "1":
            Power -= 1 
            points += 1
            print("Сила - ", Power * "*")
        if choice == "2":
            Health -= 1 
            points += 1
            print("Здоровье - ", Health * "*")
        if choice == "3":
            Knowlage -= 1 
            points += 1
            print("Мудрость - ", Knowlage * "*")
    elif choice == "3":
        print("Ваша характеристика: ")
        print("Ловкость - ", Agility * "*")
        print("Сила - ", Power * "*")
        print("Здоровье -", Health * "*")
        print("Мудрость -", Knowlage * "*")
    else :
        print("До свидания.")

        