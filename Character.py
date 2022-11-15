import random

def rolling(num_dice):
    roll_results = []
    for _ in range(num_dice):
        roll = random.randint(1, 6)
        roll_results.append(roll)
    return roll_results

class Player():

    def __init__(self, name, race, game_class, initiative, weapon, armory, inventory, money, ac):
        self.name = name
        self.race = race
        self.game_class = game_class
        self.initiative = initiative
        self.weapon = weapon
        self.armory = armory
        self.inventory = inventory
        self.money = money
        self.ac = ac

    race = []
    name = []
    game_class = []
    initiative = 3
    attack = 3
    ac = 13
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

def Char_Asset():
    print("Вас зовут " + str(Player.name) + ". Вы -" + str(*Player.race) + " класса " + str(*Player.game_class) + ".")
    print("Сила равна " + str(Character_Point.strange) + ".")
    print("Ловкость равна " + str(Character_Point.dexterity) + ".")
    print("Телосложение равно " + str(Character_Point.constitution) + ".")
    print("Мудрость равна " + str(Character_Point.wisdom) + ".")
    print("Интеллект равен " + str(Character_Point.intelligence) + ".")
    print("Харизма равна " + str(Character_Point.charisma) + ".")
    print("Ваша атака равна " + str(Player.attack) + ".")
    print("Ваша инициатива равна " + str(Player.initiative) + ".")
    print("Ваш класс доспеха равен " + str(Player.ac) + ".")
    return("Удачного путешествия!")




