import random

class Temperature:
    def __init__(self, min_temp=-30, max_temp=5, temp_type="cold"):
        """
        Инициализация температуры с диапазоном и типом.

        :param min_temp: Минимальная температура.
        :param max_temp: Максимальная температура.
        :param temp_type: Тип температуры ('cold', 'warm', 'hot').
        """
        self.temp_type = temp_type
        self.set_temperature_range(temp_type)
        self.current_temperature = random.randint(self.min_temp, self.max_temp)

    def set_temperature_range(self, temp_type):
        """Устанавливает диапазон температур в зависимости от типа погоды."""
        if temp_type == "cold":
            self.min_temp = -30
            self.max_temp = 5
        elif temp_type == "warm":
            self.min_temp = 10
            self.max_temp = 30
        elif temp_type == "hot":
            self.min_temp = 25
            self.max_temp = 45
        else:
            raise ValueError("Unknown temperature type. Use 'cold', 'warm', or 'hot'.")

    def get_current_temperature(self):
        """Возвращает текущую температуру."""
        return self.current_temperature

    def update_temperature(self):
        """Изменяет температуру в течение дня (случайным образом)."""
        change = random.randint(-5, 5)
        self.current_temperature = max(self.min_temp, min(self.current_temperature + change, self.max_temp))
        print(f"Температура изменилась на {change}°C. Текущая температура: {self.current_temperature}°C.")

    def affect_environment(self, character):
        """Применяет эффекты температуры к персонажу."""
        if self.temp_type == "cold":
            if self.current_temperature <= -10:
                print(f"Температура: {self.current_temperature}°C. Очень холодно! Персонажи двигаются медленнее.")
                character.speed *= 0.8
                character.health -= 1
            elif self.current_temperature <= 0:
                print(f"Температура: {self.current_temperature}°C. Холодно, но терпимо.")
                character.speed *= 0.9
            else:
                print(f"Температура: {self.current_temperature}°C. Прохладно, но комфортно.")

        elif self.temp_type == "warm":
            if self.current_temperature >= 35:
                print(f"Температура: {self.current_temperature}°C. Очень жарко! Персонажи начинают терять здоровье от перегрева.")
                character.health -= 1
                character.speed *= 0.7
            elif self.current_temperature >= 25:
                print(f"Температура: {self.current_temperature}°C. Тепло. Нужно пить воду.")
                character.speed *= 0.9

        elif self.temp_type == "hot":
            if self.current_temperature >= 40:
                print(f"Температура: {self.current_temperature}°C. Пекло! Персонажи теряют здоровье быстро.")
                character.health -= 1
                character.speed *= 0.6
            elif self.current_temperature >= 30:
                print(f"Температура: {self.current_temperature}°C. Очень жарко. Необходимо укрыться.")
                character.speed *= 0.8

