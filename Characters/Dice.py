import random

class Dice:
    def __init__(self, sides):
        self.sides = sides

    def roll(self):
        """Бросок одного кубика."""
        return random.randint(1, self.sides)

    def roll_with_modifier(self, modifier=0):
        """Бросок кубика с добавлением модификатора."""
        result = self.roll()
        return result + modifier,result

    def roll_multiple(self, count=1, modifier=0):
        """
        Бросок кубика count раз и суммирование результатов с добавлением модификатора.
        Полезно, когда нужно бросать несколько кубиков одновременно (например, 2D6).
        """
        total = sum(self.roll() for _ in range(count))
        return total + modifier, total

    def roll_list(self, count=1):
        """
        Бросок кубика count раз и возвращение списка отдельных результатов.
        """
        return [self.roll() for _ in range(count)]

    def __repr__(self):
        return f"{self.__class__.__name__}(sides={self.sides})"


class D20(Dice):
    def __init__(self):
        super().__init__(sides=20)


class D6(Dice):
    def __init__(self):
        super().__init__(sides=6)


# Примеры использования
if __name__ == "__main__":
    d20 = D20()
    d6 = D6()

    print("Одиночный бросок D20:", d20.roll())
    print("Бросок D20 с модификатором +3:", d20.roll_with_modifier(3))

    print("Одиночный бросок D6:", d6.roll())
    print("Бросок D6 с модификатором +2:", d6.roll_with_modifier(2))

    # Множественные броски
    print("Суммарный результат 3 бросков D6 + 1 модификатор:", d6.roll_multiple(count=3, modifier=1))
    print("Список результатов 4 бросков D20:", d20.roll_list(count=4))
