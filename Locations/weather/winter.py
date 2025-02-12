from season import Season
from snow import Snow
from temp import Temperature

class Winter(Season):
    def __init__(self):
        effects = [Snow()]

        self.temperature = Temperature(min_temp=-25, max_temp=8, temp_type="cold")
        super().__init__(name="Зима", description="Снежные холода и морозы", season_effects=effects)

    def update_season(self):
        """Обновление сезона с учетом изменений температуры."""
        self.temperature.update_temperature()
        self.temperature.affect_environment(self.character)

