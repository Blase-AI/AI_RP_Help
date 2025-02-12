from loc import Location
import random

class Forest(Location):
    def __init__(self, name="Лес", description="Тайное место, полное опасностей и приключений"):
        super().__init__(name, description)
        self.encounters = ["Дикий зверь", "Существа леса", "Природные аномалии"]

    def generate_encounter(self):
        encounter = random.choice(self.encounters)
        print(f"В лесу произошла встреча с: {encounter}.")