import AllDicts
import random

class LootAmour(object):
    def __init__(self):

        self.Amour_Itemchance = AllDicts.AmourGen[random.randint(0, 7)]
        self.AmourAdj_Chance = random.randint(1, 100)
        self.rarity_ItemChance = random.randint(1, 100)

    def ItemReturn(self):
        # ====== This section get the random int from self.rarity_ItemChance and gives it a string,
        # that is the rarity======
        if self.rarity_ItemChance <= 50:
            self.rarity_ItemChance = "common"

        elif self.rarity_ItemChance <= 85:
            self.rarity_ItemChance = "uncommon"

        elif self.rarity_ItemChance <= 95:
            self.rarity_ItemChance = "rare"

        elif self.rarity_ItemChance >= 96:
            self.rarity_ItemChance = "legendary"

        # ====== This section get the random int from self.adjectives_ItemChance and gives it a string,
        # that is the material type======
        if self.AmourAdj_Chance <= 50:
            self.AmourAdj_Chance = "Cloth"

        elif self.AmourAdj_Chance <= 75:
            self.AmourAdj_Chance = "Leather"

        elif self.AmourAdj_Chance <= 85:
            self.AmourAdj_Chance = "Chainmail"

        elif self.AmourAdj_Chance <= 95:
            self.AmourAdj_Chance = "Plate"

        elif self.AmourAdj_Chance >= 96:
            self.AmourAdj_Chance = "StormPlate"

        # ====== This section will take all the info and generate a piece of amour.======
        self.newDefence = AllDicts.Amouradj_Dict.get(self.AmourAdj_Chance) + AllDicts.rarity_Dict.get(
            self.rarity_ItemChance)
        self.newItem = rarity_ItemChance + " " + AmourAdj_Chance + " " + Amour_Itemchance
        print("you found a " + newItem + " ,It has {} Defence!".format(newDefence))
        # ====== Here I return the amour name and damage as a tuple.======
        return self.newItem, self.newDefence
