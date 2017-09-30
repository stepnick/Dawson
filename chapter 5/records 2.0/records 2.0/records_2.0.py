scores = []
choice = None 
while choice != "0":
    print(
        """
        Рекорды 2.0
        0 - Выйти
        1 - Показать рекорды 
        2 - Добавить рекорды 
        """
        )
    choice = input("Ваш выбор: ")
    print()
    if choice == "0":
        print("До свидания.")
    elif choice == "1":
        print("Рекорды\n")
        print("ИМЯ\tРЕЗУЛЬТАТ")
        for entry in scores:
            score, name = entry
            print(name, "\t", score)
    elif choice == "2":
        name = input("Впишите имя игрока: ")
        score = int(input("Впишите его результат: "))
        entry = (score, name) 
        scores.append(entry)
        scores.sort(reverse=True)
        scores = scores[:5]
    else : 
        print("Извините, но такого пункта нет.")
input("Enter")

