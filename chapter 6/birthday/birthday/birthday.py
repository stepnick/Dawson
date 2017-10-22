def birthday1(name, age):
    print("C днем рождения,", name,".Вам сегодня исполняется", age,", не так ли ?\n")
def birthday2(name = "Товарищ Иванов",age = 1):
    print("C днем рождения,", name,".Вам сегодня исполняется", age,", не так ли ?\n")
birthday1("Товарищ Иванов", 1)
birthday2(1, "Товарищ Иванов")
birthday1(name = "Товарищ Иванов", age = 1)
birthday1(age = 1, name = "Товарищ Иванов")
birthday2()
birthday2(name = "Катя")
birthday2(age = 12)
birthday2(name = "Катя", age = 12)
birthday2("Катя", 12)
input