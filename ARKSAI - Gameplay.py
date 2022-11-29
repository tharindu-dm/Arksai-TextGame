#ARKSAI - Gameplay

currency = 10_000 #refered as CC
decision = ""

weapon = "None"
atk = 70; deff = 40; spd = 50
hp = 500; mp = 800
items = ["Money bag", "Dagegr", "Permission slipt"]; title = ["Demon slayer", "Knight", "Survivor", "Ranker"]

#ALL functions
def profile(player):  #display profiel status
    print("\n===== Profile Data =====")
    print("\nName:", player,"\nTitles\n", title)
    print("\nHP\t:", hp, "\nMP\t:", mp)
    print("\nAtk: ", atk, "\nDef: ", deff, "\nSpd: ", spd)
    print("\nMoney at hand:", currency,"CC")
    print("Items in inventory:\n", items, end='')
    input("")
    
    
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
input("\nSupreme one : Child, you are the chosen one! Now go and get em boy") #seriously! fix this dialogue set

    #After reincarnation
print("\nYou open your eyes under an orange-leaved tree on a cliff.\nYou see a small village down side of the mountain\n")
decision = input("\n(1)Go to village\n(2)Look around\n(3)Check Status\nYOUR CHOICE\t: ")
if decision == "1":
    #go to village
    x = 10
elif decision == "2":
    #Look around >> dagger, storage
    c = 5
else:
    #Check profile stats
    profile(plyName)

