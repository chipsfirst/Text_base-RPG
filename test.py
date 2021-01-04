import colorama
from colorama import Fore, Back
import data_maps

colorama.init(autoreset=True)


class Character:
    def __init__(self, name, age, location):
        self.name = name
        self.age = age
        self.location = location

    def all(self):
        return (self.name + str(self.age))


char = Character(input("Введите ваше имя: "), input("Введите ваш возраст: "), input("Введите ваше местоположение: "))
print(f"{Back.GREEN + Fore.BLACK}Добро пожаловать в сны, " + char.name + ". Запомни этот день!")


class Location:
    def __init__(self, map_name, map_description, map_size):
        self.map_name = map_name
        self.map_description = map_description
        self.map_size = map_size

maps_1 = Location("Снежная площадь", data_maps.data_locations[0], "small")
print(maps_1.map_name)
print(maps_1.map_description)

