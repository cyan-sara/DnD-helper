import monsters
NPC="bob"
def NPCChara(NPC):
    print("\nYou are creating a non-playable character.")
    name=input("Enter Character Name: ")
    race=input("Race: ")
    with open("monsters.py",'r') as file:
        for line in file:
            if line.rstrip() == race.lower().rstrip():
                racefound=line
        yn=input("I have information already stored about this race \n Would you like to view it?")
        if yn == "y":
            print(monsters.aboleth)
    # Class=input("Enter Class: ")
    # LvL=int(input("Level: "))

    # Alin=input("Alignment: ")
    # EXP=int(input("Experience Points: "))
    # PN=input("Player Name: ")
    # Player["name"]= name
    # print("")
    # print(Player)

    # return NPC
NPCChara(NPC)
