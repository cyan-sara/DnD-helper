#Character Information
#Goal is to turn all the sheets into files
#def Playable():?

import printCharInfo
import charToFile

def main():
    LvLtype=False
    EXPtype=False    
    print("\nYou are creating a playable character.")
    name=input("Enter Character Name: ")
    Class=input("Enter Class: ")
    while LvLtype !=True:
        try:
            LvL=int(input("Level: "))
            LvLtype=True
        except ValueError:
            print("Incorrect value type. Please enter an integer.")
    race=input("Race: ")
    Alin=input("Alignment: ")
    while EXPtype !=True:
        try:
            EXP=int(input("Experience Points: "))
            EXPtype=True
        except ValueError:
            print("Incorrect value type. Please enter an integer.")
    PN=input("Player Name: ")
    print("")
    
    Player={"Name":name,"Class":Class,"Level":LvL,"Race":race,"Alignment":Alin,"Exp":EXP,"Player Name":PN}
    printCharInfo.printCharInfo(Player)
    
    #if yes: save to dictionary file
    #if no: ask if "Try again?"
    #if yes: loop
    #if no: return to main menu

    yn=input("Is this information correct? (yes/no): " )
    if yn=="yes":
        charToFile.charToFile(Player)
        return Player
    elif yn=="no":
        TryAgain=input("Try again? (yes/no): ")
        if TryAgain=="no":
            pass

    



