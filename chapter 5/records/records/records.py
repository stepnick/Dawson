scores = []
choice = None 
while choice != "0":
    print(
        """
        0 - Выйти
        1 - Показать рекорды
        2 - Добавить рекорд
        3 - Удалить рекорд 
        4 - Соритровать рекорд
        """
        )
    choice = input("Ваш выбор: ")
    print()
    if choice == "0":
        print("До свидания.")
    elif choice == "1":
        print("Рекорды")
        for score in scores : 
            print(score)
    elif choice == "2":
        score = int(input("Впишите свой рекорд: "))
        scores.append(score)
    elif score == "3": 
        score = int(input("Какой рекорд удалить?: "))
        if score in scores:
            scores.remove(score)
        else: 
            print("Результат", score,"не содержится в списке рекордов.")
    elif choice == "4":
        scores.sort(reverse=True)
    else : 
        print("Извините, в меню нет такого пункта", choice)
input("Enter")