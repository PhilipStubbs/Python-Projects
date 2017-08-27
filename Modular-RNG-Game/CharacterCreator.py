import sqlite3
import random

class CharacterCreator(object):
    def __init__(self):
        # ==== Assblishes connection to a data base ====
        self.db = sqlite3.connect("Character.sqlite")
        # ==== Creates the required Tables in SQLite ====
        self.db.execute("CREATE TABLE IF NOT EXISTS inventory (type TEXT PRIMARY KEY NOT NULL, playeritem TEXT NOT NULL, stat INTEGER NOT NULL)")
        self.db.execute("CREATE TABLE IF NOT EXISTS playerstats(attr TEXT NOT NULL, playerstat INTEGER NOT NULL)")
        # ==== Dicts required for characters ====
        self.inventory = {"Melee Weapon": ("Basic Iron Sword", 2),
                          "Ranged Weapon": ("Wooden Long Bow", 1),
                          "Chest": ("Cloth shirt", 1),
                          "Pants": ("Cloth Pants", 1)}

        self.PlayerStats = {"Strength": int(random.randint(1, 20)),
                            "Health": (int(random.randint(7, 20)) * 10),
                            "Intelligence": int(random.randint(1, 20)),
                            "Dexterity": int(random.randint(1, 20)),
                            "Perception": int(random.randint(1, 20)),
                            }


    def CharacterReset(self):
        # ==== Character reset tab, or creator ====
        for i in self.inventory:
            item, itemstat = self.inventory[i]
            print(" {}, {} ,{}".format(i, item, itemstat))
            self.db.execute("INSERT OR REPLACE INTO inventory(type, playeritem, stat) VALUES (?, ? , ?)", (i, item, itemstat))
            self.db.commit()

        for s in self.PlayerStats:
            attrref = self.PlayerStats[s]
            print(" {} = {}".format(s, attrref))
            self.db.execute("INSERT OR REPLACE INTO playerstats(attr, playerstat) VALUES (?, ? )", (s, attrref))
            self.db.commit()




test = CharacterCreator()
test.CharacterReset()

