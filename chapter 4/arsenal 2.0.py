inventory = ("меч",
             "кольчуга",
             "щит",
             "целебное снадобье")
print("\nИтак, в вашем арсенале:")
for item in inventory:
    print(item)
input("Нажмите Enter, чтобы продолжить")
print("Сейчас в вашем распоряжении", len(inventory),"предмета/ов")
input("Нажмите Enter, чтобы продолжить")
if "целебное снадобье" in inventory:
    print("Вы еще поживете и повоюете.")
index = int(input("\nВведите индекс одного предмета: "))
print("Под индексом", index,"находится", inventory[index])
start = int(input("\nВведите начальный индекс: "))
finish = int(input("Введите конечный индекс среза:"))
print("Cрез inventory[",start ,":", finish,"] - это", end = "")
print(inventory[start:finish])
input("Нажмите Enter, чтобы продолжить")
chest = ("золото", "драгоценные камни")
print("Вы нашли ларец. Вот , что в нем есть: ")
print(chest)
print("Вы приобщили содержимое ларца к своему арсеналу.")
inventory += chest
print("Теперь в вашем распоряжении: ")
print(inventory)
input("Нажмите Enter, чтобы продолжить")
