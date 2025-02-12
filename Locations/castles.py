# castle.py
from random import choice
from Characters import Character

class Castle:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.rooms = []
        self.enemies = []
        self.quests = []

    def add_room(self, room):
        """Добавление комнаты в замок."""
        self.rooms.append(room)

    def add_enemy(self, enemy):
        """Добавление врага в замок (враг - это персонаж)."""
        self.enemies.append(enemy)

    def room_access(self, room_name, character):
        """Проверка, доступна ли комната игроку."""
        room = next((r for r in self.rooms if r.name == room_name), None)
        if room:
            if room.accessible:
                return f"{character.name} может войти в {room_name}."
            else:
                return f"{room_name} закрыта для {character.name}."
        return f"Комната {room_name} не найдена."

    def encounter_enemy(self, character):
        """Вероятность встречи с врагом."""
        if self.enemies:
            enemy = choice(self.enemies)
            return f"{character.name} встретил врага: {enemy.name}!"
        return "Врагов нет в этом замке."

    def explore(self, character):
        """Исследование замка."""
        if not self.rooms:
            return "Замок пустой, нет комнат для исследования."
        room = choice(self.rooms)
        return f"{character.name} исследует {room.name}. {room.description}"

class Room:
    def __init__(self, name, description, accessible=True):
        self.name = name
        self.description = description
        self.accessible = accessible  # Доступность комнаты для игрока

