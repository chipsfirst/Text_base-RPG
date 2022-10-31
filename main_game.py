import random

def rolling(num_dice):
    roll_results = []

    for _ in range(num_dice):
        roll = random.randint(1, 6)

        roll_results.append(roll)

    return roll_results

class Player():

    def __init__(self, name, race, game_class, initiative, weapon, armory, inventory, money):
        self.name = name
        self.race = race
        self.game_class = game_class
        self.initiative = initiative
        self.weapon = weapon
        self.armory = armory
        self.inventory = inventory
        self.money = money

    race = []
    name = []
    game_class = []
    initiative = 3
    attack = 3
    weapon = []
    armory = []
    inventory = []
    money = 100

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
Player.name = input(str("Введите имя своего персонажа: \n"))
choose_race = print("Выберите расу своего персонажа.\n"
                    "Раса влияет на бонусы к характеристикам.\n"
                     "1) Человек.\n"
                     "2) Дварф\n"
                     "3) Эльф.\n"
                     "4) Полурослик.\n"
                     "5) Гном\n"
                     "6) Тифлинг. \n")
choose = []
player_race = choose.append(input("Введите номер выбранной расы или напишите 'Выход': "))
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
        Player.attack += 2
        print("Вы " + str(*Player.game_class) + ", и получаете бонус к атаке. Теперь значение вашей атаки равно " +
              str(Player.attack) + ".")
    elif player_class == "2":
        Player.game_class.append("следопыт")
        Character_Point.dexterity += 2
        print("Вы " + str(*Player.game_class) + ", и получаете бонус к ловкости. "
                                                "Теперь значение вашей ловкости равно " +
              str(Character_Point.dexterity) + ".")
    elif player_class == "3":
        Player.game_class.append("плут")
        Player.initiative += 2
        print("Вы " + str(*Player.game_class) + ", и получаете бонус к инициативе. Теперь её значение равно " + str(
            Player.initiative) + "."
              )
    elif player_class == "4":
        Player.game_class.append("волшебник")
        Character_Point.wisdom += 2
        print("Вы " + str(*Player.game_class) + ", и получаете бонус к мудрости. Теперь значение вашей мудрости равно "
              + str(Character_Point.wisdom) + ".")
    elif player_class == "5":
        Player.game_class.append("варвар")
        Character_Point.strange += 2
        print("Вы " + str(*Player.game_class) + ", и получаете бонус к силе. Теперь значение вашей силы равно " + str(
            Character_Point.strange) + ".")
    elif player_class == "6":
        Player.game_class.append("бард")
        Character_Point.charisma += 2
        Player.inventory.append("Лютня")
        Player.inventory.append("Плащ")
        Player.armory.append("Легкий доспех")
        Player.weapon.append("Рапира")
        Player.attack += 3
        print("Вы " + str(*Player.game_class) + ", и получаете бонус к харизме. Теперь значение вашей "
                                                "харизмы равно " + str(Character_Point.charisma) + ".")
        print(str(*Player.game_class), str(*Player.weapon),str(*Player.armory),
                  str(Player.inventory[0]),str(Player.inventory[1]))
    else:
        print("Вы ввели неверный номер.")
        player_class = classplayer.append(input("Введите номер выбранного класса: "))


