from Characters import Character

class Warrior(Character):
    def __init__(self, name, race):
        super().__init__(name, race, "Warrior")
        self.attributes['strength'] += 2.9
        self.equipment.extend(['Sword', 'Shield', 'Heavy Armor'])

class Mage(Character):
    def __init__(self, name, race):
        super().__init__(name, race, "Mage")
        self.attributes['wisdom'] += 3
        self.equipment.extend(['Staff', 'Mana Ring', 'Spellbook'])

class Paladin(Character):
    def __init__(self, name, race):
        super().__init__(name, race, "Paladin")
        self.attributes['strength'] += 2.1
        self.attributes['wisdom'] += 0.2
        self.equipment.extend(['Hammer', 'Heavy Armor', 'The Book of Forgiveness'])
#Вор
class Thief(Character):
    def __init__(self, name, race):
        super().__init__(name, race, "Thief")
        self.attributes['agility'] += 1.9
        self.attributes['charisma'] += 0.8
        self.equipment.extend(['Hammer', 'Heavy Armor', 'The Book of Forgiveness'])