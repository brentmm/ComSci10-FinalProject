#possible enemies level 1
enemies_one = ["Goblin", "Bandit", "Ogre", "Ghost", "Ent"]

#possible enemies level 2
enemies_two = ["Spider", "Bat", "Snakes", "Rat", "Skeleton"]

#possible enemies level 3
enemies_three = [" Mountain troll", "Wolf", "Giant", "Wizard", "Rock Golem"]

#items sold at shops
shopItems = [
    "Stick", "Brass Knuckles", "Steel Club", "Dagger", "EPIC GAMER SWORD",
    "Rubber Glove", "Leather Armour", "Chain Armour", "Small Sheild",
    "Big Sheild", "Potion of health 1", "Potion of health 2",
    "Potion of health 3", "Potion of damage 1", "Potion of damage 2",
    "Lettuce", "Avocado", "Pork", "Chicken", "Beef"
]

#players invertory
playerInventory = []

#beginning of program
print("Welcome to Brent Martin's Final Project")
print("")

#asking user if they are ready to start the game
start = input("Would you like to start the game? (yes or no): ").lower()

while start != "yes" and start != "no":  #checking for valid user input
    print("")
    start = input("Would you like to start the game?? (yes or no): ").lower()

if start == "no":  #if no, they play anyways
    print("")
    print("Welp, Sucks!")

#ask if new user or not
#start new game or start at progress

#starting new game setup
print("")
input("Let the journey begin!")
print("")

#introducing the characters
print("Meet the Characters")
print("")
print(
    "1) Agnar The Knight: \n Health: 200 \n Attack: 1-50 \n Money: 100 Cryolar"
)
print("")
print(
    "2) Valkyrie The Archer: \n Health: 100 \n Attack: 1-30 \n Money: 50 Cryolar"
)
print("")
print(
    "3) Vicar The Axe Lord: \n Health: 150 \n Attack: 1-70 \n Money: 75 Cryolar"
)
print("")
print(
    "4) Margravine The Witch: \n Health: 100 \n Attack: 1-100 \n Money: 50 Cryolar"
)
print("")
print(
    "5) Reeve The Sorcerer: \n Health: 125 \n Attack: 1-10 \n Money: 63 Cryolar"
)
print("")
print(
    "6) Madellaine The Spearwoman: \n Health: 150 \n Attack: 1-40 \n Money: 75 Cryolar"
)
print("")

#getting user to pick character
characterChoice = input("Choose your Character (1, 2, 3, 4, 5, OR 6): ")

while characterChoice != "1" and characterChoice != "2" and characterChoice != "3" and characterChoice != "4" and characterChoice != "5" and characterChoice != "6":  #checking for valid user input
    print("")
    characterChoice = input("Choose your Character (1, 2, 3, 4, 5, OR 6): ")

#assigning character choice
characterChoice = int(characterChoice)

#assigning varible values deterimed on character selection
if characterChoice == 1:
    characterName = "Agnar The Knight"
    originalHealth = 200
    playerHealth = originalHealth
    playerMoney = 100

if characterChoice == 2:
    characterName = "Valkyrie The Archer"
    originalHealth = 100
    playerHealth = originalHealth
    playerMoney = 50

if characterChoice == 3:
    characterName = "Vicar The Axe Lord"
    originalHealth = 150
    playerHealth = originalHealth
    playerMoney = 75

if characterChoice == 4:
    characterName = "Margravine The Witch"
    originalHealth = 100
    playerHealth = originalHealth
    playerMoney = 50

if characterChoice == 5:
    characterName = "Reeve The Sorcerer"
    originalHealth = 125
    playerHealth = originalHealth
    playerMoney = 63

if characterChoice == 6:
    characterName = "Madellaine The Spearwoman"
    originalHealth = 150
    playerHealth = originalHealth
    playerMoney = 75

#assigning randAlly value
import random
randAlly = random.randint(1, 6)

#making sure ally is not users character
while randAlly == characterChoice:
    randAlly = random.randint(1, 6)

#assigning randAlly value
if randAlly == 1:
    ally = "Agnar The Knight"
    characterHealth = 200

if randAlly == 2:
    ally = "Valkyrie The Archer"
    characterHealth = 100

if randAlly == 3:
    ally = "Vicar The Axe Lord"
    characterHealth = 150

if randAlly == 4:
    ally = "Margravine The Witch"
    characterHealth = 100

if randAlly == 5:
    ally = "Reeve The Sorcerer"
    characterHealth = 125

if randAlly == 6:
    ally = "Madellaine The Spearwoman"
    characterHealth = 150


#generating number for harmful events
def ranDamage():
    damage = random.randint(1, 25)
    return damage


#shopping
def shopping(list1):
    print("")
    print("Welcome to my shop!")
    print("")
    print("")
    item = []
    for x in range(0, 4):
        randitem = random.randint(0, 19)
        item.append(shopItems[randitem])
    return item


#randomly assigning enemy for battle
def battleSetup(enemies_one, enemies_two, enemies_three):
    if level == 1:
        randEnemy = random.randint(0, 4)
        enemy = enemies_one[randEnemy]
    if level == 2:
        randEnemy = random.randint(0, 4)
        enemy = enemies_two[randEnemy]
    if level == 3:
        randEnemy = random.randint(0, 4)
        enemy = enemies_three[randEnemy]
    return enemy


#performing item actions
def itemUse(itemSelect, playerHealth, pDamage):

    #Potion of health 1
    if itemSelect == "Potion of health 1":
        print("You have used Potion of health 1.")
        healthPlus = random.randint(10, 20)
        playerHealth = playerHealth + healthPlus
        print("You have gained " + str(healthPlus) + " health.")

    #Potion of health 2
    elif itemSelect == "Potion of health 2":
        print("You have used Potion of health 2.")
        healthPlus = random.randint(20, 30)
        playerHealth = playerHealth + healthPlus
        print("You have gained " + str(healthPlus) + " health.")

    #Potion of health 3
    elif itemSelect == "Potion of health 3":
        print("You have used Potion of health 3.")
        healthPlus = random.randint(30, 40)
        playerHealth = playerHealth + healthPlus
        print("You have gained " + str(healthPlus) + " health.")

    #Potion of damage 1
    elif itemSelect == "Potion of damage 1":
        print("You have used Potion of damage 1.")
        damagePlus = random.randint(5, 10)
        pDamage = playerAttack + damagePlus
        print("You have gained " + str(damagePlus) + " health.")

    #Potion of damage 2
    elif itemSelect == "Potion of damage 2":
        print("You have used Potion of damage 2.")
        damagePlus = random.randint(10, 15)
        pDamage = playerAttack + damagePlus
        print("You have gained " + str(damagePlus) + " health.")

    #Lettuce
    elif itemSelect == "Lettuce":
        print("You have used Lettuce.")
        healthPlus = random.randint(1, 5)
        playerHealth = playerHealth + healthPlus
        print("You have gained " + str(healthPlus) + " health.")

    #Avocado
    elif itemSelect == "Avocado":
        print("You have used Avocado.")
        healthPlus = random.randint(5, 10)
        playerHealth = playerHealth + healthPlus
        print("You have gained " + str(healthPlus) + " health.")

    #Pork
    elif itemSelect == "Pork":
        print("You have used Pork.")
        healthPlus = random.randint(10, 15)
        playerHealth = playerHealth + healthPlus
        print("You have gained " + str(healthPlus) + " health.")

    #Chicken
    elif itemSelect == "Chicken":
        print("You have used Chicken.")
        healthPlus = random.randint(15, 20)
        playerHealth = playerHealth + healthPlus
        print("You have gained " + str(healthPlus) + " health.")

    #Beef
    elif itemSelect == "Beef":
        print("You have used Beef.")
        healthPlus = random.randint(15, 20)
        playerHealth = playerHealth + healthPlus
        print("You have gained " + str(healthPlus) + " health.")

    #if the item is a weapon or defense item then user is unable to use them here
    else:
        print("That item cannot be used here.")
    return playerHealth, pDamage


#player attacking
def playerAttack():
    attack = random.randint(1, 10)

    #generating damage depending on user's character choice
    if characterChoice == 1:
        playerMove = attack + 25
    if characterChoice == 2:
        playerMove = attack + 15
    if characterChoice == 3:
        playerMove = attack + 35
    if characterChoice == 4:
        playerMove = attack + 50
    if characterChoice == 5:
        playerMove = attack + 50
    if characterChoice == 6:
        playerMove = attack + 20

    #adding weapon perks
    if "Stick" in playerInventory:
        playerMove = playerMove * 1.1
    if "Brass Knuckles" in playerInventory:
        playerMove = playerMove * 1.7
    if "Steel Club" in playerInventory:
        playerMove = playerMove * 1.5
    if "Dagger" in playerInventory:
        playerMove = playerMove * 1.7
    if "EPIC GAMER SWORD" in playerInventory:
        playerMove = playerMove * 2

    #making the players damage a whole number
    playerMove = int(playerMove)

    return playerMove


#randomly assigning enemy health
def enemyHP():
    enemyLife = random.randint(75, 125)
    return enemyLife


#enemy attacking
def enemyAttack():

    #generating enemy attack damage
    enemyDamage = random.randint(1, 30)

    #adding defense perks
    if "Rubber Glove" in playerInventory:
        enemyDamage = enemyDamage - random.randint(1, 5)
    if "Leather Armour" in playerInventory:
        enemyDamage = enemyDamage - random.randint(10, 15)
    if "Steel Club" in playerInventory:
        enemyDamage = enemyDamage - random.randint(15, 20)
    if "Small Shield" in playerInventory:
        enemyDamage = enemyDamage - random.randint(10, 15)
    if "Big Shield" in playerInventory:
        enemyDamage = enemyDamage - random.randint(15, 20)
    return enemyDamage


#randomly assigning boss health
def bossHP():
    bossLife = random.randint(200, 400)
    return bossLife


#boss attacking
def bossAttack():

    #generating boss attack damage
    bossDamage = random.randint(1, 50)

    #adding defense perks
    if "Rubber Glove" in playerInventory:
        bossDamage = bossDamage - random.randint(1, 5)
    if "Leather Armour" in playerInventory:
        bossDamage = bossDamage - random.randint(1, 5)
    if "Steel Club" in playerInventory:
        bossDamage = bossDamage - random.randint(1, 5)
    if "Small Shield" in playerInventory:
        bossDamage = bossDamage - random.randint(1, 5)
    if "Big Shield" in playerInventory:
        bossDamage = bossDamage - random.randint(1, 5)
    return bossDamage


#starting the game
print("")
input("Lets Begin " + characterName)
print("")
input(
    "It is a wonderful morning in the town of Durnatel, the birds are chirping, you can smell the flowers in the air, and feel the sun on your skin through the window."
)
print("")
input(
    "Durnatel is a peaceful place, a mining town, with a river that flows from the mountains, and not too far east the Brombia Caves which are used for mining."
)
print("")
input("On this lovely morning you are trying to decide what to do. ")
print("")
input(
    "As you are about to get out of bed you are rudely interrupted by someone yelling."
)
print("")
input(characterName + ", " + characterName +
      ", I bring urgent news, from the king.")
print("")
input("As you unravel the scroll it reads…")

#assigning the game level
level = 1

print("")
input(
    "Dear noble " + characterName + ", early this morning we received a beckon for help from the town of Calcherth, claiming that goblins have raided their kingdom, please kindly assist " + ally + " to the town of Calcherth, they will be waiting by the centre fountain at eleven o’clock this fine morning."
)
print("")
input(
    "As quick as you can you rush over to the town's main fountain to be greeted by "
    + ally)
print("")
input("You and " + ally + " set off on the Trail to Calcherth.")
print("")
input(
    "The trail consists of mostly forest and Durnatel is a twenty kilometers walk from Calcherth."
)
print("")

#randomly assigning enemy
enemy = battleSetup(enemies_one, enemies_two, enemies_three)

input("As you and " + ally +
      " are about twenty minutes into your journey when suddenly a " + enemy +
      " jumps out and challenges you.")
print("")

#checking user's invetory to see if they could use an item
if len(playerInventory) != 0:
    useItem = input("Would you like to use an item? (yes or no): ").lower()
    print("")

    while useItem != "yes" and useItem != "no":  #checking for valid input
        useItem = input("Would you like to use an item? (yes or no): ")
        print("")

    #if they want to use and item then player inventory is shown to the user
    if useItem == "yes":
        print("Your inventory: ")
        for i in playerInventory:
            print("(" + str(playerInventory.index(i) + 1) + ")" +
                  (i.capitalize()))
        print("")

        #user selects the item they want to use
        selectItem = input("What item would you like to use?: ")

        #making inventory index equal to choosen item name
        itemSelect = playerInventory[int(selectItem) - 1]

print()   
#enemy battle: 1 (loops until user wins)
victory = False
while victory == False:

    #saving user's health incase they lose and have to restart battle
    battleHealth = playerHealth

    #assigns enemy health for the battle
    enemyHealth = enemyHP()

    #checking health to see if both can fight/continue to fight
    while enemyHealth >= 1 and playerHealth >= 1:

        #battle if item has been used
        if len(playerInventory) != 0:
            pDamage = 0
            if useItem == "yes":
                if itemSelect == "Stick" or itemSelect == "Brass Knuckles" or itemSelect == "Steel Club" or itemSelect == "Dagger" or itemSelect == "EPIC GAMER SWORD" or itemSelect == "Rubber Glove" or itemSelect == "Leather Armour" or itemSelect == "Chain Armour" or itemSelect == "Small Sheild" or itemSelect == "Big Sheild":
                    pass
                else:
                    playerInventory.pop(int(selectItem) - 1)
                pDamage = itemUse(itemSelect, playerHealth, pDamage)
                pDamage = pDamage[1] + playerAttack()

        #battle without the use of an item
            else:
                pDamage = playerAttack()
        else:
            pDamage = playerAttack()

        #taking away enemy health
        enemyHealth = enemyHealth - pDamage

        #checking if enemy is alive and can attack
        if enemyHealth < 1:  #if enemy is dead
            enemyHealth = 0
        print("You did " + str(pDamage) + " damage. The " + enemy +
              " health is at " + str(enemyHealth))
        if enemyHealth > 1:  #if enemy is still alive
            eDamage = enemyAttack()

            #taking away player health
            playerHealth = playerHealth - eDamage
            if playerHealth < 1:  #if player is dead
                playerHealth = 0
            print(enemy + " did " + str(eDamage) + " damage. You have " +
                  str(playerHealth) + " health left.")
            

    #if player won battle
    if enemyHealth < 1:
        print("")
        print("You won!")
        print("")
        input("You gained 25 Cryolar")
        playerMoney = playerMoney + 25  #adding reward
        victory = True  #exiting loop

    #if player lost
    if playerHealth < 1:
        print("")
        print("You lost! You have lost 5 Cryolar")
        playerMoney = playerMoney - 5  #taking fate
        print("")
        input("As you and " + ally +
              " are about twenty minutes into your journey when suddenly a " +
              enemy + " jumps out and challenges you.")
        playerHealth = battleHealth  #reseting player health to try the battle again
        victory = False  #staying in loop

print("")
input(
    "Ten kilometers into the trail you and ally hear a sound from around the corner of the trail. In ready position you watch a shadow emerge from around the corner."
)
print("")
input("What a relief it's not an enemy, it the traveling merchant.")
print("")

#asking user if they wanna shop
shopBuy = input(
    "Would you like to purchase something? All items only 30 Cryolar (yes or no): "
).lower()
while shopBuy != "yes" and shopBuy != "no":  #checking for valid input
    print("")
    shopBuy = input("Would you like to purchase something? (yes or no): ")

#shop: 1
if shopBuy == "yes":
    item = shopping(shopItems)  #randomly selecting 5 items to sell
    print("You have " + str(playerMoney) + " Cryolar")
    print("")
    print("For Sale: ")  #showing items for sale
    for i in item:
        print("(" + str(item.index(i) + 1) + ")" + (i.capitalize()))
    print("")
    print(" (a) Buy Item \n (b) Leave")
    print("")
    shopChoice = input("What would you like to do? (a or b): ").lower(
    )  #user selecting to buy or not
    while shopChoice != "a" and shopChoice != "b":  #checking for valid input
        print("")
        shopChoice = input("What would you like to do? (a or b): ")

    if shopChoice == "a":
        print("")
        itemChoice = input("What item do to want to buy? (1, 2, 3, OR 4): ")
        while itemChoice != "1" and itemChoice != "2" and itemChoice != "3" and itemChoice != "4":  #checking for valid input
            print("")
            itemChoice = input("What item do to want to buy?: ")

        #checking users input and steps into required function
        if itemChoice == "1" or itemChoice == "2" or itemChoice == "3" or itemChoice == "4" or itemChoice == "5":

            #adding item to players inventory
            playerInventory.append(item[int(itemChoice) - 1])
            playerMoney = playerMoney - 30  #taking money from player
            print("")
        print(item[int(itemChoice) - 1] +
              " has been added to your inventory. You have " +
              str(playerMoney) + " Cryalor.")
    else:
        print("")
        print("Don't waste my time, you fool!")

print("")
input("Finally, after four hours on foot you have reached Calcherth. ")
print("")
input(
    "The town looks terrible. There is no one to be seen, and the streets are a mess."
)
print("")

#randomly selecting enemy for battle
battleSetup(enemies_one, enemies_two, enemies_three)

input(
    "As you walk through the town a tumbleweed rolls into you knocking you to the ground.  As you stand up ally shouts that a "
    + enemy + " is blocking your way and closing in.")
print("")

#checking user's invetory to see if they could use an item
if len(playerInventory) != 0:
    useItem = input("Would you like to use an item? (yes or no): ").lower()
    print("")

    while useItem != "yes" and useItem != "no":  #checking for valid input
        useItem = input("Would you like to use an item? (yes or no): ")
        print("")

    #if they want to use and item then player inventory is shown to the user
    if useItem == "yes":
        print("Your inventory: ")
        for i in playerInventory:
            print("(" + str(playerInventory.index(i) + 1) + ")" +
                  (i.capitalize()))
        print("")

        #user selects the item they want to use
        selectItem = input("What item would you like to use?: ")

        #making inventory index equal to choosen item name
        itemSelect = playerInventory[int(selectItem) - 1]

#enemy battle: 2 (loops until user wins)
victory = False
while victory == False:

    #saving user's health incase they lose and have to restart battle
    battleHealth = playerHealth

    #assigns enemy health for the battle
    enemyHealth = enemyHP()

    #checking health to see if both can fight/continue to fight
    while enemyHealth >= 1 and playerHealth >= 1:

        #battle if item has been used
        if len(playerInventory) != 0:
            pDamage = 0
            if useItem == "yes":
                if itemSelect == "Stick" or itemSelect == "Brass Knuckles" or itemSelect == "Steel Club" or itemSelect == "Dagger" or itemSelect == "EPIC GAMER SWORD" or itemSelect == "Rubber Glove" or itemSelect == "Leather Armour" or itemSelect == "Chain Armour" or itemSelect == "Small Sheild" or itemSelect == "Big Sheild":
                    pass
                else:
                    playerInventory.pop(int(selectItem) - 1)
                pDamage = itemUse(itemSelect, playerHealth, pDamage)
                pDamage = pDamage[1] + playerAttack()

        #battle without the use of an item
            else:
                pDamage = playerAttack()
        else:
            pDamage = playerAttack()

        #taking away enemy health
        enemyHealth = enemyHealth - pDamage

        #checking if enemy is alive and can attack
        if enemyHealth < 1:  #if enemy is dead
            enemyHealth = 0
        print("You did " + str(pDamage) + " damage. The " + enemy +
              " health is at " + str(enemyHealth))
        if enemyHealth > 1:  #if enemy is still alive
            eDamage = enemyAttack()

            #taking away player health
            playerHealth = playerHealth - eDamage
            if playerHealth < 1:  #if player is dead
                playerHealth = 0
            print(enemy + " did " + str(eDamage) + " damage. You have " +
                  str(playerHealth) + " health left.")

    #if player won battle
    if enemyHealth < 1:
        print("")
        print("You won!")
        print("")
        input("You gained 25 Cryolar")
        playerMoney = playerMoney + 25  #adding reward
        victory = True  #exiting loop

    #if player lost
    if playerHealth < 1:
        print("")
        print("You lost! You have lost 5 Cryolar")
        playerMoney = playerMoney - 5  #taking fate
        print("")
        input("As you stand up ally shouts that a " + enemy +
              " is blocking your way and closing in.")
        playerHealth = battleHealth  # resetting players health to redo the battle
        victory = False  #staying in loop

print("")
input(
    "You have finally made it to the castle. The gates are wide open. You walk straight in and up to the giant castle door."
)
print("")

#randomly selecting enemy for battle
battleSetup(enemies_one, enemies_two, enemies_three)

input("As you open the door a " + enemy + " swings at you.")
print("")

#checking user's invetory to see if they could use an item
if len(playerInventory) != 0:
    useItem = input("Would you like to use an item? (yes or no): ").lower()
    print("")

    while useItem != "yes" and useItem != "no":  #checking for valid input
        useItem = input("Would you like to use an item? (yes or no): ")
        print("")

    #if they want to use and item then player inventory is shown to the user
    if useItem == "yes":
        print("Your inventory: ")
        for i in playerInventory:
            print("(" + str(playerInventory.index(i) + 1) + ")" +
                  (i.capitalize()))
        print("")

        #user selects the item they want to use
        selectItem = input("What item would you like to use?: ")

        #making inventory index equal to choosen item name
        itemSelect = playerInventory[int(selectItem) - 1]

#enemy battle: 3 (loops until user wins)
victory = False
while victory == False:

    #saving user's health incase they lose and have to restart battle
    battleHealth = playerHealth

    #assigns enemy health for the battle
    enemyHealth = enemyHP()

    #checking health to see if both can fight/continue to fight
    while enemyHealth >= 1 and playerHealth >= 1:

        #battle if item has been used
        if len(playerInventory) != 0:
            pDamage = 0
            if useItem == "yes":
                if itemSelect == "Stick" or itemSelect == "Brass Knuckles" or itemSelect == "Steel Club" or itemSelect == "Dagger" or itemSelect == "EPIC GAMER SWORD" or itemSelect == "Rubber Glove" or itemSelect == "Leather Armour" or itemSelect == "Chain Armour" or itemSelect == "Small Sheild" or itemSelect == "Big Sheild":
                    pass
                else:
                    playerInventory.pop(int(selectItem) - 1)
                pDamage = itemUse(itemSelect, playerHealth, pDamage)
                pDamage = pDamage[1] + playerAttack()

        #battle without the use of an item
            else:
                pDamage = playerAttack()
        else:
            pDamage = playerAttack()

        #taking away enemy health
        enemyHealth = enemyHealth - pDamage

        #checking if enemy is alive and can attack
        if enemyHealth < 1:  #if enemy is dead
            enemyHealth = 0
        print("You did " + str(pDamage) + " damage. The " + enemy +
              " health is at " + str(enemyHealth))
        if enemyHealth > 1:  #if enemy is still alive
            eDamage = enemyAttack()

            #taking away player health
            playerHealth = playerHealth - eDamage
            if playerHealth < 1:  #if player is dead
                playerHealth = 0
            print(enemy + " did " + str(eDamage) + " damage. You have " +
                  str(playerHealth) + " health left.")

    #if player won battle
    if enemyHealth < 1:
        print("")
        print("You won!")
        print("")
        input("You gained 25 Cryolar")
        playerMoney = playerMoney + 25  #adding reward
        victory = True  #exiting loop

    #if player lost
    if playerHealth < 1:
        print("")
        print("You lost! You have lost 5 Cryolar")
        playerMoney = playerMoney - 5  #taking fate
        print("")
        input("As you open the door a " + enemy + " swings at you.")
        playerHealth = battleHealth  #resetting players health to redo the battle
        victory = False  #staying in loop

print("")
input(
    "After winning the fight you walk into the main hall and there in the throne sits THE GOBLIN KING!!!!!!!!!"
)
print("")

#checking user's invetory to see if they could use an item
if len(playerInventory) != 0:
    useItem = input("Would you like to use an item? (yes or no): ").lower()
    print("")

    while useItem != "yes" and useItem != "no":  #checking for valid input
        useItem = input("Would you like to use an item? (yes or no): ")
        print("")

    #if they want to use and item then player inventory is shown to the user
    if useItem == "yes":
        print("Your inventory: ")
        for i in playerInventory:
            print("(" + str(playerInventory.index(i) + 1) + ")" +
                  (i.capitalize()))
        print("")

        #user selects the item they want to use
        selectItem = input("What item would you like to use?: ")

        #making inventory index equal to choosen item name
        itemSelect = playerInventory[int(selectItem) - 1]

#boss battle: (loops until player wins)
victory = False
while victory == False:

    battleHealth = playerHealth  #saving players health incase of redo
    bossHealth = bossHP()  #assigns boss health for battle

    #checking health to see if both can fight/continue to fight
    while bossHealth >= 1 and playerHealth >= 1:

        #battle if item has been used
        if len(playerInventory) != 0:
            pDamage = 0
            if useItem == "yes":
                if itemSelect == "Stick" or itemSelect == "Brass Knuckles" or itemSelect == "Steel Club" or itemSelect == "Dagger" or itemSelect == "EPIC GAMER SWORD" or itemSelect == "Rubber Glove" or itemSelect == "Leather Armour" or itemSelect == "Chain Armour" or itemSelect == "Small Sheild" or itemSelect == "Big Sheild":
                    pass
                else:
                    playerInventory.pop(int(selectItem) - 1)
                pDamage = itemUse(itemSelect, playerHealth, pDamage)
                pDamage = pDamage[1] + playerAttack()

        #battle without the use of an item
            else:
                pDamage = playerAttack()
        else:
            pDamage = playerAttack()

        #taking away boss health
        bossHealth = bossHealth - pDamage

        #checking if boss is alive and can attack
        if bossHealth < 1:  #if boss is dead
            bossHealth = 0
        print("You did " + str(pDamage) +
              " damage. The Gobin King's health is at " + str(bossHealth))
        if bossHealth > 1:  #if boss is still alive
            bDamage = bossAttack()

            #taking away player health
            playerHealth = playerHealth - bDamage
            if playerHealth < 1:  #if player is dead
                playerHealth = 0
            print(" The Gobin King did " + str(bDamage) +
                  " damage. You have " + str(playerHealth) + " health left.")

    #if player won battle
    if bossHealth < 1:
        print("")
        print("You won!")
        print("")
        print("You gained 100 Cryolar")
        playerMoney = playerMoney + 100  #adding reward
        victory = True  #exiting loop

    #if player lost
    if playerHealth < 1:
        playerHealth = 0
        print("")
        print("You lost! You have lost 10 Cryolar")
        playerMoney = playerMoney - 10
        print("")
        input("The Goblin King Challeneges you!")
        playerHealth = battleHealth
        victory = False

print("")
input(
    "After defeating The Goblin King the town of Calcherth was once again peaceful. You return to Dernatel with "
    + ally + ".")
print("")
input("The king thanks you and rewards you with one hundred Cryolar.")
playerMoney = playerMoney + 100
playerHealth = originalHealth
print("")

#asking user if they wanna go to level 2
keepGoing = input("Ready to continue? (yes or no): ")
while keepGoing != "yes" and keepGoing != "no":  #checking for valid user input
    print("")
    keepGoing = input("Would you like to keep going? (yes or no): ").lower()

#saving progress if no
if keepGoing == "no":
   "You are already playing, you cannot leave now!"

#going to level 2 if yes
if keepGoing == "yes":
    #assigning level value
    level = 2

#starting Level 2
print("")
input("All of a sudden a cluster of spiders drop the sky.")
print("")
input(
    "One of the spiders grabbed the King and surrounded him in a cage of webs."
)
print("")
input(
    "All of the spiders shriek in their native language, Spiogoshi, “Bydd eich brenin yn priodi ein brenhines”. Which in english means your King will marry our queen."
)
print("")
input(
    "You and " + ally +
    " look at each other with panic. The spider kingdom resided deep down in the Brombia Caverns. Quickly you set off towards the caves."
)
print("")
input(
    "Once you reach the entrance to the cave you light a torch and slowly enter…"
)
print("")

#randomly assigning enemy
battleSetup(enemies_one, enemies_two, enemies_three)

input("A clatter comes from ahead, a " + enemy + " is in your way. ")
print("")

#checking user's invetory to see if they could use an item
if len(playerInventory) != 0:
    useItem = input("Would you like to use an item? (yes or no): ").lower()
    print("")

    while useItem != "yes" and useItem != "no":  #checking for valid input
        useItem = input("Would you like to use an item? (yes or no): ")
        print("")

    #if they want to use and item then player inventory is shown to the user
    if useItem == "yes":
        print("Your inventory: ")
        for i in playerInventory:
            print("(" + str(playerInventory.index(i) + 1) + ")" +
                  (i.capitalize()))
        print("")

        #user selects the item they want to use
        selectItem = input("What item would you like to use?: ")

        #making inventory index equal to choosen item name
        itemSelect = playerInventory[int(selectItem) - 1]

#enemy battle: 4 (loops until user wins)
victory = False
while victory == False:

    #saving user's health incase they lose and have to restart battle
    battleHealth = playerHealth

    #assigns enemy health for the battle
    enemyHealth = enemyHP()

    #checking health to see if both can fight/continue to fight
    while enemyHealth >= 1 and playerHealth >= 1:

        #battle if item has been used
        if len(playerInventory) != 0:
            pDamage = 0
            if useItem == "yes":
                if itemSelect == "Stick" or itemSelect == "Brass Knuckles" or itemSelect == "Steel Club" or itemSelect == "Dagger" or itemSelect == "EPIC GAMER SWORD" or itemSelect == "Rubber Glove" or itemSelect == "Leather Armour" or itemSelect == "Chain Armour" or itemSelect == "Small Sheild" or itemSelect == "Big Sheild":
                    pass
                else:
                    playerInventory.pop(int(selectItem) - 1)
                pDamage = itemUse(itemSelect, playerHealth, pDamage)
                pDamage = pDamage[1] + playerAttack()

        #battle without the use of an item
            else:
                pDamage = playerAttack()
        else:
            pDamage = playerAttack()

        #taking away enemy health
        enemyHealth = enemyHealth - pDamage

        #checking if enemy is alive and can attack
        if enemyHealth < 1:  #if enemy is dead
            enemyHealth = 0
        print("You did " + str(pDamage) + " damage. The " + enemy +
              " health is at " + str(enemyHealth))
        if enemyHealth > 1:  #if enemy is still alive
            eDamage = enemyAttack()

            #taking away player health
            playerHealth = playerHealth - eDamage
            if playerHealth < 1:  #if player is dead
                playerHealth = 0
            print(enemy + " did " + str(eDamage) + " damage. You have " +
                  str(playerHealth) + " health left.")

    #if player won battle
    if enemyHealth < 1:
        print("")
        print("You won!")
        print("")
        input("You gained 25 Cryolar")
        playerMoney = playerMoney + 25  #adding reward
        victory = True  #exiting loop

    #if player lost
    if playerHealth < 1:
        print("")
        print("You lost! You have lost 5 Cryolar")
        playerMoney = playerMoney - 5
        print("")
        input("A clatter comes from ahead, a " + enemy + " is in your way. ")
        playerHealth = battleHealth  #resetting players health to redo battle
        victory = False  #staying in loop

print("")
input(
    "You continue down into the cave, as your walking the ground begins to crumble. You and ally start to run but before you make it to solid ground you fall..."
)
print("")

#assigning hamful event damage
harm = ranDamage()
input(
    "There you lay, you gain your consciousness once again but you have lost "
    + str(harm) + " health.")
print("")

#randomly assigning enemy
battleSetup(enemies_one, enemies_two, enemies_three)

input(
    "You and ally are now lost in the cave, you begin walkling and turn a corner, a "
    + enemy + " lunges at you.")
print("")

#checking user's invetory to see if they could use an item
if len(playerInventory) != 0:
    useItem = input("Would you like to use an item? (yes or no): ").lower()
    print("")

    while useItem != "yes" and useItem != "no":  #checking for valid input
        useItem = input("Would you like to use an item? (yes or no): ")
        print("")

    #if they want to use and item then player inventory is shown to the user
    if useItem == "yes":
        print("Your inventory: ")
        for i in playerInventory:
            print("(" + str(playerInventory.index(i) + 1) + ")" +
                  (i.capitalize()))
        print("")

        #user selects the item they want to use
        selectItem = input("What item would you like to use?: ")

        #making inventory index equal to choosen item name
        itemSelect = playerInventory[int(selectItem) - 1]

#enemy battle: 5 (loops until user wins)
victory = False
while victory == False:

    #saving user's health incase they lose and have to restart battle
    battleHealth = playerHealth

    #assigns enemy health for the battle
    enemyHealth = enemyHP()

    #checking health to see if both can fight/continue to fight
    while enemyHealth >= 1 and playerHealth >= 1:

        #battle if item has been used
        if len(playerInventory) != 0:
            pDamage = 0
            if useItem == "yes":
                if itemSelect == "Stick" or itemSelect == "Brass Knuckles" or itemSelect == "Steel Club" or itemSelect == "Dagger" or itemSelect == "EPIC GAMER SWORD" or itemSelect == "Rubber Glove" or itemSelect == "Leather Armour" or itemSelect == "Chain Armour" or itemSelect == "Small Sheild" or itemSelect == "Big Sheild":
                    pass
                else:
                    playerInventory.pop(int(selectItem) - 1)
                pDamage = itemUse(itemSelect, playerHealth, pDamage)
                pDamage = pDamage[1] + playerAttack()

        #battle without the use of an item
            else:
                pDamage = playerAttack()
        else:
            pDamage = playerAttack()

        #taking away enemy health
        enemyHealth = enemyHealth - pDamage

        #checking if enemy is alive and can attack
        if enemyHealth < 1:  #if enemy is dead
            enemyHealth = 0
        print("You did " + str(pDamage) + " damage. The " + enemy +
              " health is at " + str(enemyHealth))
        if enemyHealth > 1:  #if enemy is still alive
            eDamage = enemyAttack()

            #taking away player health
            playerHealth = playerHealth - eDamage
            if playerHealth < 1:  #if player is dead
                playerHealth = 0
            print(enemy + " did " + str(eDamage) + " damage. You have " +
                  str(playerHealth) + " health left.")

    #if player won battle
    if enemyHealth < 1:
        print("")
        print("You won!")
        print("")
        input("You gained 25 Cryolar")
        playerMoney = playerMoney + 25  #adding reward
        victory = True  #exiting loop

    #if player lost
    if playerHealth < 1:
        print("")
        print("You lost! You have lost 5 Cryolar")
        playerMoney = playerMoney - 5  #taking fate
        print("")
        input(
            "You and ally are now lost in the cave, you begin walkling and turn a corner, a "
            + enemy + " lunges at you.")
        playerHealth = battleHealth  #resetting players health to redo battle
        victory = False  #staying in loop

print("")
input("You see a cluster of Spider Minions flee, you and ally follow.")
print("")
input(
    "You lose sight of the Spiders but continue walking, a little while later you manage to find Mr Moles Fantastic Shop."
)
print("")

#asking user if they wanna shop
shopBuy = input(
    "Would you like to purchase something? All items only 40 Cryolar (yes or no): "
).lower()
while shopBuy != "yes" and shopBuy != "no":  #checking for valid input
    shopBuy = input("Would you like to purchase something? (yes or no): ")

#shop: 2
if shopBuy == "yes":
    item = shopping(shopItems)  #randomly selecting 5 items to sell
    print("For Sale: ")  #showing items for sale
    for i in item:
        print("(" + str(item.index(i) + 1) + ")" + (i.capitalize()))
    print("")
    print(" (a) Buy Item \n (b) Leave")
    print("")
    shopChoice = input("What would you like to do? (a or b): ").lower(
    )  #user selecting to buy or not
    while shopChoice != "a" and shopChoice != "b":  #checking for valid input
        shopChoice = input(
            shopChoice=input("What would you like to do? (a or b): "))

    if shopChoice == "a":
        print("")
        itemChoice = input("What item do to want to buy? (1, 2, 3, OR 4): ")
        while itemChoice != "1" and itemChoice != "2" and itemChoice != "3" and itemChoice != "4" and itemChoice != "5":  #checking for valid input
            itemChoice = input("What item do to want to buy?: ")

        #checking users input and steps into required function
        if itemChoice == "1" or itemChoice == "2" or itemChoice == "3" or itemChoice == "4" or itemChoice == "5":

            #adding item to players inventory
            playerInventory.append(item[int(itemChoice) - 1])
            playerMoney = playerMoney - 30  #taking money from player
        print(item[int(itemChoice) - 1] +
              " has been added to your inventory. You have " +
              str(playerMoney) + " Cryalor.")
    else:
        print("Don't waste my time, you fool!")

print("")
input(ally + " calls you from ahead."
      "“" + characterName + ", I see the spiders nest!”")
print("")
input(
    "As you approach the spiders nest you can hear the spiders chanting “clymwch y gwlwm”. The ceremony has begun, they are they are marrying the King to their spider Queen. "
)
print("")
input(
    "“STOP THIS NOW!”, " + ally +
    " shouts to the cluster.  The chanting stops and all of the spider minions sharply turn towards your position. All the spiders scurry away with the King but one."
)
print("")
print("It shoots webs at you.")
print("")

#checking user's invetory to see if they could use an item
if len(playerInventory) != 0:
    useItem = input("Would you like to use an item? (yes or no): ").lower()
    print("")

    while useItem != "yes" and useItem != "no":  #checking for valid input
        useItem = input("Would you like to use an item? (yes or no): ")
        print("")

    #if they want to use and item then player inventory is shown to the user
    if useItem == "yes":
        print("Your inventory: ")
        for i in playerInventory:
            print("(" + str(playerInventory.index(i) + 1) + ")" +
                  (i.capitalize()))
        print("")

        #user selects the item they want to use
        selectItem = input("What item would you like to use?: ")

        #making inventory index equal to choosen item name
        itemSelect = playerInventory[int(selectItem) - 1]

#enemy battle: 6 (loops until user wins)
victory = False
while victory == False:

    #saving user's health incase they lose and have to restart battle
    battleHealth = playerHealth

    #assigns enemy health for the battle
    enemyHealth = enemyHP()

    #checking health to see if both can fight/continue to fight
    while enemyHealth >= 1 and playerHealth >= 1:

        #battle if item has been used
        if len(playerInventory) != 0:
            pDamage = 0
            if useItem == "yes":
                if itemSelect == "Stick" or itemSelect == "Brass Knuckles" or itemSelect == "Steel Club" or itemSelect == "Dagger" or itemSelect == "EPIC GAMER SWORD" or itemSelect == "Rubber Glove" or itemSelect == "Leather Armour" or itemSelect == "Chain Armour" or itemSelect == "Small Sheild" or itemSelect == "Big Sheild":
                    pass
                else:
                    playerInventory.pop(int(selectItem) - 1)
                pDamage = itemUse(itemSelect, playerHealth, pDamage)
                pDamage = pDamage[1] + playerAttack()

        #battle without the use of an item
            else:
                pDamage = playerAttack()
        else:
            pDamage = playerAttack()

        #taking away enemy health
        enemyHealth = enemyHealth - pDamage

        #checking if enemy is alive and can attack
        if enemyHealth < 1:  #if enemy is dead
            enemyHealth = 0
        print("You did " + str(pDamage) + " damage. The " + enemy +
              " health is at " + str(enemyHealth))
        if enemyHealth > 1:  #if enemy is still alive
            eDamage = enemyAttack()

            #taking away player health
            playerHealth = playerHealth - eDamage
            if playerHealth < 1:  #if player is dead
                playerHealth = 0
            print(enemy + " did " + str(eDamage) + " damage. You have " +
                  str(playerHealth) + " health left.")

    #if player won battle
    if enemyHealth < 1:
        print("")
        print("You won!")
        print("")
        input("You gained 25 Cryolar")
        playerMoney = playerMoney + 25  #adding reward
        victory = True  #exiting loop

    #if player lost
    if playerHealth < 1:
        print("")
        print("You lost! You have lost 5 Cryolar")
        playerMoney = playerMoney - 5  #taking fate
        print("")
        input("It shoots webs at you.")
        playerHealth = battleHealth  #resetting players health to redo battle
        victory = False  #staying in loop

print("")
input(
    "After defeating the spider minion you walk into the nest, there sits the Spider Queen with the King tied up behind her."
)
print("")

#checking user's invetory to see if they could use an item
if len(playerInventory) != 0:
    useItem = input("Would you like to use an item? (yes or no): ").lower()
    print("")

    while useItem != "yes" and useItem != "no":  #checking for valid input
        useItem = input("Would you like to use an item? (yes or no): ")
        print("")

    #if they want to use and item then player inventory is shown to the user
    if useItem == "yes":
        print("Your inventory: ")
        for i in playerInventory:
            print("(" + str(playerInventory.index(i) + 1) + ")" +
                  (i.capitalize()))
        print("")

        #user selects the item they want to use
        selectItem = input("What item would you like to use?: ")

        #making inventory index equal to choosen item name
        itemSelect = playerInventory[int(selectItem) - 1]

#boss battle: The Spider Queen (loops until player wins)
victory = False
while victory == False:

    battleHealth = playerHealth  #saving players health incase of redo
    bossHealth = bossHP()  #assigns boss health for battle

    #checking health to see if both can fight/continue to fight
    while bossHealth >= 1 and playerHealth >= 1:

        #battle if item has been used
        if len(playerInventory) != 0:
            pDamage = 0
            if useItem == "yes":
                if itemSelect == "Stick" or itemSelect == "Brass Knuckles" or itemSelect == "Steel Club" or itemSelect == "Dagger" or itemSelect == "EPIC GAMER SWORD" or itemSelect == "Rubber Glove" or itemSelect == "Leather Armour" or itemSelect == "Chain Armour" or itemSelect == "Small Sheild" or itemSelect == "Big Sheild":
                    pass
                else:
                    playerInventory.pop(int(selectItem) - 1)
                pDamage = itemUse(itemSelect, playerHealth, pDamage)
                pDamage = pDamage[1] + playerAttack()

        #battle without the use of an item
            else:
                pDamage = playerAttack()
        else:
            pDamage = playerAttack()

        #taking away boss health
        bossHealth = bossHealth - pDamage

        #checking if boss is alive and can attack
        if bossHealth < 1:  #if boss is dead
            bossHealth = 0
        print("You did " + str(pDamage) +
              " damage. The Spider Queen's health is at " + str(bossHealth))
        if bossHealth > 1:  #if boss is still alive
            bDamage = bossAttack()

            #taking away player health
            playerHealth = playerHealth - bDamage
            if playerHealth < 1:  #if player is dead
                playerHealth = 0
            print(" The Spider Queen did " + str(bDamage) +
                  " damage. You have " + str(playerHealth) + " health left.")

    #if player won battle
    if bossHealth < 1:
        print("")
        print("You won!")
        print("")
        print("You gained 100 Cryolar")
        playerMoney = playerMoney + 100  #adding reward
        playerHealth = originalHealth
        victory = True  #exiting loop

    #if player lost
    if playerHealth < 1:
        playerHealth = 0
        print("")
        print("You lost! You have lost 10 Cryolar")
        playerMoney = playerMoney - 10  #taking fate
        print("")
        input("The Spider Queen Challeneges you!")
        playerHealth = battleHealth  #reseting player health to try the battle again
        victory = False  #staying in loop
print("")
input(
    "You have defeated the Spider Queen, and untangle the King from spider webs. You are now lost in the caves. The king mentions there was a backdoor that all the minions escaped out of."
)
print("")
input(
    "You find the back door and follow it up, you finally see the light and march towards it. You come of the cave and realize you are about a kilometer west from Durnatel."
)
print("")
input(
    "Turns out the spiders nest it right under the town of Durnatel. You return to the castle and the King thanks you and you are once again rewared 100 cryolar."
)
print("")
input(
    "Unexpectedly fire begins to rain down on the kingdom, the Wizard colony is attacking."
)

#asking if they want to go to level 3
keepGoing = input("Ready to continue? (yes or no): ")
while keepGoing != "yes" and keepGoing != "no":  #checking for valid user input
    print("")
    keepGoing = input("Would you like to keep going? (yes or no): ").lower()

#saving progress if no
if keepGoing == "no":
   "You are already playing, you cannot leave now!"

#going to level 3 if yes
if keepGoing == "yes":
    level = 3  #assigning level value

print("")
input(
    "The kingdom is on fire, the wizards are casting spells like crazy. The people of Durnatel are being turned into frogs. Out of nowhere you see one of the wizards grow to an unimaginable size."
)
print("")
input("You and " + ally + " hustle over to the Giant Wizard.")
print("")
input("You shout at the giant wizard.")
print("")
input(
    "He bellows back, “HOW DARE YOU SPEAK TO ME LIKE THAT, I AM JOEY, THE ALL POWERFUL WIZARD OVERLORD, NOW YOU SHALL FACE THE CONSEQUENCES!!”. She casts a spell. You and "
    + ally + " are transported awayyyyyyyyyyyyyyy.")
print("")
input(
    "You are startled by rumbling roar, you have been beamed over to the Barren Mountains and it happens to be right in the path of a mountain troll."
)
print("")

#checking user's invetory to see if they could use an item
if len(playerInventory) != 0:
    useItem = input("Would you like to use an item? (yes or no): ").lower()
    print("")

    while useItem != "yes" and useItem != "no":  #checking for valid input
        useItem = input("Would you like to use an item? (yes or no): ")
        print("")

    #if they want to use and item then player inventory is shown to the user
    if useItem == "yes":
        print("Your inventory: ")
        for i in playerInventory:
            print("(" + str(playerInventory.index(i) + 1) + ")" +
                  (i.capitalize()))
        print("")

        #user selects the item they want to use
        selectItem = input("What item would you like to use?: ")

        #making inventory index equal to choosen item name
        itemSelect = playerInventory[int(selectItem) - 1]

#enemy battle: 7 (loops until user wins)
victory = False
while victory == False:

    #saving user's health incase they lose and have to restart battle
    battleHealth = playerHealth

    #assigns enemy health for the battle
    enemyHealth = enemyHP()

    #checking health to see if both can fight/continue to fight
    while enemyHealth >= 1 and playerHealth >= 1:

        #battle if item has been used
        if len(playerInventory) != 0:
            pDamage = 0
            if useItem == "yes":
                if itemSelect == "Stick" or itemSelect == "Brass Knuckles" or itemSelect == "Steel Club" or itemSelect == "Dagger" or itemSelect == "EPIC GAMER SWORD" or itemSelect == "Rubber Glove" or itemSelect == "Leather Armour" or itemSelect == "Chain Armour" or itemSelect == "Small Sheild" or itemSelect == "Big Sheild":
                    pass
                else:
                    playerInventory.pop(int(selectItem) - 1)
                pDamage = itemUse(itemSelect, playerHealth, pDamage)
                pDamage = pDamage[1] + playerAttack()

        #battle without the use of an item
            else:
                pDamage = playerAttack()
        else:
            pDamage = playerAttack()

        #taking away enemy health
        enemyHealth = enemyHealth - pDamage

        #checking if enemy is alive and can attack
        if enemyHealth < 1:  #if enemy is dead
            enemyHealth = 0
        print("You did " + str(pDamage) + " damage. The " + enemy +
              " health is at " + str(enemyHealth))
        if enemyHealth > 1:  #if enemy is still alive
            eDamage = enemyAttack()

            #taking away player health
            playerHealth = playerHealth - eDamage
            if playerHealth < 1:  #if player is dead
                playerHealth = 0
            print(enemy + " did " + str(eDamage) + " damage. You have " +
                  str(playerHealth) + " health left.")

    #if player won battle
    if enemyHealth < 1:
        print("")
        print("You won!")
        print("")
        input("You gained 25 Cryolar")
        playerMoney = playerMoney + 25  #adding reward
        victory = True  #exiting loop

    #if player lost
    if playerHealth < 1:
        print("")
        print("You lost! You have lost 5 Cryolar")
        playerMoney = playerMoney - 5  #taking fate
        print("")
        input(
            "You are startled by rumbling roar, you have been beamed over to the Barren Mountains and it happens to be right in the path of a mountain troll."
        )
        playerHealth = battleHealth  #resetting players health to redo battle
        victory = False  #staying in loop

print("")
input(
    "You defeated the Mountain Troll and it spins around before hitting the ground with a thud. The thud is so intense that the ground shakes beneath you. The shaking stops then turns into a powerful rumble."
)
print("")
input(
    "You look to your side and see an avalanche sliding down the side of a mountain. You try to flee but the snow consumes you."
)
print("")

#assigning harmful even damage
ranDamage()

input("You lost " + str(harm) + " health.")
print("")
input(
    ally +
    " digs you out from under the snow, but now you have to make it back to Durnatel and help your kingdom fight off the attack, the mountains are five kilometers north. So you and "
    + ally + " begin sprinting back.")
print("")

#randomly assigning enemy
battleSetup(enemies_one, enemies_two, enemies_three)
input(
    "As you are running back you feel the ground shaking beneath your feet once again, you turn back and see "
    + enemy)
print("")

#checking user's invetory to see if they could use an item
if len(playerInventory) != 0:
    useItem = input("Would you like to use an item? (yes or no): ").lower()
    print("")

    while useItem != "yes" and useItem != "no":  #checking for valid input
        useItem = input("Would you like to use an item? (yes or no): ")
        print("")

    #if they want to use and item then player inventory is shown to the user
    if useItem == "yes":
        print("Your inventory: ")
        for i in playerInventory:
            print("(" + str(playerInventory.index(i) + 1) + ")" +
                  (i.capitalize()))
        print("")

        #user selects the item they want to use
        selectItem = input("What item would you like to use?: ")

        #making inventory index equal to choosen item name
        itemSelect = playerInventory[int(selectItem) - 1]

#enemy battle: 8 (loops until user wins)
victory = False
while victory == False:

    #saving user's health incase they lose and have to restart battle
    battleHealth = playerHealth

    #assigns enemy health for the battle
    enemyHealth = enemyHP()

    #checking health to see if both can fight/continue to fight
    while enemyHealth >= 1 and playerHealth >= 1:

        #battle if item has been used
        if len(playerInventory) != 0:
            pDamage = 0
            if useItem == "yes":
                if itemSelect == "Stick" or itemSelect == "Brass Knuckles" or itemSelect == "Steel Club" or itemSelect == "Dagger" or itemSelect == "EPIC GAMER SWORD" or itemSelect == "Rubber Glove" or itemSelect == "Leather Armour" or itemSelect == "Chain Armour" or itemSelect == "Small Sheild" or itemSelect == "Big Sheild":
                    pass
                else:
                    playerInventory.pop(int(selectItem) - 1)
                pDamage = itemUse(itemSelect, playerHealth, pDamage)
                pDamage = pDamage[1] + playerAttack()

        #battle without the use of an item
            else:
                pDamage = playerAttack()
        else:
            pDamage = playerAttack()

        #taking away enemy health
        enemyHealth = enemyHealth - pDamage

        #checking if enemy is alive and can attack
        if enemyHealth < 1:  #if enemy is dead
            enemyHealth = 0
        print("You did " + str(pDamage) + " damage. The " + enemy +
              " health is at " + str(enemyHealth))
        if enemyHealth > 1:  #if enemy is still alive
            eDamage = enemyAttack()

            #taking away player health
            playerHealth = playerHealth - eDamage
            if playerHealth < 1:  #if player is dead
                playerHealth = 0
            print(enemy + " did " + str(eDamage) + " damage. You have " +
                  str(playerHealth) + " health left.")

    #if player won battle
    if enemyHealth < 1:
        print("")
        print("You won!")
        print("")
        input("You gained 25 Cryolar")
        playerMoney = playerMoney + 25  #adding reward
        victory = True  #exiting loop

    #if player lost
    if playerHealth < 1:
        print("")
        print("You lost! You have lost 5 Cryolar")
        playerMoney = playerMoney - 5  #taking fate
        print("")
        input(
            "As you are running back you feel the ground shaking beneath your feet once again, you turn back and see "
            + enemy)
        playerHealth = battleHealth  #resetting players health to redo battle
        victory = False  #staying in loop

print("")

#assigning harmful even damage
ranDamage()

input(
    "You help " + ally +
    " up and continue towards Durnatel, you come up over a hill and are hit in the face by a snowball, you lost "
    + str(harm) + " health")
print("")

#randomly assigning enemy
battleSetup(enemies_one, enemies_two, enemies_three)

print(ally + " runs to the " + enemy +
      " that threw the snowball and challenges it.")
print("")

#checking user's invetory to see if they could use an item
if len(playerInventory) != 0:
    useItem = input("Would you like to use an item? (yes or no): ").lower()
    print("")

    while useItem != "yes" and useItem != "no":  #checking for valid input
        useItem = input("Would you like to use an item? (yes or no): ")
        print("")

    #if they want to use and item then player inventory is shown to the user
    if useItem == "yes":
        print("Your inventory: ")
        for i in playerInventory:
            print("(" + str(playerInventory.index(i) + 1) + ")" +
                  (i.capitalize()))
        print("")

        #user selects the item they want to use
        selectItem = input("What item would you like to use?: ")

        #making inventory index equal to choosen item name
        itemSelect = playerInventory[int(selectItem) - 1]

#enemy battle: 9 (loops until user wins)
victory = False
while victory == False:

    #saving user's health incase they lose and have to restart battle
    battleHealth = playerHealth

    #assigns enemy health for the battle
    enemyHealth = enemyHP()

    #checking health to see if both can fight/continue to fight
    while enemyHealth >= 1 and playerHealth >= 1:

        #battle if item has been used
        if len(playerInventory) != 0:
            pDamage = 0
            if useItem == "yes":
                if itemSelect == "Stick" or itemSelect == "Brass Knuckles" or itemSelect == "Steel Club" or itemSelect == "Dagger" or itemSelect == "EPIC GAMER SWORD" or itemSelect == "Rubber Glove" or itemSelect == "Leather Armour" or itemSelect == "Chain Armour" or itemSelect == "Small Sheild" or itemSelect == "Big Sheild":
                    pass
                else:
                    playerInventory.pop(int(selectItem) - 1)
                pDamage = itemUse(itemSelect, playerHealth, pDamage)
                pDamage = pDamage[1] + playerAttack()

        #battle without the use of an item
            else:
                pDamage = playerAttack()
        else:
            pDamage = playerAttack()

        #taking away enemy health
        enemyHealth = enemyHealth - pDamage

        #checking if enemy is alive and can attack
        if enemyHealth < 1:  #if enemy is dead
            enemyHealth = 0
        print("You did " + str(pDamage) + " damage. The " + enemy +
              " health is at " + str(enemyHealth))
        if enemyHealth > 1:  #if enemy is still alive
            eDamage = enemyAttack()

            #taking away player health
            playerHealth = playerHealth - eDamage
            if playerHealth < 1:  #if player is dead
                playerHealth = 0
            print(enemy + " did " + str(eDamage) + " damage. You have " +
                  str(playerHealth) + " health left.")

    #if player won battle
    if enemyHealth < 1:
        print("")
        print("You won!")
        print("")
        input("You gained 25 Cryolar")
        playerMoney = playerMoney + 25  #adding reward
        victory = True  #exiting loop

    #if player lost
    if playerHealth < 1:
        print("")
        print("You lost! You have lost 5 Cryolar")
        playerMoney = playerMoney - 5  #taking fate
        print("")
        input(ally + " runs to the " + enemy +
              " that threw the snowball and challenges it.")
        playerHealth = battleHealth  # resetting players health to redo battle
        victory = False  #staying in loop

print("")
print(
    "You defeat the snowball throwing beast and charge towards the borders of Durnatel. As you approach the walls of the kingdom a wizard flies over the wall and blasts a spell towards you."
)
print("")

#checking user's invetory to see if they could use an item
if len(playerInventory) != 0:
    useItem = input("Would you like to use an item? (yes or no): ").lower()
    print("")

    while useItem != "yes" and useItem != "no":  #checking for valid input
        useItem = input("Would you like to use an item? (yes or no): ")
        print("")

    #if they want to use and item then player inventory is shown to the user
    if useItem == "yes":
        print("Your inventory: ")
        for i in playerInventory:
            print("(" + str(playerInventory.index(i) + 1) + ")" +
                  (i.capitalize()))
        print("")

        #user selects the item they want to use
        selectItem = input("What item would you like to use?: ")

        #making inventory index equal to choosen item name
        itemSelect = playerInventory[int(selectItem) - 1]

#enemy battle: 10 (loops until user wins)
victory = False
while victory == False:

    #saving user's health incase they lose and have to restart battle
    battleHealth = playerHealth

    #assigns enemy health for the battle
    enemyHealth = enemyHP()

    #checking health to see if both can fight/continue to fight
    while enemyHealth >= 1 and playerHealth >= 1:

        #battle if item has been used
        if len(playerInventory) != 0:
            pDamage = 0
            if useItem == "yes":
                if itemSelect == "Stick" or itemSelect == "Brass Knuckles" or itemSelect == "Steel Club" or itemSelect == "Dagger" or itemSelect == "EPIC GAMER SWORD" or itemSelect == "Rubber Glove" or itemSelect == "Leather Armour" or itemSelect == "Chain Armour" or itemSelect == "Small Sheild" or itemSelect == "Big Sheild":
                    pass
                else:
                    playerInventory.pop(int(selectItem) - 1)
                pDamage = itemUse(itemSelect, playerHealth, pDamage)
                pDamage = pDamage[1] + playerAttack()

        #battle without the use of an item
            else:
                pDamage = playerAttack()
        else:
            pDamage = playerAttack()

        #taking away enemy health
        enemyHealth = enemyHealth - pDamage

        #checking if enemy is alive and can attack
        if enemyHealth < 1:  #if enemy is dead
            enemyHealth = 0
        print("You did " + str(pDamage) + " damage. The " + enemy +
              " health is at " + str(enemyHealth))
        if enemyHealth > 1:  #if enemy is still alive
            eDamage = enemyAttack()

            #taking away player health
            playerHealth = playerHealth - eDamage
            if playerHealth < 1:  #if player is dead
                playerHealth = 0
            print(enemy + " did " + str(eDamage) + " damage. You have " +
                  str(playerHealth) + " health left.")

    #if player won battle
    if enemyHealth < 1:
        print("")
        print("You won!")
        print("")
        input("You gained 25 Cryolar")
        playerMoney = playerMoney + 25  #adding reward
        victory = True  #exiting loop

    #if player lost
    if playerHealth < 1:
        print("")
        print("You lost! You have lost 5 Cryolar")
        playerMoney = playerMoney - 5  #taking fate
        print("")
        input(
            "As you approach the walls of the kingdom a wizard flies over the wall and blasts a spell towards you."
        )
        playerHealth = battleHealth  #resetting players health to redo battle
        victory = False  #staying in loop

print(
    "The traveling merchant’s cart bursts through the gates, the driver sees you and quickly pulls over."
)
print("")

#asking user if they wanna shop
shopBuy = input(
    "Would you like to purchase something? All items only 50 Cryolar (yes or no): "
).lower()
while shopBuy != "yes" and shopBuy != "no":  #checking for valid input
    shopBuy = input("Would you like to purchase something? (yes or no): ")

#shop: 3
if shopBuy == "yes":
    item = shopping(shopItems)  #randomly selecting 5 items to sell
    print("For Sale: ")  #showing items for sale
    for i in item:
        print("(" + str(item.index(i) + 1) + ")" + (i.capitalize()))
    print("")
    print(" (a) Buy Item \n (b) Leave")
    print("")
    shopChoice = input("What would you like to do? (a or b): ").lower(
    )  #user selecting to buy or not
    while shopChoice != "a" and shopChoice != "b":  #checking for valid input
        shopChoice = input(
            shopChoice=input("What would you like to do? (a or b): "))

    if shopChoice == "a":
        print("")
        itemChoice = input("What item do to want to buy? (1, 2, 3, OR 4): ")
        while itemChoice != "1" and itemChoice != "2" and itemChoice != "3" and itemChoice != "4" and itemChoice != "5":  #checking for valid input
            itemChoice = input("What item do to want to buy?: ")

        #checking users input and steps into required function
        if itemChoice == "1" or itemChoice == "2" or itemChoice == "3" or itemChoice == "4" or itemChoice == "5":

            #adding item to players inventory
            playerInventory.append(item[int(itemChoice) - 1])
            playerMoney = playerMoney - 30  #taking money from player
        print(item[int(itemChoice) - 1] +
              " has been added to your inventory. You have " +
              str(playerMoney) + " Cryalor.")
    else:
        print("Don't waste my time, you fool!")

print("")
input(
    "You make it inside the walls and make your way towards the giant wizard lord. The town is in shambles and still on fire. The kingdoms army is running around frantically trying to protect the king and take down the wizard lord, but many of the guards have been turned into frogs. "
)
print("")
input("You return to the feet of the wizard and yell once again.")
print("")
print("The Wizard Lord replys back, “ It's on mortal”.")
print("")

#checking user's invetory to see if they could use an item
if len(playerInventory) != 0:
    useItem = input("Would you like to use an item? (yes or no): ").lower()
    print("")

    while useItem != "yes" and useItem != "no":  #checking for valid input
        useItem = input("Would you like to use an item? (yes or no): ")
        print("")

    #if they want to use and item then player inventory is shown to the user
    if useItem == "yes":
        print("Your inventory: ")
        for i in playerInventory:
            print("(" + str(playerInventory.index(i) + 1) + ")" +
                  (i.capitalize()))
        print("")

        #user selects the item they want to use
        selectItem = input("What item would you like to use?: ")

        #making inventory index equal to choosen item name
        itemSelect = playerInventory[int(selectItem) - 1]

#boss battle: The Wizard Lord (loops until player wins)
victory = False
while victory == False:

    battleHealth = playerHealth  #saving players health incase of redo
    bossHealth = bossHP()  #assigns boss health for battle

    #checking health to see if both can fight/continue to fight
    while bossHealth >= 1 and playerHealth >= 1:

        #battle if item has been used
        if len(playerInventory) != 0:
            pDamage = 0
            if useItem == "yes":
                if itemSelect == "Stick" or itemSelect == "Brass Knuckles" or itemSelect == "Steel Club" or itemSelect == "Dagger" or itemSelect == "EPIC GAMER SWORD" or itemSelect == "Rubber Glove" or itemSelect == "Leather Armour" or itemSelect == "Chain Armour" or itemSelect == "Small Sheild" or itemSelect == "Big Sheild":
                    pass
                else:
                    playerInventory.pop(int(selectItem) - 1)
                pDamage = itemUse(itemSelect, playerHealth, pDamage)
                pDamage = pDamage[1] + playerAttack()

        #battle without the use of an item
            else:
                pDamage = playerAttack()
        else:
            pDamage = playerAttack()

        #taking away boss health
        bossHealth = bossHealth - pDamage

        #checking if boss is alive and can attack
        if bossHealth < 1:  #if boss is dead
            bossHealth = 0
        print("You did " + str(pDamage) +
              " damage. The Wizard Lord's health is at " + str(bossHealth))
        if bossHealth > 1:  #if boss is still alive
            bDamage = bossAttack()

            #taking away player health
            playerHealth = playerHealth - bDamage
            if playerHealth < 1:  #if player is dead
                playerHealth = 0
            print(" The Wizard Lord " + str(bDamage) + " damage. You have " +
                  str(playerHealth) + " health left.")

    #if player won battle
    if bossHealth < 1:
        print("")
        print("You won!")
        print("")
        print("You gained 100 Cryolar")
        playerMoney = playerMoney + 100  #adding reward
        playerHealth = originalHealth
        victory = True  #exiting loop

    #if player lost
    if playerHealth < 1:
        playerHealth = 0
        print("")
        print("You lost! You have lost 10 Cryolar")
        playerMoney = playerMoney - 10  #taking fate
        print("")
        input("The Wizard Lord Challeneges you!")
        playerHealth = battleHealth  #reseting player health to try the battle again
        victory = False  #staying in loop

print("")
input(
    "You fought a hard and brutal battle against the wizard lord, but it is now over. The wizard minions flee on their brooms "
)
print("")
input(
    "You and " + ally +
    " are rewarded and the kingdom of Durnatel was eventually rebuilt and once again peaceful."
)
print("")
print("Thank you for playing :)")
