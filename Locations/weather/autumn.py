from season import Season
from Characters import Character
from temp import Temperature

class Autumn(Season):
    def __init__(self):
        super().__init__(name="Осень", description="Листья падают, холоднее", season_effects=[])
        self.temperature = Temperature(min_temp=0, max_temp=15)

    def affect_environment(self, character: Character):
        """Влияние осени на окружающую среду и персонажей."""
        print("Осенью трава становится скользкой из-за выпавших листьев.")

        if self.temperature.get_current_temperature() <= 5:
            print(f"Температура: {self.temperature.get_current_temperature()}°C. Холодно, листья покрывают землю.")
            character.speed *= 0.85
            character.agility -= 1
        else:
            print(f"Температура: {self.temperature.get_current_temperature()}°C. Прохладно, но легко двигаться.")
            character.agility += 1

    def update_season(self):
        """Обновление температуры в осенний сезон."""
        self.temperature.update_temperature()
        self.temperature.affect_environment(self.character)
