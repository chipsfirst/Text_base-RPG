class Character:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def password(self):
        return bin(int(self))


class Points:
    def __init__(self, strange, dexterity, constitution, intelligence, wisdom, charisma):
        self.strange = strange
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma

    def strange_up(strange):
        strange += 1
        return strange

    def dex_up(dexterity):
        dexterity += 1
        return dexterity

    def const_up(constitution):
        constitution += 1
        return constitution

    def intel_up(intelligence):
        intelligence += 1
        return intelligence

    def wisdom_up(wisdom):
        wisdom += 1
        return wisdom

    def charisma_up(charisma):
        charisma += 1
        return charisma


Inventory = []


