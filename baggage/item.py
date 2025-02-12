

class Item:
    def __init__(self, name, weight, description=""):
        self.name = name
        self.weight = weight
        self.description = description

    def __repr__(self):
        return f"{self.name} (Вес: {self.weight} кг)"

