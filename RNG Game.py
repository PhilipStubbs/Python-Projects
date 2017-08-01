import random
import time
# Player Stats Generater
inventory = {"Weak healing potion": "20 health over 30 seconds",
             "Melee Weapon": ("Basic Iron Sword", 5),
             "Ranged Weapon": ("Wooden Long Bow", 5),
             "Chest": ("Cloth shirt", 10),
             "Pants": ("Cloth Pants", 10)}

CommandList = ['Move on', 'Melee Weapon', 'Ranged Weapon', 'Chest', 'Pants', 'Hit', "heal", "Melee", "Ranged"]

PlayerStats = {"strength": int(random.randint(1, 20)),
               "health": (int(random.randint(7, 20))*10),
               "Intelligence": int(random.randint(1, 20)),
               "Dexterity": int(random.randint(1, 20)),
               "Perception": int(random.randint(1, 20)),
               "Level": (1, 100)}

Level, ExperienceRequired = PlayerStats.get("Level")

maxhealing = PlayerStats.get('health')

for stat in PlayerStats:
    print("Your {} is".format(stat), PlayerStats[stat])

print("Your Commands are")
for cmds in CommandList:
    print("{} , ".format(cmds), end="")

userinput = input()

TheMonster = ""
MonsterHealth = 0
MonsterDamage = 0

#Item Generator

WeaponGen = ["Sword", "Club", "Quarterstaff", "Dagger", "Pike", "Recurve Bow", "Compound Bow", "Longbow", "Crossbows", "Javelin"]
adjectives = ["Iron", "Steel", "Demasicus Steel", "Magic", "Elemental", ]
rarity = ["common", "uncommon", "rare", "legendary"]

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


    global userinput
    Weapon_Itemchance = WeaponGen[random.randint(0, 9)]
    adjectives_ItemChance = random.randint(1, 100)
    rarity_ItemChance = random.randint(1, 100)

    if rarity_ItemChance <= 50:
        rarity_ItemChance = "common"

    elif rarity_ItemChance <= 85:
        rarity_ItemChance = "uncommon"

    elif rarity_ItemChance <= 95:
        rarity_ItemChance = "rare"

    elif rarity_ItemChance >= 96:
        rarity_ItemChance = "legendary"


    if adjectives_ItemChance <= 50:
        adjectives_ItemChance = "Iron"

    elif adjectives_ItemChance <= 75:
        adjectives_ItemChance = "Steel"

    elif adjectives_ItemChance <= 85:
        adjectives_ItemChance = "Damascus Steel"

    elif adjectives_ItemChance <= 95:
        adjectives_ItemChance = "Magic"

    elif adjectives_ItemChance >= 96:
        adjectives_ItemChance = "Elemental"

    newDamage = adjectives_Dict.get(adjectives_ItemChance) + rarity_Dict.get(rarity_ItemChance)

    newItem = rarity_ItemChance  + " " +  adjectives_ItemChance + " " + Weapon_Itemchance
    print("you found a " + newItem + " ,It does {} Damage!".format(newDamage))

    userinput = input("Do you want to keep the weapon? y/n, Your Current Melee and Ranged Damages are {}, {} ".format(inventory.get("Melee Weapon")[1], inventory.get("Ranged Weapon")[1]))

    while True:
        if userinput == "n":
            if Weapon_Itemchance in WeaponGen[:4]:
                print("your Melee weapon is still your beloved {}".format(inventory["Melee Weapon"][0]))
                break
            else:
                print("your Ranged weapon is still your beloved {}".format(inventory["Ranged Weapon"][0]))
                break


        elif userinput == "y":
            if Weapon_Itemchance in WeaponGen[:5]:
                inventory["Melee Weapon"] = newItem, (newDamage + PlayerStats.get("strength"))
                print("your Melee weapon is now the {} you just found!".format(newItem))
                break
            else:
                inventory["Ranged Weapon"] = newItem, (newDamage + PlayerStats.get("Dexterity"))
                print("Your Ranged Weapon is now the {} you just found!".format(newItem))
                break

        else:
            print("Please input y or n")

        userinput = input()


def BoolChance():
    changeA = random.randint(1,101)
    changeB = random.randint(1,101)

    if changeA <= changeB:
        return True

    else:
        return False


def lootDrop():
    lootdecider = random.randint(1,101)
    droprate = random.randint(1,101)

    if lootdecider <= droprate:
        lootWeapon()

    elif lootdecider >= droprate:
        LootAmour()

    else:
        print("No loot for you!")


def LootAmour():
    AmourGen = ['Pants', 'Leggings', 'Gleaves', 'Fauld', 'Jacket', 'Shirt', 'Light Chest Piece', 'Heavy Chest Piece']
    AmourAdj_Chance = ['Cloth', 'Plate', 'Chainmail', 'Leather', 'Shard Plate']
    Amouradj_Dict = {"Cloth": random.randint(1, 10),
                     "Leather": random.randint(5, 15),
                     "Chainmail": random.randint(10, 20),
                     "Plate": random.randint(15, 25),
                     "StormPlate": random.randint(15, 50)}

    Amour_Itemchance = AmourGen[random.randint(0, 7)]
    AmourAdj_Chance = random.randint(1, 100)
    rarity_ItemChance = random.randint(1, 100)

    if rarity_ItemChance <= 50:
        rarity_ItemChance = "common"

    elif rarity_ItemChance <= 85:
        rarity_ItemChance = "uncommon"

    elif rarity_ItemChance <= 95:
        rarity_ItemChance = "rare"

    elif rarity_ItemChance >= 96:
        rarity_ItemChance = "legendary"


    if AmourAdj_Chance <= 50:
        AmourAdj_Chance = "Cloth"

    elif AmourAdj_Chance <= 75:
        AmourAdj_Chance = "Leather"

    elif AmourAdj_Chance <= 85:
        AmourAdj_Chance = "Chainmail"

    elif AmourAdj_Chance <= 95:
        AmourAdj_Chance = "Plate"

    elif AmourAdj_Chance >= 96:
        AmourAdj_Chance = "StormPlate"

    newDefence = Amouradj_Dict.get(AmourAdj_Chance) + rarity_Dict.get(rarity_ItemChance)

    newItem = rarity_ItemChance  + " " +  AmourAdj_Chance + " " +  Amour_Itemchance
    print("you found a " + newItem + " ,It has {} Defence!".format(newDefence))

    userinput = input("Do you want to keep the Amour? y/n, Your current Chest and Pants are {}, {}".format(inventory.get("Chest")[1], inventory.get("Pants")[1]))

    while True:
        if userinput == "n":
            if Amour_Itemchance in AmourGen[4:]:
                print("your Amour is still your beloved {}".format(inventory["Chest"][0]))
                break
            else:
                print("your Amour is still your beloved {}".format(inventory["Pants"][0]))
                break


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
    locations = ['Desert', 'Bridge', 'Hills', 'Forrest', "Town", "City", "Abandoned house"]
    adjLoc = ["Spooky", "windy", "Barron", "Stormy", "Dark"]

    Locchance = random.randint(0, 6)
    adjLoc_Chance = random.randint(0, 4)
    rarity_ItemChance = random.randint(0, 3)

    TheLocation = rarity[rarity_ItemChance] +" "+ adjLoc[adjLoc_Chance] + " " + locations[Locchance]
    print(TheLocation)


def MonsterGen():
    global MonsterHealth
    global MonsterDamage
    global TheMonster
    Monster_Dict = {"Bandit": (random.randint(1, 100), random.randint(10, 20)),
                    "Orc": (random.randint(40, 100), random.randint(15, 25)),
                    "Ghost": (random.randint(20, 50), random.randint(25, 30)),
                    "Demon": (random.randint(100, 200), random.randint(15, 50)),
                    "Wolf": (random.randint(15, 50), random.randint(5, 20)),
                    "Bear": (random.randint(15, 50), random.randint(5, 20)),
                    "Cthulu": (random.randint(100, 400), random.randint(25, 100))}


    adjectives_Dict = {"Whimpy": (random.randint(1, 10), random.randint(1, 10)),
                       "Friendly": (random.randint(5, 15), random.randint(1, 10)),
                       "Tough": (random.randint(10, 20), random.randint(1, 10)),
                       "Scary": (random.randint(15, 25), random.randint(1, 10)),
                       "Deadly": (random.randint(15, 50),random.randint(1, 10))}





    MonsterTypes = ["Bandit", "Orc", "Ghost", "Demon", "Wolf", "Bear", "Cthulu"]
    AdjMonster = ["Whimpy", "Friendly", "Tough", "Scary", "Deadly"]

    MonsterTypesChance = random.randint(0, 101)
    AdjMonsterChance = random.randint(0, 101)

    Monster = AdjMonsterChance + MonsterTypesChance


    if MonsterTypesChance <= 10:
        MonsterTypesChance = "Bear"

    elif MonsterTypesChance <= 20:
        MonsterTypesChance = "Wolf"

    elif MonsterTypesChance <= 40:
        MonsterTypesChance = "Bandit"

    elif MonsterTypesChance <= 60:
        MonsterTypesChance = "Orc"

    elif MonsterTypesChance <= 70:
        MonsterTypesChance = "Ghost"

    elif MonsterTypesChance <= 96:
        MonsterTypesChance = "Demon"

    elif MonsterTypesChance >= 97:
        MonsterTypesChance = "Cthulu"


    if AdjMonsterChance <= 30:
        AdjMonsterChance = "Whimpy"

    elif AdjMonsterChance <=40:
        AdjMonsterChance = "Friendly"

    elif AdjMonsterChance <= 60:
        AdjMonsterChance = "Tough"

    elif AdjMonsterChance <= 89:
        AdjMonsterChance = "Scary"

    elif AdjMonsterChance >=90:
        AdjMonsterChance = "Deadly"



    MonsterHealth , MonsterDamage = Monster_Dict.get(MonsterTypesChance)
    TheMonster = AdjMonsterChance +' ' + MonsterTypesChance
    AdjHeath, AdjDamage = adjectives_Dict.get(AdjMonsterChance)
    MonsterHealth += AdjHeath
    MonsterDamage += AdjDamage

    print("You are faced with a {} it has {} Heath and does {} Damage!".format(TheMonster, MonsterHealth, MonsterDamage))



while True:

    MeleeWeapon, Meleedamage = inventory.get('Melee Weapon')
    RangedWeapon, Rangeddamage = inventory.get('Ranged Weapon')
    defence = round((inventory.get("Chest")[1] + inventory.get("Pants")[1])/2)
    if userinput.lower() =="quit":
        break

    elif PlayerStats.get("health") <= 0:
        print("You Died")
        break


    elif userinput.lower() == "more loot":
        lootDrop()

    elif userinput.lower() == "monster":
        MonsterGen()

    elif userinput.lower() == "more a":
        LootAmour()

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

    elif userinput.lower() == "kill":
        PlayerStats["health"] -= PlayerStats.get("health")

    elif userinput.lower() =="heal":
        if BoolChance() == True:
            PlayerStats['health'] = maxhealing
            print("You are fully healed!!")

        else:
            print("You could not be healed!")


    elif userinput.lower() =="move on":
        LocGen()
        if BoolChance() == True:

            time.sleep(.5)
            MonsterGen()
            time.sleep(.5)
            monstername = TheMonster

            while True:
                userinput = input("Pick a weapon to attack with or Run: Melee {} damage or Ranged {} damage ".format(Meleedamage, Rangeddamage))
                if userinput.lower() == "melee":

                    if BoolChance() == True:
                        MonsterHealth -= Meleedamage
                        time.sleep(.5)
                        print("You Hit for {} Damage, The {} has {} Health Left".format(Meleedamage ,TheMonster , MonsterHealth))
                    else:
                        time.sleep(.5)
                        print("You missed!")



                    if MonsterHealth <= 0:
                        time.sleep(0.5)
                        print("You have defeated the {}".format(monstername))
                        time.sleep(0.5)
                        if BoolChance() == True:
                            lootDrop()
                        break

                    elif userinput.lower() == "run":
                        if BoolChance() == True:
                            time.sleep(.5)
                            print('You Ran Away!')
                            break

                        else:
                            time.sleep(.5)
                            print("You could not run away!")

                    elif PlayerStats.get("health") <= 0:
                        time.sleep(.5)
                        print("You Died!")
                        break


                if userinput.lower() == "ranged":

                    if BoolChance() == True:
                        MonsterHealth -= Rangeddamage
                        time.sleep(.5)
                        print("You Hit for {} Damage, {} has {} Health Left".format(Rangeddamage , TheMonster ,MonsterHealth))
                    else:
                        time.sleep(.5)
                        print("You missed!")

                    if BoolChance() == True:
                        if (MonsterDamage-defence) <= 0:
                            print("The {} does no damage!".format(TheMonster))
                            pass
                        else:
                            PlayerStats['health'] -= (MonsterDamage-defence)
                            time.sleep(0.5)
                            print("The {} has hit you for {} damage! You have {} Health left!".format(TheMonster, MonsterDamage-defence, PlayerStats.get("health")))


                    if MonsterHealth <= 0:
                        time.sleep(0.5)
                        print("You have defeated the {}".format(monstername))
                        time.sleep(0.5)
                        if BoolChance() == True:
                            lootDrop()
                        break

                    elif PlayerStats.get("health") <= 0:
                        time.sleep(.5)
                        print("You Died!")
                        break

                if BoolChance() == True:
                    if (MonsterDamage-defence) <= 0:
                        print("The {} does no damage!".format(TheMonster))
                        pass
                    else:
                        PlayerStats['health'] -= (MonsterDamage-defence)
                        time.sleep(0.5)
                        print("The {} has hit you for {} damage! You have {} Health left!".format(TheMonster, MonsterDamage-defence, PlayerStats.get("health")))


                if userinput.lower() == "run":
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


    else:
        print("Unknown Command, please try again, your commands are as followed")
        for i in CommandList:
            print(i)



    userinput = input()



# MonsterStats = {"strength": int(random.randint(1,20)), "Constitution": int(random.randint(1,10)),"Dexterity": int(random.randint(1,20))}
