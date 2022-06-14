class Entity:
    def __init__(self, name, level, maxHP, maxMP, actions ):
        self.name = name
        self.level = level
        self.maxHP = maxHP
        self.currentHP = maxHP
        self.maxMP = maxMP
        self.actions = ["Attack"] + actions

class WhiteMage(Entity):
    def __init__(self, name, level, maxHP, maxMP, actions):
        super().__init__(name, level, maxHP, maxMP, actions)

    def cure(target):
        target.currentHP = target.currentHP + 50

player3 = WhiteMage("Ib", 30, 500, 1000, ["Cure"])
player3.cure(player3)
print(player3.currentHP)