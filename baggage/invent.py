

class Inventory:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.items = []

    def add_item(self, item):
        """Добавление предмета в инвентарь."""
        if len(self.items) < self.capacity:
            self.items.append(item)
            print(f"Предмет {item.name} добавлен в инвентарь.")
        else:
            print("Инвентарь полон!")

    def remove_item(self, item):
        """Удаление предмета из инвентаря."""
        if item in self.items:
            self.items.remove(item)
            print(f"Предмет {item.name} удалён из инвентаря.")
        else:
            print("Предмет не найден в инвентаре.")

    def list_items(self):
        """Выводит все предметы в инвентаре."""
        if not self.items:
            print("Инвентарь пуст!")
        for item in self.items:
            print(item)
