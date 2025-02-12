import random

class Character:
    def __init__(self, name, race, char_class):
        self.name = name
        self.race = race
        self.char_class = char_class
        self.level = 1
        self.experience = 0
        self.attributes = self.generate_attributes()
        self.skills = self.generate_skills()
        self.equipment = self.generate_equipment()
        self.history = None  # История будет добавляться отдельно

    def generate_equipment(self):
        return []
    def generate_attributes(self):
        # Генерация случайных атрибутов
        return {
            'strength': random.randint(3, 18),
            'agility': random.randint(3, 18),
            'constitution': random.randint(3, 18),
            'intelligence': random.randint(3, 18),
            'wisdom': random.randint(3, 18),
            'charisma': random.randint(3, 18)
        }

    def generate_skills(self):
        # Список навыков
        return {
            'power': random.randint(1, 5),
            #'agility': random.randint(1,5),
            'arcana': random.randint(1, 5),
            'persuasion': random.randint(1, 5), # убеждение
            'stealth': random.randint(1, 5) # хитрость
        }

    def level_up(self):
        self.level += 1
        self.experience = 0
        self.attributes['strength'] += random.randint(1, 2)
        self.attributes['dexterity'] += random.randint(1, 2)
        self.attributes['constitution'] += random.randint(1, 2)

    def display_stats(self):
        # Отображение текущих характеристик персонажа
        stats = f"Name: {self.name}\n"
        stats += f"Race: {self.race}\n"
        stats += f"Class: {self.char_class}\n"
        stats += f"Level: {self.level}\n"
        stats += f"Experience: {self.experience}\n"
        stats += f"Attributes: {self.attributes}\n"
        stats += f"Skills: {self.skills}\n"
        stats += f"Equipment: {self.equipment}\n"
        stats += f"History: {self.history if self.history else 'No history'}"
        return stats

    def __str__(self):
        return f"{self.name}, the {self.race} {self.char_class}"


