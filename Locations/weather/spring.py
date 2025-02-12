from season import Season
from Characters import Character
from temp import Temperature


class Spring(Season):
    def __init__(self):
        super().__init__(name="Весна", description="Цветение, дождливая погода", season_effects=[])
        self.temperature = Temperature(min_temp=5, max_temp=20)

    def affect_environment(self, character: Character):
        """Влияние весны на окружающую среду и персонажей."""
        print("Весной цветут цветы и происходят дожди.")

        # Дождливая погода может влиять на персонажа
        if self.temperature.get_current_temperature() <= 10:
            print(f"Температура: {self.temperature.get_current_temperature()}°C. Дождливо и прохладно.")
            character.speed *= 0.95
            character.agility += 1
        else:
            print(f"Температура: {self.temperature.get_current_temperature()}°C. Комфортно для путешествий.")
            character.agility += 2

    def update_season(self):
        """Обновление температуры в весенний сезон."""
        self.temperature.update_temperature()
        self.temperature.affect_environment(self.character)
