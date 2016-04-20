# Character Information
# Using file;Dictionaries 
# Goal is to turn all the sheets into files'
#Lower cases Key Values

#def Playable():
import printCharInfo

def main():
    print("\nYou are creating a playable character.")
    
    name=input("Enter Character Name: ")
    Class=input("Enter Class: ")
    LvL=int(input("Level: "))
    race=input("Race: ")
    Alin=input("Alignment: ")
    EXP=int(input("Experience Points: "))
    PN=input("Player Name: ")
    print("")
    Player={"Name":name,"Class":Class,"Level":LvL,"Race":race,"Alignment":Alin,"Exp":EXP,"Player Name":PN}
    
    printCharInfo.printCharInfo(Player)
    
main()
#return Player


