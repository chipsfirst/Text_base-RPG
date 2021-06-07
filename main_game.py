import colorama, random
from colorama import Fore, Back
import Character
import os, sys
from locations import map_1, map_2

colorama.init(autoreset=True)
import time

dice_roll = random.randint(1,20)
#def print_slow(str):
#   for letter in str:
#        sys.stdout.write(letter)
#       sys.stdout.flush()
#        time.sleep(0.1)


a = 2
b = 1
char = Character.Character(input("Введите ваше имя: "), input("Введите год вашего рождения: "))
time.sleep(b)
password = Character.Character.password(char.age)

print(f"{Back.GREEN + Fore.BLACK}Добро пожаловать в сны, " + char.name + ". Запомни этот день!")
# from media import logo
time.sleep(5)
os.system('cls||clear')  # - очистка экрана вывода.
print("Ветер нежно нашептывает тебе песни на незнакомом языке. Ты чувствуешь яркий свет, бьющий в глаза. \n"
           "Заслонив их рукой, осматриваешься. Чистое поле до самого горизонта, ни птиц, ни животных вокруг. \n"
           "И прямо перед тобой камень с какими-то рисунками. Ты подходишь ближе. \n")
print(f"{Back.GREEN + Fore.BLACK}****************************************************************************")
print("Это камень-указатель. На нем четыре стрелки с названиями.\n"
           "1) Вперед - Королевский замок.\n"
           "2) Назад - Цветочные луга.\n"
           "3) Направо - Древние топи.\n"
           "4) Налево - Ледяные пустоши.\n"
           "5) Переписать карту на листок и положить в инвентарь. \n"
           "6) Бросить кубик\n")


path = []
ways = path.append(input("Input your way:"))
for ways in path:
    if ways == "1":
        print(map_1.name)
        print(map_1.description)
        print(map_1.puzzle)
        break
    elif ways == "2":
        print(map_2.name)
        print(map_2.description)
        print(map_2.puzzle)
        break
    elif ways == "6":
        print(dice_roll)
    else:
        ways = path.append(input("Input your way:"))

