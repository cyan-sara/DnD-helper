# Character Information
# Using file;Dictionaries 
# Goal is to turn all the sheets into files'
#Lower cases Key Values
#Would you like input the story of your character? (File input)
#Ask if NPC or Playable Character



def PlayableChara(player):
    Player={}
    print("\nYou are creating a playable character.")
    name=input("Enter Character Name: ")
    Class=input("Enter Class: ")
    LvL=int(input("Level: "))
    race=input("Race: ")
    Alin=input("Alignment: ")
    EXP=int(input("Experience Points: "))
    PN=input("Player Name: ")
    Player["name"]= name
    print("")
    print(Player)

    return Player

def NPCChara(NPC):
    print("\nYou are creating a non-playable character.")
    name=input("Enter Character Name: ")
    Class=input("Enter Class: ")
    LvL=int(input("Level: "))
    race=input("Race: ")
    Alin=input("Alignment: ")
    EXP=int(input("Experience Points: "))
    PN=input("Player Name: ")
    Player["name"]= name
    print("")
    print(Player)

    return NPC
