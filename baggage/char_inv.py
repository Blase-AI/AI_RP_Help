from Characters import Character
from invent import Inventory
from EquipableItem import EquipableItem
from Base_setting.Event_Dispatcher import EventDispatcher


class CharacterWithInventory(Character):
    def __init__(self, name, race, char_class):
        super().__init__(name, race, char_class)
        self.inventory = Inventory()  # Добавляем инвентарь как атрибут персонажа
        self.event_dispatcher = EventDispatcher()  # Создаем экземпляр диспетчера событий

    def add_to_inventory(self, item):
        """Добавление предмета в инвентарь."""
        self.inventory.add_item(item)
        # Генерация события
        self.event_dispatcher.dispatch("ITEM_ADDED", owner=self, item=item)

    def remove_from_inventory(self, item):
        """Удаление предмета из инвентаря."""
        self.inventory.remove_item(item)
        # Генерация события
        self.event_dispatcher.dispatch("ITEM_REMOVED", owner=self, item=item)

    def list_inventory(self):
        """Вывод всех предметов в инвентаре."""
        self.inventory.list_items()

    def equip_item(self, item):
        """Экипировка предмета."""
        if isinstance(item, EquipableItem):
            item.equip(self)
            # Генерация события экипировки
            self.event_dispatcher.dispatch("ITEM_EQUIPPED", owner=self, item=item)
        else:
            print(f"{item.name} не является экипируемым предметом.")


