from loc import Location
import random

class Dungeon(Location):
    def __init__(self, name="Подземелье", description="Тёмное место, полное врагов и ловушек"):
        super().__init__(name, description)
        self.levels = random.randint(1, 10)  # Случайное количество уровней в подземелье

    def explore(self):
        print(f"Вы исследуете {self.name}, и находите {self.levels} уровней подземелий.")