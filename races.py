from character import Character


class Elf(Character):
    def __init__(self, name, char_class):
        super().__init__(name, "Elf", char_class)
        self.attributes['agility'] += 2
        self.equipment = ['Sandals of Impetuosity']

class Orc(Character):
    def __init__(self, name, char_class):
        super().__init__(name, "Orc", char_class)
        self.attributes['strength'] += 2
        self.equipment = ['Ham'] # окорок

class Undead(Character):
    def __init__(self, name, char_class):
        super().__init__(name, "Undead", char_class)
        self.attributes['wisdom'] += 2
        self.equipment = ["Shovel"] #сделай рандомную руну из списка рун который нужно попозже создать
        #способность разбирает себя по частям и пролезает в узкие места

class Fishman(Character):
    def __init__(self, name, char_class):
        super().__init__(name, "Fishman", char_class)
        self.attributes['intelligence'] += 2
        self.equipment = ["A minor healing Potion"]