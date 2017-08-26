import random
import AllDicts

class LootWeapon(object):
    def __init__(self):

        self.Weapon_Itemchance = AllDicts.WeaponGen[random.randint(0, 9)]
        self.adjectives_ItemChance = random.randint(1, 100)
        self.rarity_ItemChance = random.randint(1, 100)
        self.rarity_ItemChanceStr = None
        self.adjectives_ItemChanceStr = None

    def ItemReturn(self):
        # ====== This section get the random int from self.rarity_ItemChance and gives it a string,
        # that is the rarity======
        if self.rarity_ItemChance <= 50:
            self.rarity_ItemChanceStr = "common"

        elif self.rarity_ItemChance <= 85:
            self.rarity_ItemChanceStr = "uncommon"

        elif self.rarity_ItemChance <= 95:
            self.rarity_ItemChanceStr = "rare"

        elif self.rarity_ItemChance >= 96:
            self.rarity_ItemChanceStr = "legendary"

        # ====== This section get the random int from self.adjectives_ItemChance and gives it a string,
        # that is the Metal type======
        if self.adjectives_ItemChance <= 50:
            self.adjectives_ItemChanceStr = "Iron"

        elif self.adjectives_ItemChance <= 75:
            self.adjectives_ItemChanceStr = "Steel"

        elif self.adjectives_ItemChance <= 85:
            self.adjectives_ItemChanceStr = "Damascus Steel"

        elif self.adjectives_ItemChance <= 95:
            self.adjectives_ItemChanceStr = "Magic"

        elif self.adjectives_ItemChance >= 96:
            self.adjectives_ItemChanceStr = "Elemental"

        # ====== This section will take all the info and generate a weapon.======
        self.newDamage = AllDicts.adjectives_Dict.get(self.adjectives_ItemChanceStr) + AllDicts.rarity_Dict.get(self.rarity_ItemChanceStr)
        self.newItem = self.rarity_ItemChanceStr + " " + self.adjectives_ItemChanceStr + " " + self.Weapon_Itemchance
        print("you found a " + self.newItem + " ,It does {} Damage!".format(self.newDamage))
        # ====== Here I return the weapon name and damage as a tuple.======
        return self.newItem, self.newDamage
