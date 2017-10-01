son_father = {"Иван Иванов": ["Иван Андреевич", "Андрей Федорович"],
              "Андрей Никитин": ["Никита Николаевич","Джон Сноу"],
              "Сергей Сергеевич": ["Сергей Сергеевич", "Сергей Сергеевич"]
              }
choice = None
while choice != "0":
    print(
        """
        0 - Выйти
        1 - Найти отца и деда
        2 - Изменить отца и деда
        3 - Удалить отца и деда
        4 - Добавить отца и деда
        """
        )
    choice = input("Ваш выбор: ")
    print()
    if choice == "0":
        print("До свидания.")
    elif choice == "1":
        son = input("Введите имя ребенка: ")
        if son in son_father:
            print("Отцом является: ", son_father[son][0])
            print("Дедом является: ", son_father[son][1])
        else :
            print("У него нет отца(.")
    elif choice == "2":
        son = input("Введите имя ребенка: ")
        if son in son_father:
            father = input("Введите имя отца: ")
            ded = input("Введите имя деда: ")
            son_father[son][0] = father
            son_father[son][1] = ded
            print("Отцом является: ", son_father[son][0])
            print("Дедомв является: ", son_father[son][1])
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
            ded = input("Введите имя деда: ")
            son_father[son][0] = father
            son_father[son][1] = ded
            print("ДОбалено")
           
          

    
