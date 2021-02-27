import sys, time, os


def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)

print_slow("Это правила игры. Ты - путник, который очнулся в незнакомом для тебя мире. Твоя основная цель - на каждой \n"
           "локации решать загадки, общаться с персонажами и сражаться с врагами, получив в итоге пятый уровень и \n"
           "могущественный артефакт, который вернет тебя домой. Взаимодействие осуществляется с помощью цифр и ввода.\n")
print_slow("Хочешь ли ты вернуться в главное меню?")
answer = input("Ответь, да или нет:")
if answer.lower() == "да":
    os.system('cls||clear')
    import menu
else:
    sys.exit()