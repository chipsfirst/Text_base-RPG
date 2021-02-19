import colorama
from colorama import Fore, Back
import Character
from locations import map_1
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
char = Character.Character(input("Введите ваше имя: "), input("Введите год вашего рождения: "),
                           input("Введите ваше местоположение: "))
time.sleep(b)
password = Character.Character.password(char.age)

print(f"{Back.GREEN + Fore.BLACK}Добро пожаловать в сны, " + char.name + ". Запомни этот день!")
from media import logo
time.sleep(5)
os.system('cls||clear') # - очистка экрана вывода.
print_slow("Ветер нежно нашептывает тебе песни на незнакомом языке. Ты чувствуешь яркий свет, бьющий в глаза. \n"
      "Заслонив их рукой, осматриваешься. Чистое поле до самого горизонта, ни птиц, ни животных вокруг. \n"
      "И прямо перед тобой камень с какими-то рисунками. Ты подходишь ближе. \n")
print(f"{Back.GREEN + Fore.BLACK}****************************************************************************")
print_slow("Это камень-указатель. На нем четыре стрелки с названиями.\n"
      "1) Вперед - Королевский замок.\n"
      "2) Назад - Цветочные луга.\n"
      "3) Направо - Древние топи.\n"
      "4) Налево - Ледяные пустоши.\n")
time.sleep(5)
path = input("Выбери направление, введя цифру. ")
if path == "1":
    print("Первый")