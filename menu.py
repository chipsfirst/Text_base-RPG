import sys, os



print("-------------------------Меню-------------------------")
print("1. Играть")
print("2. Правила")
print("3. Об игре")
print("4. Выход")
answer = input("Выберите нужный пункт:")
if answer == "1":
    os.system('cls||clear')
    import main_game
elif answer == "2":
    os.system('cls||clear')
    import rules
elif answer == "3":
    os.system('cls||clear')
    import about
elif answer == "4":
    os.system('cls||clear')
    sys.exit()
