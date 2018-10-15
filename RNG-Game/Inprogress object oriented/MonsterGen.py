import random
import AllDicts
class MonsterGen(object):
    def __init__(self):

        self.MonsterTypes = ["Bandit", "Orc", "Ghost", "Demon", "Wolf", "Bear", "Cthulhu"]
        self.AdjMonster = ["Whimpy", "Friendly", "Tough", "Scary", "Deadly"]

        self.MonsterTypesChance = random.randint(0, 101)
        self.AdjMonsterChance = random.randint(0, 101)
        self.Monster = self.AdjMonsterChance + self.MonsterTypesChance
        self.MonsterTypesChanceStr = None
        self.AdjMonsterChanceStr = None

    def MonsterReturn(self):

        # ====== This section get the random int from self.MonsterTypesChance and gives it a string,
        # that is the Monster type======
        if self.MonsterTypesChance <= 10:
            self.MonsterTypesChanceStr = "Bear"

        elif self.MonsterTypesChance <= 20:
            self.MonsterTypesChanceStr = "Wolf"

        elif self.MonsterTypesChance <= 40:
            self.MonsterTypesChanceStr = "Bandit"

        elif self.MonsterTypesChance <= 60:
            self.MonsterTypesChanceStr = "Orc"

        elif self.MonsterTypesChance <= 70:
            self.MonsterTypesChanceStr = "Ghost"

        elif self.MonsterTypesChance <= 96:
            self.MonsterTypesChanceStr = "Demon"

        elif self.MonsterTypesChance >= 97:
            self.MonsterTypesChanceStr = "Cthulhu"

        # ====== This section get the random int from self.AdjMonsterChance and gives it a string,
        # that is the rarity======
        if self.AdjMonsterChance <= 30:
            self.AdjMonsterChanceStr = "Whimpy"

        elif self.AdjMonsterChance <= 40:
            self.AdjMonsterChanceStr = "Friendly"

        elif self.AdjMonsterChance <= 60:
            self.AdjMonsterChanceStr = "Tough"

        elif self.AdjMonsterChance <= 89:
            self.AdjMonsterChanceStr = "Scary"

        elif self.AdjMonsterChance >= 90:
            self.AdjMonsterChanceStr = "Deadly"

        # ====== This section will take all the info and generate a weapon.======
        self.MonsterHealth, self.MonsterDamage = AllDicts.Monster_Dict.get(self.MonsterTypesChanceStr)
        self.TheMonster = self.AdjMonsterChanceStr + ' ' + self.MonsterTypesChanceStr
        self.AdjHeath, self.AdjDamage = AllDicts.Monster_adjectives_Dict.get(self.AdjMonsterChanceStr)
        self.MonsterHealth += self.AdjHeath
        self.MonsterDamage += self.AdjDamage
        print("You are faced with a {} it has {} Heath and does {} Damage!".format(self.TheMonster, self.MonsterHealth,
                                                                                   self.MonsterDamage))
        # ====== Here I return the monster name and damage and health as a tuple.======
        return self.TheMonster, self.MonsterDamage, self.MonsterHealth
