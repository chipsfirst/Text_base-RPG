import sys, os, time


def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)


print_slow("Игра создана и поддерживается двумя программистами-энтузиастами. Сама игра служит скорее как тренировка \n"
           "навыков и проверка знаний) Она несложная, скорее забавная. Присоединяйтесь) \n"
           "Создатель: Карташов Владимир, Оптимизатор и дизайнер: Жемчужнов Дмитрий.\n")
print_slow("Хочешь ли ты вернуться в главное меню?")
answer = input("Ответь, да или нет:")
if answer.lower() == "да":
    os.system('cls||clear')
    import menu
else:
    sys.exit()
