def read_global():
    print("В области видемости функции read_global() значение value равно", value)
def shadow_global():
    value = -10
    print("В области видемости функции shadow_global значение value равно", value)
def change_global():
    global value
    value = -10 
    print("В области видимости функции change_global значение value равно", value)
value = 10 
print("В глобальной области видимости значение value стало равно", value)
read_global()
print("Вернемся в глобальную область видимости. Здесь value по-прежднему равно", value)
shadow_global()
print("Вернемся в глобальную область видимости. Здесь value по-прежднему равно", value)
change_global()
print("Вернемся в глобальную область видимости. Здесь value изменилось на", value)
input 