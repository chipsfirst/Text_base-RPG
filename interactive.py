import data_maps

class Interactive:
    def __init__(self, active1, active2, active3, active4):
        self.active1 = active1
        self.active2 = active2
        self.active3 = active3
        self.active4 = active4


active_maps_1 = Interactive("1. Исследовать", "2. Отдохнуть", "3. Читать записи", "4. Купить сувенир")


class Active(Interactive):
    def __init__(self):
        pass

    def active_1(self):
        print("Вы осматриваетесь. Видите огромные ледяные поверхности, богато украшенные здания и различные магазины.")

    def active_2(self):
        print("Решив отдохнуть, вы присаживаетесь на скамейку и достаете термос с чаем.")

    def active_3(self):
        print("Открыв свой блокнот, вы начинаете кропотливо описывать все что видите.")

    def active_4(self):
        print("Увидев ближайший магазинчик, вы отправляетесь туда в поисках сувениров.")