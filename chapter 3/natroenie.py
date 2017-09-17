import random
print("Я ощущая вашу энергетику. От моего экрана не скрыто не иодно из выших чувств")
print("Итак, ваше настроение...")
mood = random.randint(1, 3)
if mood == 1:
    print(":-)")
elif mood == 2:
    print(":-|")
elif mood == 3:
    print(":-(")
else:
    print("Не бывает такого настроения")
input
