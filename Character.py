class Character:
    def __init__(self, name, age, location):
        self.name = name
        self.age = age
        self.location = location

    def password(self):
        return bin(int(self))