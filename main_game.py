import colorama
from colorama import Fore, Back
import Character
import os, sys

colorama.init(autoreset=True)
import time


def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)


a = 2
b = 1
char = Character.Character(input("Введите ваше имя: "), input("Введите год вашего рождения: "))
time.sleep(b)
password = Character.Character.password(char.age)

print(f"{Back.GREEN + Fore.BLACK}Добро пожаловать в сны, " + char.name + ". Запомни этот день!")
# from media import logo
time.sleep(5)
os.system('cls||clear')  # - очистка экрана вывода.
print_slow("Ветер нежно нашептывает тебе песни на незнакомом языке. Ты чувствуешь яркий свет, бьющий в глаза. \n"
           "Заслонив их рукой, осматриваешься. Чистое поле до самого горизонта, ни птиц, ни животных вокруг. \n"
           "И прямо перед тобой камень с какими-то рисунками. Ты подходишь ближе. \n")
print(f"{Back.GREEN + Fore.BLACK}****************************************************************************")
print_slow("Это камень-указатель. На нем четыре стрелки с названиями.\n"
           "1) Вперед - Королевский замок.\n"
           "2) Назад - Цветочные луга.\n"
           "3) Направо - Древние топи.\n"
           "4) Налево - Ледяные пустоши.\n"
           "5) Переписать карту на листок и положить в инвентарь. \n")
time.sleep(5)
path = input("Выбери направление, введя цифру: ")
if path == "1":
    import locations.map_1
if path == "2":
    print_slow(map_1.name + "\n")
    print(f"{Back.GREEN + Fore.BLACK}****************************************************************************")
    print_slow(map_1.description)
if path == "3":
    print_slow(map_1.name + "\n")
    print(f"{Back.GREEN + Fore.BLACK}****************************************************************************")
    print_slow(map_1.description)
if path == "4":
    print_slow(map_1.name + "\n")
    print(f"{Back.GREEN + Fore.BLACK}****************************************************************************")
    print_slow(map_1.description)
elif path == "5":
    write1 = Character.Inventory.append("Карта")
    # point = input("У вас есть возможность повысить силу на два очка. Введите: ")
    # level1 = Character.Points.strange_up(int(point))
    # print("ваша сила возросла на 1 и теперь равна " + str(level1))
else:
    print("Введи цифру из указанного диапазона или попробуй еще раз) ")