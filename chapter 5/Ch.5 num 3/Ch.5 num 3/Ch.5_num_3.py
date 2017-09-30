son_father = {"Иван Иванов", "Иван Андреевич",
              "Андрей Никитин", "Никита Николаевич",
              "Сергей Сергеевич", "Сергей Сергеевич"}
choice = None
while choice != "0":
    print(
        """
        0 - Выйти
        1 - Найти отца 
        2 - Изменить отца
        3 - Удалить отца 
        4 - Добавить отца
        """
        )
    choice = input("Ваш выбор: ")
    print()
    if choice == "0":
        print("До свидания.")
    elif choice == "1":
        son = input("Введите имя ребенка: ")
        if son in son_father:
            print("Отцом является: ", son_father[son])
        else :
            print("У него нет отца(.")
    elif choice == "2":
        son = input("Введите имя ребенка")
        if son in son_father:
            father = input("Введите имя отца: ")
            son_father[son] = father
            print("Отцом является", son_father[son])
    elif choice == "3":
        son = input("Введите имя ребенка: ")
        if son in son_father:
            del son_father[son]
            print("Данные удалены.")
        else:
            print("Такого ребенка нет")
    elif choice == "4":
        son = input("Введите имя ребенка: ")
        if son in son_father:
            print("Такой ребенок уже есть.")
        else:
            father = input("Введите имя отца: ")
            son_father[son] = father
            print("ДОбалено")
           
          

    