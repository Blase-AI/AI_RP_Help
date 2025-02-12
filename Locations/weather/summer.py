from season import Season
from temp import Temperature
from Characters import Character

class Summer(Season):
    def __init__(self):
        self.temperature = Temperature(min_temp=20, max_temp=40, temp_type="hot")
        super().__init__(name="Лето", description="Жаркие дни, зелень вокруг", season_effects=[])

    def affect_environment(self, character: Character):
        """Влияние лета на окружающую среду и персонажей."""
        print("Летняя жара влияет на выносливость персонажей.")
        if self.temperature.get_current_temperature() >= 30:
            print(
                f"Температура: {self.temperature.get_current_temperature()}°C. Персонажи начинают чувствовать усталость.")
            character.speed *= 0.9
            character.agility -= 2

        # Дополнительно можно добавлять другие эффекты, например:
        # - Растущая жара может вызывать жажду, снижение здоровья и т.д.

    def update_season(self):
        """Обновление температуры в летний сезон."""
        self.temperature.update_temperature()
        self.temperature.affect_environment(self.character)
