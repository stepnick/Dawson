geek = {"404" : "Не знать, не владеть информацией. От сообщения об ошибке 404'Страница не найдена'.",
        "Googling" : "'Гугдение', поиск в Сети чего-либо.",
        "Keyboard Plaque" : "Мусор, который скапливается на клавиатуре компьютера.",
        "Link Rot" : "Процесс устаревания гиперссылок на веб-страницах.",
        "Percussive Maintenance" : "О ситуации, когда кто- либо бьет по корпусу неисправного электронного прибора в надежде исправить его работу",
        "Uninstalled" : "Об увольнении кого-либо. Особенно ппулярно на рубеже 1990-2000-х годов."}
choice = None 
while choice != "0":
    print(
        """
        Переводчик с гигского на русский
        0 - Выйти
        1 - Найти толкование термина 
        2 - Добавить термин 
        3 - Изменить толкование 
        4 - Удалить термин
        """
        )
    choice = input("Ваш выбор: ")
    print()
    if choice == "0":
        print("До свидания")
    elif choice == "1":
        term = input("Какой термин вы хотите перевести?")
        if term in geek:
            definition = geek[term]
            print("\n", term,"означает", definition)
        else:
            print("\nУвы, этот термин мне незаком:", term)
    elif choice == "2":
        term = input("Какой термин гигского языка вы хотите добавить? ")
        if term not in geek:
            definition = input("Введите ваше толкование: ")
            geek[term] = definition
            print("\nТермин", term,"добавлен в словарь")
        else: 
            print("Такой термин уже есть!")
    elif choice == "3":
        term = input("Какой термин вы хотите переопределить? ")
        if term in geek:
            definition = input("Впишите ваше толкование: ")
            geek[term] = definition
            print("\nТермин", term,"переопределен.")
        else:
            print("\nТакого термина пока нет. Попробуйте добавить его в словарь.")
    elif choice == "4":
        term = input("Какой термин вы хотите удалить? ")
        if term in geek:
            del geek[term]
            print("\nТермин", term,"был удален")
        else :
            print("Термина", term,"нет в словаре")
    else : 
        print("Нет такого пункта.")
input("Введите Enter")