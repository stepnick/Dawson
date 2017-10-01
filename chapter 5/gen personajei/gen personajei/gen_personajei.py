person = [0, 0, 0, 0]
Power = 0
Agility = 0
Health = 0 
Knowlage = 0
choice = None
choice1 = None
i = 30 
sumDOSTUPNpoints = 30
while choice != 0:
    print(
    """
    0 - Выйти
    1 - Добавить характеристку
    2 - Убрать пункты характреристики
    3 - Посмотреть характеристику
    """)
    choice = input("Введите цифру: ")
    if choice == "1" or choice == "2":
        print(
            """
            0 - Ловкость
            1 - Сила 
            2 - Здоровье 
            3 - Мудрость
            """)
        if choice == "1":
            print("К какой характеристике вы хоттите лобавить очки?")
            z = +1
        else:
            print("От какой характеристике вы хоттите отнять очки?")
            z = -1

        characteristic = int(input())
        if characteristic < len(person):
            characteristicValue = int(input("Введите, сколько очков:"))

            if z > 0 and characteristicValue > sumDOSTUPNpoints: 
                person[characteristic] += sumDOSTUPNpoints
                sumDOSTUPNpoints = 0

            elif z < 0 and characteristicValue > person[characteristic]:
                sumDOSTUPNpoints += person[characteristic]
                person[characteristic] = 0

            else: 
                person[characteristic] += characteristicValue * z
                
                sumDOSTUPNpoints -= characteristicValue * z

        print("Осталось очков: ", sumDOSTUPNpoints)
    elif choice == "3":
        print("Ваша характеристика: ")
        print("Ловкость - ","*" * person[0])
        print("Сила - ","*" * person[1])
        print("Здоровье -","*" * person[2])
        print("Мудрость -","*" * person[3])
    else :
        print("До свидания.")


