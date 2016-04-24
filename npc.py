def NPCChara(NPC):
    print("\nYou are creating a non-playable character.")
    name=input("Enter Character Name: ")
    race=input("Race: ")
    race=race.replace(" ","_").lower()
    with open("monsters.py",'r') as file:
        for line in file:
            line=str(line)
            file_race,traits=line.rstrip().split("=")
            if file_race == race:
                print(file_race)
                racefound=traits
                
        yn=input("I have information already stored about this race \n Would you like to view it?")
        if yn == "y":
            print(racefound)
    # Class=input("Enter Class: ")
    # LvL=int(input("Level: "))

    # Alin=input("Alignment: ")
    # EXP=int(input("Experience Points: "))
    # PN=input("Player Name: ")
    # Player["name"]= name
    # print("")
    # print(Player)

    # return NPC
NPCChara(
