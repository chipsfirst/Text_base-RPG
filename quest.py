import colorama
from colorama import Fore, Back

from data_maps import data_locations

colorama.init(autoreset=True)

client_data = []
steps = []
character = input(f"{Back.GREEN + Fore.BLACK}Добро пожаловать в Новогодний квест! Как вас зовут?:")
client_data.append(character)
location = input(f"{Back.BLUE + Fore.BLACK}Откуда вы к нам?:")
client_data.append(location)
print("------------------------------------------------------------------------------------")
question1 = input(
    f'{Back.WHITE + Fore.BLACK}Отличные новости, ' + client_data[0] + '! Двери нашей резиденции откроются '
                                                                      'совсем скоро. '
                                                                      'Хотите посмотреть карту?:').title()
if question1 == "Да":
    delimiter = ", \n"
    output = delimiter.join(data_locations)
    print(Fore.GREEN + output)
    print()
    print("**********************************************************************************************")
else:
    print("Попробуйте еще раз!")

change_loc = input("Куда хотите отправиться?:").title()
if change_loc in data_locations:
    if change_loc != data_locations:
        print(f"{Fore.WHITE + Back.RED}Попробуйте еще разок!")
    if change_loc == "Снежная площадь":
        print(f"{Fore.WHITE + Back.BLUE} "
              "городом. А если в новогоднюю ночь потереть шарик на елке, исполнятся любые мечты!")
    elif change_loc == "Ледяной дворец":
        print(f"{Fore.WHITE + Back.BLUE})
    elif change_loc == "Фабрика игрушек":
        print(f"{Fore.WHITE + Back.BLUE}")
    elif change_loc == "Конфетный двор":
        print(f"{Fore.WHITE + Back.BLUE}")
    elif change_loc == "Еловые поля":
        print(f"{Fore.WHITE + Back.BLUE}")
    elif change_loc == "Аттракционы Снеговиков":
        print(f"{Fore.WHITE + Back.BLUE}")
    elif change_loc == "Снежковый Тир":
        print(f"{Fore.WHITE + Back.BLUE}")
    else:
        print(f"{Fore.WHITE + Back.RED}Попробуйте еще разок!")

