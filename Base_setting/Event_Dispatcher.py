# Event_Dispatcher.py
import logging
from typing import Callable, Dict, List, Any

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class EventDispatcher:
    """
    Простая система событий, позволяющая:
      - подписываться на событие,
      - отписываться от события,
      - рассылать событие всем подписчикам.
    Каждый тип события определяется уникальным идентификатором (например, строкой).
    Обработчики (callback-функции) вызываются с именованными аргументами, переданными при отправке события.
    """
    def __init__(self) -> None:
        self._subscribers: Dict[str, List[Callable[..., None]]] = {}

    def subscribe(self, event_type: str, callback: Callable[..., None]) -> None:
        """
        Подписывается на событие event_type.

        :param event_type: Тип события (например, "LEVEL_UP").
        :param callback: Функция-обработчик, которая будет вызвана при рассылке события.
        """
        if event_type not in self._subscribers:
            self._subscribers[event_type] = []
        if callback not in self._subscribers[event_type]:
            self._subscribers[event_type].append(callback)
            logging.info(f"Подписан обработчик {callback.__name__} на событие {event_type}")

    def unsubscribe(self, event_type: str, callback: Callable[..., None]) -> None:
        """
        Отписывается от события event_type.

        :param event_type: Тип события.
        :param callback: Функция-обработчик, которую нужно удалить.
        """
        if event_type in self._subscribers:
            try:
                self._subscribers[event_type].remove(callback)
                logging.info(f"Обработчик {callback.__name__} отписан от события {event_type}")
            except ValueError:
                logging.warning(f"Обработчик {callback.__name__} не найден для события {event_type}")

    def dispatch(self, event_type: str, **kwargs: Any) -> None:
        """
        Рассылает событие event_type всем подписчикам, передавая дополнительные данные.

        :param event_type: Тип события.
        :param kwargs: Именованные аргументы, которые будут переданы каждому обработчику.
        """
        if event_type in self._subscribers:
            logging.info(f"Рассылка события {event_type} с параметрами {kwargs}")
            for callback in self._subscribers[event_type]:
                try:
                    callback(**kwargs)
                except Exception as e:
                    logging.error(f"Ошибка в обработчике {callback.__name__} при событии {event_type}: {e}")

    def clear(self, event_type: str = None) -> None:
        """
        Удаляет подписчиков.

        :param event_type: Если указан, удаляет подписчиков только для этого типа события.
                           Если не указан, очищает всех подписчиков.
        """
        if event_type is None:
            self._subscribers.clear()
            logging.info("Все подписчики удалены.")
        else:
            if event_type in self._subscribers:
                self._subscribers.pop(event_type)
                logging.info(f"Подписчики для события {event_type} удалены.")


# Пример использования:
if __name__ == "__main__":
    def on_level_up(owner, new_level):
        print(f"Событие: {owner.name} достиг уровня {new_level}!")

    dispatcher = EventDispatcher()
    dispatcher.subscribe("LEVEL_UP", on_level_up)

    # Пример вызова события с передачей данных
    class DummyCharacter:
        def __init__(self, name):
            self.name = name

    character = DummyCharacter("Thalor")
    dispatcher.dispatch("LEVEL_UP", owner=character, new_level=2)

    # Отписка и повторная рассылка
    dispatcher.unsubscribe("LEVEL_UP", on_level_up)
    dispatcher.dispatch("LEVEL_UP", owner=character, new_level=3)
