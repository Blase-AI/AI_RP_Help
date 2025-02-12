

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def enter(self):
        """Метод, который срабатывает при входе в локацию."""
        print(f"Вы вошли в {self.name}. {self.description}")