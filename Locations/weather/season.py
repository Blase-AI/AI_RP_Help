
class Season:
    def __init__(self, name, description, season_effects=None):
        self.name = name
        self.description = description
        self.season_effects = season_effects if season_effects else []

    def __str__(self):
        return f"{self.name}: {self.description}"

    def affect_environment(self):
        """Метод, который применяет сезонные эффекты."""
        for effect in self.season_effects:
            effect.affect_environment()
