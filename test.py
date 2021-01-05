import colorama
from colorama import Fore, Back
import data_maps

colorama.init(autoreset=True)


class Character:
    def __init__(self, name, age, location):
        self.name = name
        self.age = age
        self.location = location


char = Character(input("Введите ваше имя: "), input("Введите год вашего рождения: "), input("Введите ваше местоположение: "))


password = bin(int(char.age))


print(f"{Back.GREEN + Fore.BLACK}Добро пожаловать в сны, " + char.name + ". Запомни этот день!")


class Location:
    def __init__(self, map_name, map_description):
        self.map_name = map_name
        self.map_description = map_description


maps_1 = Location("Снежная площадь", data_maps.data_locations[0])
maps_2 = Location("Ледяной дворец", data_maps.data_locations[1])
maps_3 = Location("Фабрика игрушек", data_maps.data_locations[2])
maps_4 = Location("Конфетный двор", data_maps.data_locations[3])
maps_5 = Location("Еловые поля", data_maps.data_locations[4])
maps_6 = Location("Аттракционы Снеговиков", data_maps.data_locations[5])
maps_7 = Location("Снежковый Тир", data_maps.data_locations[6])


class Interactive:
    def __init__(self, active1, active2, active3, active4):
        self.active1 = active1
        self.active2 = active2
        self.active3 = active3
        self.active4 = active4


active_maps_1 = Interactive("1. Исследовать", "2. Отдохнуть", "3. Читать записи", "4. Купить сувенир")


class Active(Interactive):
    def active_1(self):
        print("Вы осматриваетесь. Видите огромные ледяные поверхности, богато украшенные здания и различные магазины.")
    def active_2(self):
        print("Решив отдохнуть, вы присаживаетесь на скамейку и достаете термос с чаем.")
    def active_3(self):
        print("Открыв свой блокнот, вы начинаете кропотливо описывать все что видите.")
    def active_4(self):
        print("Увидев ближайший магазинчик, вы отправляетесь туда в поисках сувениров.")


print("Выбери, что делать дальше?")
print("1. Осмотреться")
print("2. Идти дальше!")
choose = input("Введите число: ")
if choose == "1":
    print("Вы попали на локацию ", maps_1.map_name)
    print("Выбери что будешь делать? ")
    print(active_maps_1.active1)
    print(active_maps_1.active2)
    print(active_maps_1.active3)
    print(active_maps_1.active4)
    choose2 = input("Что будешь делать?: ")
    if choose2 == "1":
        Active.active_1("1")
    elif choose2 == "2":
        Active.active_2("2")
    elif choose2 == "3":
        Active.active_3("3")
    elif choose2 == "4":
        Active.active_4("4")
elif choose == "2":
    print("Открыв двери, вы отправляетесь в", maps_2.map_name)
