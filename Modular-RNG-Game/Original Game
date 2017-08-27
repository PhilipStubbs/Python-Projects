import random
import time

# ==== default player inventory ====
inventory = {"Melee Weapon": ("Basic Iron Sword", 5),
             "Ranged Weapon": ("Wooden Long Bow", 5),
             "Chest": ("Cloth shirt", 10),
             "Pants": ("Cloth Pants", 10)}

# ==== generates player stats ====
PlayerStats = {"strength": int(random.randint(1, 20)),
               "health": (int(random.randint(7, 20)) * 10),
               "Intelligence": int(random.randint(1, 20)),
               "Dexterity": int(random.randint(1, 20)),
               "Perception": int(random.randint(1, 20)),
               "Level": (1, 100)}

Level, ExperienceRequired = PlayerStats.get("Level")

maxhealing = PlayerStats.get('health')

# ==== prints player stats ====
for stat in PlayerStats:
    print("Your {} is".format(stat), PlayerStats[stat])

CommandList = ['Move on', 'Melee Weapon', 'Ranged Weapon', 'Chest', 'Pants', 'Hit', "heal", "Melee", "Ranged"]

# ==== prints commands ====
print("Your Commands are")
for cmds in CommandList:
    print("{} , ".format(cmds), end="")

userinput = input()
# ==== sets Monsters variables ====
TheMonster = None
MonsterHealth = None
MonsterDamage = None

# ==== Item Generator dicts and lists. ====
WeaponGen = ["Sword", "Club", "Quarterstaff", "Dagger", "Pike", "Recurve Bow", "Compound Bow", "Longbow", "Crossbows",
             "Javelin"]
adjectives = ["Iron", "Steel", "Demasicus Steel", "Magic", "Elemental", ]
rarity = ["common", "uncommon", "rare", "legendary"]

# ==== Each time a weapon is generated, a random value is given to the Key which is then used to augment the damage ====
adjectives_Dict = {"Iron": random.randint(1, 10),
                   "Steel": random.randint(5, 15),
                   "Damascus Steel": random.randint(10, 20),
                   "Magic": random.randint(15, 25),
                   "Elemental": random.randint(15, 50)}

rarity_Dict = {"common": random.randint(1, 10),
               "uncommon": random.randint(5, 15),
               "rare": random.randint(10, 20),
               "legendary": random.randint(15, 25)}


def lootWeapon():
    # ==== Weapon generator function. ====
    # ==== Pulls in the userinput, and sets up the random weapon values ====
    global userinput
    Weapon_Itemchance = WeaponGen[random.randint(0, 9)]
    adjectives_ItemChance = random.randint(1, 100)
    rarity_ItemChance = random.randint(1, 100)
    rarity_ItemChanceStr = None
    adjectives_ItemChanceStr = None

    # ====== This section get the random int from rarity_ItemChance and gives it a string,
    # that is the rarity======
    if rarity_ItemChance <= 50:
        rarity_ItemChanceStr = "common"

    elif rarity_ItemChance <= 85:
        rarity_ItemChanceStr = "uncommon"

    elif rarity_ItemChance <= 95:
        rarity_ItemChanceStr = "rare"

    elif rarity_ItemChance >= 96:
        rarity_ItemChanceStr = "legendary"

     # ====== This section get the random int from adjectives_ItemChance and gives it a string,
     # that is the Metal type======
    if adjectives_ItemChance <= 50:
        adjectives_ItemChanceStr = "Iron"

    elif adjectives_ItemChance <= 75:
        adjectives_ItemChanceStr = "Steel"

    elif adjectives_ItemChance <= 85:
        adjectives_ItemChanceStr = "Damascus Steel"

    elif adjectives_ItemChance <= 95:
        adjectives_ItemChanceStr = "Magic"

    elif adjectives_ItemChance >= 96:
        adjectives_ItemChanceStr = "Elemental"

    # ====== NewDamge, newItem are generated from the weapon. This is the Weapons total damage and full name======
    newDamage = adjectives_Dict.get(adjectives_ItemChanceStr) + rarity_Dict.get(rarity_ItemChanceStr)
    newItem = rarity_ItemChanceStr + " " + adjectives_ItemChanceStr + " " + Weapon_Itemchance
    print("you found a " + newItem + " ,It does {} Damage!".format(newDamage))
    # ==== The user is given the option to keep the weapon ====
    userinput = input("Do you want to keep the weapon? y/n, Your Current Melee and Ranged Damages are {}, {} ".format(
        inventory.get("Melee Weapon")[1], inventory.get("Ranged Weapon")[1]))

    # ==== If user inputs 'n' the weapon is discarded ====
    while True:
        if userinput == "n":
            if Weapon_Itemchance in WeaponGen[:4]:
                print("your Melee weapon is still your beloved {}".format(inventory["Melee Weapon"][0]))
                break
            else:
                print("your Ranged weapon is still your beloved {}".format(inventory["Ranged Weapon"][0]))
                break

        # ==== If user inputs 'y' inventory.Melee Weapon is updated with the new item ====
        elif userinput == "y":
            if Weapon_Itemchance in WeaponGen[:5]:
                inventory["Melee Weapon"] = newItem, (newDamage + PlayerStats.get("strength"))
                print("your Melee weapon is now the {} you just found!".format(newItem))
                break
            else:
                inventory["Ranged Weapon"] = newItem, (newDamage + PlayerStats.get("Dexterity"))
                print("Your Ranged Weapon is now the {} you just found!".format(newItem))
                break

        # ==== This will keep looping until the user inputs y, or n ====
        else:
            print("Please input y or n")

        userinput = input()


def BoolChance():
    # ==== This funtion generates a Yes or No for most of the actions ingame. If the attack hits, monster spawns
    # and so on ====
    changeA = random.randint(1, 101)
    changeB = random.randint(1, 101)

    # ==== This checks if one variable is bigger than the other, then returns True if it is. ====
    if changeA <= changeB:
        return True

    else:
        return False


def lootDrop():
    # ==== This funtion generates a Yes or No for a loot drop chance.====
    # ==== This funtion is the same as the BoolChance ====
    lootdecider = random.randint(1, 101)
    droprate = random.randint(1, 101)

    if lootdecider <= droprate:
        lootWeapon()

    elif lootdecider >= droprate:
        LootAmour()

    else:
        print("No loot for you!")


def LootAmour():
    # ==== Weapon generator function. ====
    # ==== Pulls in the userinput, and sets up the random weapon values ====
    AmourGen = ['Pants', 'Leggings', 'Gleaves', 'Fauld', 'Jacket', 'Shirt', 'Light Chest Piece', 'Heavy Chest Piece']
    AmourAdj_Chance_dict = ['Cloth', 'Plate', 'Chainmail', 'Leather', 'Shard Plate']
    Amouradj_Dict = {"Cloth": random.randint(1, 10),
                     "Leather": random.randint(5, 15),
                     "Chainmail": random.randint(10, 20),
                     "Plate": random.randint(15, 25),
                     "StormPlate": random.randint(15, 50)}

    Amour_Itemchance = AmourGen[random.randint(0, 7)]
    AmourAdj_Chance = random.randint(1, 100)
    rarity_ItemChance = random.randint(1, 100)
    rarity_ItemChanceStr = None
    AmourAdj_ChanceStr = None

    # ====== This section get the random int from rarity_ItemChance and gives it a string,
    # that is the rarity======
    if rarity_ItemChance <= 50:
        rarity_ItemChanceStr = "common"

    elif rarity_ItemChance <= 85:
        rarity_ItemChanceStr = "uncommon"

    elif rarity_ItemChance <= 95:
        rarity_ItemChanceStr = "rare"

    elif rarity_ItemChance >= 96:
        rarity_ItemChanceStr = "legendary"

    # ====== This section get the random int from adjectives_ItemChance and gives it a string,
    # that is the Material type======
    if AmourAdj_Chance <= 50:
        AmourAdj_ChanceStr = "Cloth"

    elif AmourAdj_Chance <= 75:
        AmourAdj_ChanceStr = "Leather"

    elif AmourAdj_Chance <= 85:
        AmourAdj_ChanceStr = "Chainmail"

    elif AmourAdj_Chance <= 95:
        AmourAdj_ChanceStr = "Plate"

    elif AmourAdj_Chance >= 96:
        AmourAdj_ChanceStr = "StormPlate"

    # ====== newDefence, newItem are generated from the weapon. This is the Amourtotal damage and full name======
    newDefence = Amouradj_Dict.get(AmourAdj_ChanceStr) + rarity_Dict.get(rarity_ItemChanceStr)
    newItem = rarity_ItemChanceStr + " " + AmourAdj_ChanceStr + " " + Amour_Itemchance
    print("you found a " + newItem + " ,It has {} Defence!".format(newDefence))
    # ==== The user is given the option to keep the amour ====
    userinput = input(
        "Do you want to keep the Amour? y/n, Your current Chest and Pants are {}, {}".format(inventory.get("Chest")[1],
                                                                                             inventory.get("Pants")[1]))
    # ==== If user inputs 'n' the weapon is discarded ====
    while True:
        if userinput == "n":
            if Amour_Itemchance in AmourGen[4:]:
                print("your Amour is still your beloved {}".format(inventory["Chest"][0]))
                break
            else:
                print("your Amour is still your beloved {}".format(inventory["Pants"][0]))
                break

                # ==== If user inputs 'y' inventory.Melee Weapon is updated with the new item ====
        elif userinput == "y":
            if Amour_Itemchance in AmourGen[4:]:
                inventory["Chest"] = newItem, newDefence
                print("your Chest Piece is now the {} you just found!".format(newItem))
                break
            else:
                inventory["Pants"] = newItem, newDefence
                print("Your Pants are now the {} you just found!".format(newItem))
                break
        else:
            print("Please input y or n")

        userinput = input()


def LocGen():
    # ==== Here I generate the location====
    locations = ['Desert', 'Bridge', 'Hills', 'Forrest', "Town", "City", "Abandoned house"]
    adjLoc = ["Spooky", "windy", "Barron", "Stormy", "Dark"]
    # ==== Random values given for the index of the lists above which will generate the location====
    Locchance = random.randint(0, 6)
    adjLoc_Chance = random.randint(0, 4)
    rarity_ItemChance = random.randint(0, 3)
    # ==== Adds all the above variables ====
    TheLocation = rarity[rarity_ItemChance] + " " + adjLoc[adjLoc_Chance] + " " + locations[Locchance]
    print(TheLocation)


def MonsterGen():
    # ==== This will generate the Monsters====
    # ==== Pull in the global variables for later use====
    global MonsterHealth
    global MonsterDamage
    global TheMonster

    # ==== generates the monsters stats and name====
    Monster_Dict = {"Bandit": (random.randint(1, 100), random.randint(10, 20)),
                    "Orc": (random.randint(40, 100), random.randint(15, 25)),
                    "Ghost": (random.randint(20, 50), random.randint(25, 30)),
                    "Demon": (random.randint(100, 200), random.randint(15, 50)),
                    "Wolf": (random.randint(15, 50), random.randint(5, 20)),
                    "Bear": (random.randint(15, 50), random.randint(5, 20)),
                    "Cthulu": (random.randint(100, 400), random.randint(25, 100))}
    # ==== generates the monsters adjective and more stats====
    adjectives_Dict = {"Whimpy": (random.randint(1, 10), random.randint(1, 10)),
                       "Friendly": (random.randint(5, 15), random.randint(1, 10)),
                       "Tough": (random.randint(10, 20), random.randint(1, 10)),
                       "Scary": (random.randint(15, 25), random.randint(1, 10)),
                       "Deadly": (random.randint(15, 50), random.randint(1, 10))}

    MonsterTypes = ["Bandit", "Orc", "Ghost", "Demon", "Wolf", "Bear", "Cthulu"]
    AdjMonster = ["Whimpy", "Friendly", "Tough", "Scary", "Deadly"]

    MonsterTypesChance = random.randint(0, 101)
    AdjMonsterChance = random.randint(0, 101)
    MonsterTypesChanceStr = None
    AdjMonsterChanceStr = None
    Monster = AdjMonsterChance + MonsterTypesChance

    # ====== This section get the random int from MonsterTypesChance and gives it a string,
    # that is the Type======

    if MonsterTypesChance <= 10:
        MonsterTypesChanceStr = "Bear"

    elif MonsterTypesChance <= 20:
        MonsterTypesChanceStr = "Wolf"

    elif MonsterTypesChance <= 40:
        MonsterTypesChanceStr = "Bandit"

    elif MonsterTypesChance <= 60:
        MonsterTypesChanceStr = "Orc"

    elif MonsterTypesChance <= 70:
        MonsterTypesChanceStr = "Ghost"

    elif MonsterTypesChance <= 96:
        MonsterTypesChanceStr = "Demon"

    elif MonsterTypesChance >= 97:
        MonsterTypesChanceStr = "Cthulu"

    # ====== This section get the random int from AdjMonsterChance and gives it a string,
    # that is the personality======

    if AdjMonsterChance <= 30:
        AdjMonsterChanceStr = "Whimpy"

    elif AdjMonsterChance <= 40:
        AdjMonsterChanceStr = "Friendly"

    elif AdjMonsterChance <= 60:
        AdjMonsterChanceStr = "Tough"

    elif AdjMonsterChance <= 89:
        AdjMonsterChanceStr = "Scary"

    elif AdjMonsterChance >= 90:
        AdjMonsterChanceStr = "Deadly"

    # ====== MonsterHealth, MonsterDamage  are generated from the weapon.
    # This is the Monsters total damage and full name======
    MonsterHealth, MonsterDamage = Monster_Dict.get(MonsterTypesChanceStr)
    TheMonster = AdjMonsterChanceStr + ' ' + MonsterTypesChanceStr
    AdjHeath, AdjDamage = adjectives_Dict.get(AdjMonsterChanceStr)
    MonsterHealth += AdjHeath
    MonsterDamage += AdjDamage

    print(
        "You are faced with a {} it has {} Heath and does {} Damage!".format(TheMonster, MonsterHealth, MonsterDamage))


while True:
    # ==== This section takes everything and puts it into a game====
    MeleeWeapon, Meleedamage = inventory.get('Melee Weapon')
    RangedWeapon, Rangeddamage = inventory.get('Ranged Weapon')
    defence = round((inventory.get("Chest")[1] + inventory.get("Pants")[1]) / 2)
    # ==== Sets up the quit command====
    if userinput.lower() == "quit":
        break

    # ==== Sets up player death====
    elif PlayerStats.get("health") <= 0:
        print("You Died")
        break

    # ==== These new few are cheat command, meant to be used by me====
    elif userinput.lower() == "more loot":
        lootDrop()

    elif userinput.lower() == "monster":
        MonsterGen()

    elif userinput.lower() == "more a":
        LootAmour()

    # ==== Sets up check inventory command====
    elif userinput.lower() == "inventory":
        for i in inventory:
            print(i)

    elif userinput.lower() == "defence":
        print(defence)

    elif userinput in inventory:
        item, stat = inventory.get(userinput)
        if userinput == "Ranged Weapon" or item == "Melee Weapon":
            print("your {} is a {} with {} damage".format(userinput, item, stat))
        else:
            print("your {} is a {} with {}".format(userinput, item, stat))

    # ==== Sets up Death command====
    elif userinput.lower() == "kill":
        PlayerStats["health"] -= PlayerStats.get("health")

    # ==== Sets up Heal command====
    elif userinput.lower() == "heal":
        if BoolChance() == True:
            PlayerStats['health'] = maxhealing
            print("You are fully healed!!")

        else:
            print("You could not be healed!")

    # ==== Sets up Move on command====
    elif userinput.lower() == "move on":
        LocGen()
        # ==== Checks if a monster is going to spawn====
        if BoolChance() == True:

            time.sleep(.5)
            MonsterGen()
            time.sleep(.5)
            monstername = TheMonster
            # ====if monster spawns this starts combat====
            while True:
                # ==== User picks a weapon====
                userinput = input(
                    "Pick a weapon to attack with or Run: Melee {} damage or Ranged {} damage ".format(Meleedamage,
                                                                                                       Rangeddamage))
                if userinput.lower() == "melee":

                    if BoolChance() == True:
                        # ==== Checks if the melee attack hit, if so the monster takes damage====
                        MonsterHealth -= Meleedamage
                        time.sleep(.5)
                        print("You Hit for {} Damage, The {} has {} Health Left".format(Meleedamage, TheMonster,
                                                                                        MonsterHealth))
                    else:
                        # ==== If attack misses ====
                        time.sleep(.5)
                        print("You missed!")

                        # ====Checks monsters health ====
                    if MonsterHealth <= 0:
                        time.sleep(0.5)
                        print("You have defeated the {}".format(monstername))
                        time.sleep(0.5)
                        if BoolChance() == True:
                            lootDrop()
                        break
                        # ==== If the user wants to run====
                    elif userinput.lower() == "run":
                        if BoolChance() == True:
                            # ==== Checks if user can run====
                            time.sleep(.5)
                            print('You Ran Away!')
                            break

                        else:
                            time.sleep(.5)
                            print("You could not run away!")

                    # ==== Checks if the Users is still alive====
                    elif PlayerStats.get("health") <= 0:
                        time.sleep(.5)
                        print("You Died!")
                        break

                if userinput.lower() == "ranged":


                    if BoolChance() == True:
                        # ==== Checks if the ranged attack hit, if so the monster takes damage====
                        MonsterHealth -= Rangeddamage
                        time.sleep(.5)
                        print("You Hit for {} Damage, {} has {} Health Left".format(Rangeddamage, TheMonster,
                                                                                    MonsterHealth))
                    else:
                        # ==== If attack misses ====
                        time.sleep(.5)
                        print("You missed!")

                    if BoolChance() == True:
                        # ====Checks if the monster does hit and if it can damage the player ====
                        if (MonsterDamage - defence) <= 0:
                            print("The {} does no damage!".format(TheMonster))
                            pass
                        else:
                            PlayerStats['health'] -= (MonsterDamage - defence)
                            time.sleep(0.5)
                            print("The {} has hit you for {} damage! You have {} Health left!".format(TheMonster,
                                                                                                      MonsterDamage - defence,
                                                                                                      PlayerStats.get(
                                                                                                          "health")))
                    # ====Checks monsters health ====
                    if MonsterHealth <= 0:
                        time.sleep(0.5)
                        print("You have defeated the {}".format(monstername))
                        time.sleep(0.5)
                        if BoolChance() == True:
                            lootDrop()
                        break

                    # ====Checks Players health ====
                    elif PlayerStats.get("health") <= 0:
                        time.sleep(.5)
                        print("You Died!")
                        break

                if BoolChance() == True:
                    if (MonsterDamage - defence) <= 0:
                        print("The {} does no damage!".format(TheMonster))
                        pass
                    else:
                        PlayerStats['health'] -= (MonsterDamage - defence)
                        time.sleep(0.5)
                        print("The {} has hit you for {} damage! You have {} Health left!".format(TheMonster,
                                                                                                  MonsterDamage - defence,
                                                                                                  PlayerStats.get(
                                                                                                      "health")))

                if userinput.lower() == "run":
                    # ====Checks if player can run====
                    if BoolChance() == True:
                        time.sleep(.5)
                        print("You were able to run! Move on to continue")
                        break

                    else:
                        time.sleep(.5)
                        print("You couldn't escape!")

        else:
            time.sleep(.5)
            print("No Monsters Here!")
            if BoolChance() == True:
                lootDrop()

    # ====Checks if unknown command is entered====
    else:
        print("Unknown Command, please try again, your commands are as followed")
        for i in CommandList:
            print(i)

    userinput = input()


