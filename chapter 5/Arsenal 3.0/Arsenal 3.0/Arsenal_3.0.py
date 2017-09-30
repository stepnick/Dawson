inventory = ["меч", "кольчуга", "щит", "целебное снадобье"]
print("Итак, в вашем арсенале: ")
for item in inventory:
    print(item)
input("\nНажмите Enter")
print("Cейчас в вашем распорежении", len(inventory),"предметов")
input("\nНажмите Enter")
if "целебное снадобье" in inventory:
    print("Вы еще поживете")
index = int(input("Введите индекс одного из предметов: "))
print("Под индексом", index, "в арсенале находится", inventory[index])
start = int(input("\nВведите начальный индекс среза: "))
finish = int(input("Введите конечный индекс среза: "))
print("Срез inventory[",start, ":", finish,"] - это ",end =" ")
print(inventory[start:finish])
input("\nНажмите Enter")
#соеденим два списка
chest = ("золото", "драгоценные камни")
print("Вы нашли ларец. В нем что-то есть.")
print(chest)
print("Вы приобщили содержимое ларца к своему арсеналу.")
inventory += chest
print("Теперь в вашем распоряжении: ")
print(inventory)
input("\nНажмите Enter")
print("Вы обменяли меч на арбалет.")
inventory[0] = "арбалет"
print(inventory)
input("\nНажмите Enter")
print("За золото и драгоценные камни вы купили магический кристал, способный предсказывать будущее ")
inventory[4:6] = ["магческий кристал"]
print("Теперь в вашем распоряжении:")
print(inventory)
input("\nНажмите Enter")
print("В тяжелом бою был раздроблен ваш щит.")
del inventory[2]
print("Вот, что осталось в вашем арсенале: ")
print(inventory)
input("\nНажмите Enter")
print("Воры лишили вас абалет и кольчуги.")
del inventory[:2]
print("Теперь в вашем арсеналде только: ")
print(inventory)
input("\nНажмите Enter")
