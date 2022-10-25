# import Character
import os, sys
# from locations import map_1, map_2, map_3, map_4
# from functions import Dragon1, Dragon2, Dragon3, Dragon4
import random
import time
#
# dice_roll = random.randint(1, 20)
# def print_slow(str):
#    for letter in str:
#         sys.stdout.write(letter)
#         sys.stdout.flush()
#         time.sleep(0.1)
#
def rolling(num_dice):
    roll_results = []

    for _ in range(num_dice):
        roll = random.randint(1, 6)

        roll_results.append(roll)

    return roll_results
#
#
# a = 2
# b = 1
# char = Character.Character(input("Придумайте имя своего персонажа: "), input("Придумайте возраст персонажа: "))
# time.sleep(b)
# password = Character.Character.password(char.age)
#
# choose_race = print("Выберите расу своего персонажа.\n"
#                     "1) Человек.\n"
#                     "2) Дварф\n"
#                     "3) Эльф.\n"
#                     "4) Полурослик.\n"
#                     "5) Гном\n"
#                     "6) Тифлинг. \n")
# race = []
# char_race = race.append(input("Введите выбранный номер расы:"))
# if char_race == "1":
#     Character.Score.strange_up("4")
#     print("Человек обладает бонусом к силе. Ваша сила сейчас" + Character.Score.strange_up())
# elif char_race == "2":
#     Character.Score.const_up("4")
#     print("Дварф обладает бонусом к телосложению. Ваше телосложение сейчас" + Character.Score.const_up())
# if char_race == "3":
#     Character.Score.dex_up("4")
#     print("Эльф обладает бонусом к ловкости. Ваша ловкость сейчас" + Character.Score.dex_up())
#
#     print("Добро пожаловать, " + char.name + ". Ты находишься в таверне, полной народу. Кто-то пьет, некоторые веселятся.")
# # from media import logo
# time.sleep(3)
# os.system('cls||clear')  # - очистка экрана вывода.
# print("Ветер нежно нашептывает тебе песни на незнакомом языке. Ты чувствуешь яркий свет, бьющий в глаза. \n"
#            "Заслонив их рукой, осматриваешься. Чистое поле до самого горизонта, ни птиц, ни животных вокруг. \n"
#            "И прямо перед тобой камень с какими-то рисунками. Ты подходишь ближе. \n")
# print("****************************************************************************")
# print("Это камень-указатель. На нем четыре стрелки с названиями.\n"
#            "1) Вперед - Королевский замок.\n"
#            "2) Назад - Цветочные луга.\n"
#            "3) Направо - Древние топи.\n"
#            "4) Налево - Ледяные пустоши.\n"
#            "5) Переписать карту на листок и положить в инвентарь. \n"
#            "6) Сражение со случайным монстром. \n"
#            "7) Бросить кубик\n")
#
#
# path = []
# ways = path.append(input("Выберите путь:"))
# for ways in path:
#     if ways == "1":
#         print(map_1.name)
#         print(map_1.description)
#         print(map_1.puzzle)
#         ways = path.append(input("Выберите путь:"))
#     elif ways == "2":
#         print(map_2.name)
#         print(map_2.description)
#         print(map_2.puzzle)
#         ways = path.append(input("Выберите путь:"))
#     elif ways == "3":
#         print(map_3.name)
#         print(map_3.description)
#         print(map_3.puzzle)
#         ways = path.append(input("Выберите путь:"))
#     elif ways == "4":
#         print(map_4.name)
#         print(map_4.description)
#         print(map_4.puzzle)
#         ways = path.append(input("Выберите путь:"))
#     elif ways == "5":
#         Character.Inventory.append(input("Записать: "))
#         print(Character.Inventory)
#         ways = path.append(input("Выберите путь:"))
#     elif ways == "6":
#         monsters = [str(Dragon1.name + Dragon1.description), str(Dragon2.name + Dragon2.description),
#                     str(Dragon3.name + Dragon3.description), str(Dragon4.name + Dragon4.description)]
#         print("На вас нападает " + random.choice(monsters))
#         ways = path.append(input("Выберите путь:"))
#     elif ways == "7":
#         print(rolling(1))
#         ways = path.append(input("Выберите путь:"))
#     elif ways == "Выход":
#         print("Игра окончена")
#         break
#     else:
#         ways = path.append(input("Выберите путь:"))

class Player():

    def __init__(self, name, race, game_class, initiative ):
        self.name = name
        self.race = race
        self.game_class = game_class
        self.initiative = initiative

    race = []
    name = []
    game_class = []
    initiative = 3
    attack = 3

class Character_Point():
    def __init__(self, strange, dexterity, constitution, intelligence, wisdom, charisma):
        self.strange = strange
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma

    strange = 8
    dexterity = 8
    constitution = 8
    intelligence = 8
    wisdom = 8
    charisma = 8

# def print_slow(str):
#    for letter in str:
#         sys.stdout.write(letter)
#         sys.stdout.flush()
#         time.sleep(0.2)

print("Приветствую тебя, путник!\n")
player_name = input(str("Введите имя своего персонажа: \n"))
choose_race = print("Выберите расу своего персонажа.\n"
                    "Раса влияет на бонусы к характеристикам.\n"
                     "1) Человек.\n"
                     "2) Дварф\n"
                     "3) Эльф.\n"
                     "4) Полурослик.\n"
                     "5) Гном\n"
                     "6) Тифлинг. \n")
choose = []
player_race = choose.append(input("Введите номер выбранной расы: "))
for player_race in choose:
    if player_race == "1":
        Player.race.append("человек")
        print(*Player.race)
        Character_Point.strange += 2
        print("Вы " + str(*Player.race) + ", и получаете бонус к силе. Теперь значение вашей силы равно " + str(Character_Point.strange) + "."
              )
    elif player_race == "2":
        Player.race.append("дварф")
        Character_Point.constitution += 2
        print("Вы " + str(*Player.race) + ", и получаете бонус к телосложению. Теперь значение вашего телосложения равно " + str(
            Character_Point.constitution) + "."
              )
    elif player_race == "3":
        Player.race.append("эльф")
        Character_Point.dexterity += 2
        print("Вы " + str(*Player.race) + ", и получаете бонус к ловкости. Теперь значение вашей ловкости равно " + str(
            Character_Point.dexterity) + "."
              )
    elif player_race == "4":
        Player.race.append("полурослик")
        Character_Point.charisma += 3
        print("Вы " + str(*Player.race) + ", и получаете бонус к харизме. Теперь значение вашей харизмы равно " + str(
            Character_Point.charisma) + "."
              )
    elif player_race == "5":
        Player.race.append("тифлинг")
        Character_Point.wisdom += 2
        print("Вы " + str(*Player.race) + ", и получаете бонус к мудрости. Теперь значение вашего телосложения равно " + str(
            Character_Point.wisdom) + "."
              )
    elif player_race == "6":
        Player.race.append("гном")
        Character_Point.constitution += 2
        print("Вы " + str(*Player.race) + ", и получаете бонус к телосложению. Теперь значение вашего телосложения равно " + str(
            Character_Point.constitution) + "."
              )
    else:
        print("Вы ввели неверный номер.")
        player_race = choose.append(input("Введите номер выбранной расы: "))

choose_class = print("Выберите класс своего персонажа.\n"
                    "Класс влияет на бонусы к инициативе и атаке.\n"
                     "1) Воин.\n"
                     "2) Следопыт\n"
                     "3) Плут.\n"
                     "4) Волшебник.\n"
                     "5) Варвар\n"
                     "6) Бард.\n")
classplayer = []
player_class = classplayer.append(input("Введите номер выбранного класса: "))
for player_class in classplayer:
    if player_class == "1":
        Player.game_class.append("воин")
        print(*Player.game_class)
        Player.attack += 2
        print("Вы " + str(*Player.game_class) + ", и получаете бонус к атаке. Теперь значение вашей атаки равно " + str(Player.attack) + "."
              )
        print("Ваши характеристики. Бонус расы:" + str(Character_Point.strange) + ". Бонус класса:" + str(Player.attack))
    elif player_race == "2":
        Player.race.append("дварф")
        Character_Point.constitution += 2
        print("Вы " + str(*Player.race) + ", и получаете бонус к телосложению. Теперь значение вашего телосложения равно " + str(
            Character_Point.constitution) + "."
              )
    elif player_race == "3":
        Player.race.append("эльф")
        Character_Point.dexterity += 2
        print("Вы " + str(*Player.race) + ", и получаете бонус к ловкости. Теперь значение вашей ловкости равно " + str(
            Character_Point.dexterity) + "."
              )
    elif player_race == "4":
        Player.race.append("полурослик")
        Character_Point.charisma += 3
        print("Вы " + str(*Player.race) + ", и получаете бонус к харизме. Теперь значение вашей харизмы равно " + str(
            Character_Point.charisma) + "."
              )
    elif player_race == "5":
        Player.race.append("тифлинг")
        Character_Point.wisdom += 2
        print("Вы " + str(*Player.race) + ", и получаете бонус к мудрости. Теперь значение вашего телосложения равно " + str(
            Character_Point.wisdom) + "."
              )
    elif player_race == "6":
        Player.race.append("гном")
        Character_Point.constitution += 2
        print("Вы " + str(*Player.race) + ", и получаете бонус к телосложению. Теперь значение вашего телосложения равно " + str(
            Character_Point.constitution) + "."
              )
    else:
        print("Вы ввели неверный номер.")
        player_race = choose.append(input("Введите номер выбранной расы: "))