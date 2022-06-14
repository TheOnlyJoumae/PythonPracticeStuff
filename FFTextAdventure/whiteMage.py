import entity

player3 = entity.WhiteMage("Ib", 30, 500, 1000, ["Cure"])
player3.cure(player3)
print(player3.currentHP)