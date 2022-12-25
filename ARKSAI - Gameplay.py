#ARKSAINT - Gameplay

#player profile     (should have the abilitiy to Create and save text files in player names)
currency = 10000 #refered as CC
decision = ""

weapon = "None"
atk = 70; deff = 40; spd = 50
hp = 500; mp = 800
PlayerItems = ["Money bag"];
title = []
rank = ''

#ALL ITEMS AT gamepoints(g<num>)
item_g1 = ["Dagger (weapon)", "Drawstring cloth bag", "Unkown book"] # unknown book is a grimory - can't read until magic is known.


#ALL functions
def profile(player):  #display profiel status
    print("\n===== Profile Data =====")
    print("\nName:", player,"\nTitles\n", title)
    print("\nHP\t:", hp, "\nMP\t:", mp)
    print("\nAtk: ", atk, "\nDef: ", deff, "\nSpd: ", spd)
    print("\nMoney at hand:", currency,"CC")
    print("Items in inventory:\n", PlayerItems, end='')
    input("")
    
def initialGamePoint():
    #Starting Point
    print("\nYou see a small village down side of the mountain\n")
    decision = input("\n(1)Go to village\n(2)Look around\n(3)Check Status\nYOUR CHOICE\t: ")

    if decision == "1":
        print("You went back and found the road leading to the village. You decided to walk along and you finally reached the village entrance.")
        input("")
        villageOUTGamePoint()

    elif decision == "2":
        if(len(item_g1) > 0):
            print("You found some items near the foot of the tree and decided to get them all.")
            print("You obtained\n", item_g1)
            for i in item_g1:
                PlayerItems.append(i)
            item_g1.clear()

        else:
            print("There's nothing more than a beautiful scenery")
        
        initialGamePoint()

    elif decision == "3":
        profile(plyName)
        initialGamePoint()  

    else:
        print("Wrong input\n")
        initialGamePoint()

def villageOUTGamePoint():  #Exit/Outside the village
    #enter? dungeon? mountain?
    print("\nYou are outside the village\n")

    #add conditons decisions. for now directly entiring the village
    input("You decided to enter the village\n")
    villageINGamePoint()

def villageINGamePoint():   #Enter/Inside the village
    print("You're in the village.")
    
    print("\n(1)Go to Adventurers' Guild\n(2)Visit Library\n(3)Check Status\n(4)Access Inventory\n(5)Check Medical Center\n")
    print("(6)Go to Blacksmith\n(7)Checkout Souvernir Shop\n(11)Exit Village\n")
    
    decision = input("YOUR CHOICE\t: ")
    
    if decision == "1":     #Adventurers' guild
        print("You walk toward the advevnturers' guild (Flaming Hearts) and meet the receptionist.\n")
        adv_guildGamePoint()
        villageINGamePoint()

    elif decision == "2":   #Visit Library
        #count visit times
        libraryGamePoint()
        
        villageINGamePoint()
    elif decision == "3":
        profile(plyName)
        
        villageINGamePoint()  
    elif decision == "4":
        profile(plyName)
        
        villageINGamePoint()  
    elif decision == "5":
        profile(plyName)
        
        villageINGamePoint()  
    elif decision == "6":
        profile(plyName)
        
        villageINGamePoint()  
    elif decision == "7":
        profile(plyName)
        
        villageINGamePoint()  
    elif decision == "11":
        villageOUTGamePoint()
        
    else:
        print("Wrong input\n")
        villageINGamePoint()

def adv_guildGamePoint():   #Enter/Inside Adventure guild
    input("\nWelcome to the adventurers' guild! May I know your inquiry?\n")
    print("(1) Become an adventurer\n(2)Check quests\n(3)Sell items\n(11)Good bye!\n")
    
    decision = input("YOUR CHOICE\t: ")
    if(decision == "1" and "Adventurer" not in title):  #becomes an adventurer
        input("\nReceptionist : Please fill your details in this form.")
        input("\n\t......You fill all the requested details......")
        input("\nReceptionist : Hmm...")
        input("\nReceptionist : Look alright! Please wait. I'll register you as an adventurer")
        input("\nHalf an hour later...")
        input("\nReceptionist : Congratulations! You are officiallay an Adventuere.")
        input("\nReceptionist : Your starter rank is 'D'. More expereince you get, quicker you move to a higher rank.")
        input("\n\n SYSTEM: Achievement: ADVENTURER\n(title: Adventurer obtained)\n +1000CC")

        global currency
        currency += 1000
        title.append("Adventurer")
        adv_guildGamePoint()

    elif(decision == "2"):
        print("")

    elif(decision == "3"):
        print("")

    elif(decision == "11"):
        villageINGamePoint()

    else:
        print("Invalid Input")
        adv_guildGamePoint()

def libraryGamePoint():
    print("The library is still under constructions and the requested books are not imported yet.\n")
    villageINGamePoint()

def medicalCenterGamePoint():
    print("")

def blacksmithGamePoint():
    print("")

def souvernirShopGamePoint():
    print("")


#GETTING Player Name
while True:
    plyName = input("\nEnter player Name (10 characters)\t: ")
    if len(plyName) > 10:
        print("Invalid Player name.")
        continue
    else:
        break
print("WELCOME", plyName, ", to ARKSAI\nTHE story unfolds.....\n\n")

#GAME begins here
    #Stage 0
print("Press Enter to continue dialogues\nPress required key only, for Actions\n")
input("\nUnkown voice : Wake up child!")
input("\nHuh? What? Where am I? Who are you?")
input("\nUnkown voice : I am the supreme one. One shall not disclose more")
input("\n...")
input("\nSupreme one : Child, you are the chosen one! Now go and get em boy")
#seriously! fix this dialogue set

    #Stage 1
print("\nYou open your eyes under an orange-leaved tree on a cliff.")
initialGamePoint()
villageOUTGamePoint()





