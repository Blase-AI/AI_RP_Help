from Characters import Character

class ExperienceSystem:
    def __init__(self, owner: Character, level=1, experience=0, exp_formula=None, on_level_up_callback=None):
        """
        owner: объект класса Character, которому принадлежит эта система опыта.
        level: начальный уровень.
        experience: начальное количество опыта.
        exp_formula: функция для расчёта требуемого опыта для следующего уровня.
                     По умолчанию используется формула: 135 * уровень.
        on_level_up_callback: callback-функция, вызываемая при повышении уровня.
                              Если не задана, выводится сообщение с именем персонажа и новым уровнем.
        """
        self.owner = owner
        self._level = level
        self._experience = experience
        self.exp_formula = exp_formula or (lambda lvl: 135 * lvl)
        self.on_level_up_callback = on_level_up_callback
        self._experience_to_next_level = self._calculate_experience_for_next_level()

    def _calculate_experience_for_next_level(self):
        """Рассчитывает необходимое количество опыта для следующего уровня."""
        return self.exp_formula(self._level)

    def add_experience(self, amount):
        """Добавление опыта персонажу. Если опыт превышает порог, происходит повышение уровня."""
        if amount < 0:
            raise ValueError("Нельзя добавить отрицательное количество опыта.")
        self._experience += amount
        while self._experience >= self._experience_to_next_level:
            self._experience -= self._experience_to_next_level
            self._level_up()

    def _level_up(self):
        """Повышение уровня персонажа и обновление необходимого опыта для следующего уровня."""
        self._level += 1
        # Если задан callback, вызываем его с передачей владельца и нового уровня
        if self.on_level_up_callback:
            self.on_level_up_callback(self.owner, self._level)
        else:
            print(f"Поздравляем, {self.owner.name}! Ваш уровень повышен до {self._level}!")
        self._experience_to_next_level = self._calculate_experience_for_next_level()

    @property
    def level(self):
        """Возвращает текущий уровень персонажа."""
        return self._level

    @property
    def experience(self):
        """Возвращает текущее количество опыта персонажа."""
        return self._experience

    @property
    def experience_to_next_level(self):
        """Возвращает количество опыта, необходимое для следующего уровня."""
        return self._experience_to_next_level

    @property
    def percentage_to_next_level(self):
        """Возвращает процент достижения следующего уровня."""
        return (self._experience / self._experience_to_next_level) * 100

    def __str__(self):
        return (f"{self.owner.name}: Уровень: {self.level}, "
                f"Опыт: {self.experience}/{self.experience_to_next_level} "
                f"({self.percentage_to_next_level:.2f}% до следующего уровня)")


