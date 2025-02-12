from Characters import Character
from Dice import Dice, D6, D20

class CharacterWithDice(Character):
    def __init__(self, name, race, char_class):
        super().__init__(name, race, char_class)

    def roll_attack(self, skill='power'):
        """
        Бросок атаки.
        Используется D20. Если натуральный результат равен 20, то критический успех,
        если 1 – критический провал.
        """
        dice = D20()
        modifier = self.skills.get(skill, 0)
        total, raw = dice.roll_with_modifier(modifier)
        if raw == 20:
            return f"Критический успех! (Натуральный: {raw}, Модификатор: {modifier}, Итог: {total})"
        elif raw == 1:
            return f"Критическая неудача! (Натуральный: {raw}, Модификатор: {modifier}, Итог: {total})"
        else:
            return f"Результат атаки: {total} (Натуральный: {raw}, Модификатор: {modifier})"

    def check_skill(self, skill):
        """
        Проверка навыка с D20.
        При натуральном 20 – критический успех, при натуральном 1 – критическая неудача.
        Используется порог успеха (например, 15) для определения результата.
        """
        dice = D20()
        modifier = self.skills.get(skill, 0)
        total, raw = dice.roll_with_modifier(modifier)
        success_threshold = 15  # Порог для успеха
        outcome = "Успех" if total >= success_threshold else "Неудача"
        if raw == 20:
            outcome = "Критический успех"
        elif raw == 1:
            outcome = "Критическая неудача"
        return f"{outcome}! Результат: {total} (Натуральный: {raw}, Модификатор: {modifier})"

    def roll_dice_notation(self, notation, modifier=0):
        """
        Обработка записи типа "2D6", где 2 — количество кубиков, D6 — тип кубика.
        Возвращает итоговую сумму бросков с модификатором и список отдельных результатов.
        """
        try:
            count, die = notation.upper().split("D")
            count = int(count)
            sides = int(die)
        except Exception as e:
            raise ValueError(f"Неверная нотация кубиков: {notation}") from e

        dice = Dice(sides)
        total, rolls = dice.roll_multiple(count, modifier)
        return total, rolls

    def roll_damage(self, damage_type='D6'):
        """
        Бросок урона.
        По умолчанию используется D6, но можно указать другой тип (например, D20).
        """
        if damage_type.upper() == 'D6':
            dice = D6()
        elif damage_type.upper() == 'D20':
            dice = D20()
        else:
            dice = Dice(int(damage_type[1:]))
        damage = dice.roll()
        return f"Нанесено урона: {damage}"
