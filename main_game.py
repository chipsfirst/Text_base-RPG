import Character
import random

def rolling(num_dice):
    roll_results = []
    for _ in range(num_dice):
        roll = random.randint(1, 6)
        roll_results.append(roll)
    return roll_results

print("Приветствую тебя, путник!\n")
Character.Player.name = input(str("Введите имя своего персонажа: \n"))
choose_race = print("Выберите расу своего персонажа.\n"
                    "Раса влияет на бонусы к характеристикам.\n"
                     "1) Человек.\n"
                     "2) Дварф\n"
                     "3) Эльф.\n"
                     "4) Полурослик.\n"
                     "5) Тифлинг\n"
                     "6) Гном. \n")
choose = []
player_race = choose.append(input("Введите номер выбранной расы или напишите 'Выход': "))
for player_race in choose:
    if player_race == "1":
        Character.Player.race.append("человек")
        print(*Character.Player.race)
        Character.Character_Point.strange += 2
        print("Вы " + str(*Character.Player.race) + ", и получаете бонус к силе. Теперь значение вашей силы равно " +
              str(Character.Character_Point.strange) + "."
              )
    elif player_race == "2":
        Character.Player.race.append("дварф")
        Character.Character_Point.constitution += 2
        print("Вы " + str(*Character.Player.race) + ", и получаете бонус к телосложению. Теперь значение вашего телосложения равно " + str(
            Character.Character_Point.constitution) + "."
              )
    elif player_race == "3":
        Character.Player.race.append("эльф")
        Character.Character_Point.dexterity += 2
        print("Вы " + str(*Character.Player.race) + ", и получаете бонус к ловкости. Теперь значение вашей ловкости равно " + str(
            Character.Character_Point.dexterity) + "."
              )
    elif player_race == "4":
        Character.Player.race.append("полурослик")
        Character.Character_Point.charisma += 3
        print("Вы " + str(*Character.Player.race) + ", и получаете бонус к харизме. Теперь значение вашей харизмы равно " + str(
            Character.Character_Point.charisma) + "."
              )
    elif player_race == "5":
        Character.Player.race.append("тифлинг")
        Character.Character_Point.wisdom += 2
        print("Вы " + str(*Character.Player.race) + ", и получаете бонус к мудрости. Теперь значение вашего телосложения равно " + str(
            Character.Character_Point.wisdom) + "."
              )
    elif player_race == "6":
        Character.Player.race.append("гном")
        Character.Character_Point.constitution += 2
        print("Вы " + str(*Character.Player.race) + ", и получаете бонус к телосложению. Теперь значение вашего телосложения равно " + str(
            Character.Character_Point.constitution) + "."
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
        Character.Player.game_class.append("воин")
        Character.Player.attack += 2
        print("Вы " + str(*Character.Player.game_class) + ", и получаете бонус к атаке. Теперь значение вашей атаки равно " +
              str(Character.Player.attack) + ".")
    elif player_class == "2":
        Character.Player.game_class.append("следопыт")
        Character.Character_Point.dexterity += 2
        print("Вы " + str(*Character.Player.game_class) + ", и получаете бонус к ловкости. "
                                                "Теперь значение вашей ловкости равно " +
              str(Character.Character_Point.dexterity) + ".")
    elif player_class == "3":
        Character.Player.game_class.append("плут")
        Character.Player.initiative += 2
        print("Вы " + str(*Character.Player.game_class) + ", и получаете бонус к инициативе. Теперь её значение равно " + str(
            Character.Player.initiative) + "."
              )
    elif player_class == "4":
        Character.Player.game_class.append("волшебник")
        Character.Character_Point.wisdom += 2
        print("Вы " + str(*Character.Player.game_class) + ", и получаете бонус к мудрости. Теперь значение вашей мудрости равно "
              + str(Character.Character_Point.wisdom) + ".")
    elif player_class == "5":
        Character.Player.game_class.append("варвар")
        Character.Character_Point.strange += 2
        print("Вы " + str(*Character.Player.game_class) + ", и получаете бонус к силе. Теперь значение вашей силы равно " + str(
            Character.Character_Point.strange) + ".")
    elif player_class == "6":
        Character.Player.game_class.append("бард")
        Character.Character_Point.charisma += 2
        print("Вы " + str(*Character.Player.game_class) + ", и получаете бонус к харизме. Теперь значение вашей "
                                                "харизмы равно " + str(Character.Character_Point.charisma) + ".")
    else:
        print("Вы ввели неверный номер.")
        player_class = classplayer.append(input("Введите номер выбранного класса: "))


print(Character.Char_Asset())