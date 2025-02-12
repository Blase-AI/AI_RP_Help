import random


class Snow:
    def __init__(self):
        self.name = "Снег"
        self.description = "Мелкий снегопад, который покрывает землю слоем снега."
        self.movement_penalty = 0.15  # Понижение скорости движения на 15%
        self.visibility_penalty = 0.3  # Понижение видимости на 30%

    def affect_environment(self, character):
        """Применяет эффекты снега к окружению и персонажу."""
        print(f"{self.name}: {self.description}")
        print(
            f"Из-за снега, персонажи двигаются медленнее на {self.movement_penalty * 100}% и видимость снижена на {self.visibility_penalty * 100}%.")

        # Влияние на скорость персонажа
        character.speed *= (1 - self.movement_penalty)
        character.visibility *= (1 - self.visibility_penalty)

        # Возможность случайных событий (например, снежная буря)
        if random.random() < 0.1:  # 10% шанс на случайное событие
            self.random_snow_event(character)

    def random_snow_event(self, character):
        """Случайное событие во время снега (например, снежная буря)."""
        events = ["Снежная буря начинается, видимость ухудшается!",
                  "Лавина разрушает ближайшую тропу!",
                  "Персонаж получает лёгкую обморожение."]

        event = random.choice(events)
        print(f"Случайное событие: {event}")

        # Применяем эффект на персонажа, например, обморожение
        if event == "Персонаж получает лёгкую обморожение.":
            character.health -= 10  # Уменьшаем здоровье персонажа

