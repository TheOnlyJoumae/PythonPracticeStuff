import tarfile

#This file should contain the basis for all entities, players and enemies, that can be in combat.
#Warrior/Knight, Blackbelt/Master, Thief/Ninja, Black Mage/Black Wizard, White Mage/White Wizard, Red Mage/Red Wizard
class Entity:
    def __init__(self, name, level, maxHP, maxMP, actions ):
        self.name = name
        self.level = level
        self.maxHP = maxHP
        self.currentHP = maxHP
        self.maxMP = maxMP
        self.actions = ["Attack", "Items"] + actions

class WhiteMage(Entity):
    def __init__(self, name, level, maxHP, maxMP, actions):
        super().__init__(name, level, maxHP, maxMP, actions)

    def cure(self, target):
        target.currentHP = target.currentHP + 50

    def life(self, target):
        if target.currentHP < 1:
            target.currentHP = target.maxHP/2
        elif target.name == "Undead":
            target.currentHP = 0
        else: 
            return