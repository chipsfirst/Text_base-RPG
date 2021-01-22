import colorama
from colorama import Fore, Back
import data_maps
import Character
import interactive

colorama.init(autoreset=True)

char = Character.Character(input("Введите ваше имя: "), input("Введите год вашего рождения: "),
                           input("Введите ваше местоположение: "))

password = Character.Character.password(char.age)

print(f"{Back.GREEN + Fore.BLACK}Добро пожаловать в сны, " + char.name + ". Запомни этот день!")
print("Выбери, что делать дальше?")
print("1. Осмотреться")
print("2. Идти дальше!")
choose = input("Введите число: ")
if choose == "1":
    print("Вы попали на локацию ", data_maps.maps_1.map_name)
    print("Выбери что будешь делать? ")
    print(interactive.active_maps_1.active1)
    print(interactive.active_maps_1.active2)
    print(interactive.active_maps_1.active3)
    print(interactive.active_maps_1.active4)
    choose2 = input("Что будешь делать?: ")
    if choose2 == "1":
        interactive.Active.active_1("1")
    elif choose2 == "2":
        interactive.Active.active_2("2")
    elif choose2 == "3":
        interactive.Active.active_3("3")
    elif choose2 == "4":
        interactive.Active.active_4("4")
elif choose == "2":
    print("Открыв двери, вы отправляетесь в", data_maps.maps_2.map_name)
