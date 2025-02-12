from item import Item

class EquipableItem(Item):
    def __init__(self, name, weight, description, equip_type):
        super().__init__(name, weight, description)
        self.equip_type = equip_type

    def equip(self, character):
        """Одеваем предмет на персонажа."""
        print(f"{character.name} экипировал {self.name} как {self.equip_type}.")
