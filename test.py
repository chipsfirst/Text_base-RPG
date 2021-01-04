import colorama
from colorama import Fore, Back
import data_maps

colorama.init(autoreset=True)


class Character:
    def __init__(self, name, age, location):
        self.name = name
        self.age = age
        self.location = location


char = Character(input("Введите ваше имя: "), input("Введите ваш возраст: "), input("Введите ваше местоположение: "))
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


print("Выбери, что делать дальше?")
print("1. Осмотреться")
print("2. Идти дальше!")
choose = input("Введите число: ")
if choose == "1":
    print("You inter")
elif choose == "2":
    print("Hoy")
