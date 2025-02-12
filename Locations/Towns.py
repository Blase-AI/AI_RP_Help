from loc import Location

class Town(Location):
    def __init__(self, name="Город", description="Место для начала приключений"):
        super().__init__(name, description)
        self.npc = []  # Список NPC, которые могут быть в городе

    def add_npc(self, npc):
        self.npc.append(npc)

    def list_npcs(self):
        print(f"В городе находятся следующие NPC:")
        for npc in self.npc:
            print(f"- {npc}")
