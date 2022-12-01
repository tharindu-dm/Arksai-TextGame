#ARKSAINT - Gameplay

#player profile
currency = 10_000 #refered as CC
decision = ""

weapon = "None"
atk = 70; deff = 40; spd = 50
hp = 500; mp = 800
PlayerItems = ["Money bag"]; title = ["Demon slayer", "Knight", "Survivor", "Ranker"]

#ALL ITEMS AT gamepoints
item_g1 = ["Dagger (weapon)", "Drawstring cloth bag", "Unkown book"]
# unknown book is a grimory - can't read until magic is known.

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
#save point 1
    print("\nYou see a small village down side of the mountain\n")
    decision = input("\n(1)Go to village\n(2)Look around\n(3)Check Status\nYOUR CHOICE\t: ")
    if decision == "1":
        print("You went back and found the road leading to the village. You decided to walk along and you finally reached the village entrance.\n")
        input("")
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

def villageGamePoint():
    print("You Entered the village.")
    print("\n(1)Go to Adventurers' Guild\n(2)Look around\n(3)Check Status\n")
    decision = input("YOUR CHOICE\t: ")
    if decision == "1":
        print("You went back and found the road leading to the village. You decided to walk along and you finally reached the village entrance.\n")
        input("")
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
        
        villageGamePoint()  
    else:
        print("Wrong input\n")
        
        villageGamePoint()
        
while True:     #getting player name
    plyName = input("\nEnter player Name (10 characters)\t: ")
    if len(plyName) > 10:
        print("Invalid Player name.")
        continue
    else:
        break
print("WELCOME", plyName, ", to ARKSAI\nTHE story unfolds.....\n\n")

#game begins here
    #Realisation
print("Press Enter to continue dialogues\nPress required key only, for Actions\n")
input("\nUnkown voice : Wake up child!")
input("\nHuh? What? Where am I? Who are you?")
input("\nUnkown voice : I am the supreme one. One shall not disclose more")
input("\n...")
input("\nSupreme one : Child, you are the chosen one! Now go and get em boy")
#seriously! fix this dialogue set

    #After reincarnation
print("\nYou open your eyes under an orange-leaved tree on a cliff.")
initialGamePoint()
villageGamePoint()

