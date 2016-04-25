import yaml #allows me to load the dictionay from monsters.py
import printCharInfo
import charToFile
def NPCChara(NPC):
    print("\nYou are creating a non-playable character.")
    name=input("Enter Character Name: ")
    race=input("Race: ")
    race_=race.replace(" ","_").lower()
    with open("monsters.py",'r') as file:
        for line in file: #iterate through the file until the dictionary name matches the input race
            file_race,traits=line.split("=") #turn the string given from opening the file into 2 strings
            if file_race == race_: 
                f=yaml.load(traits) #turn the 
                yn=input("I have information already stored about this race \n Would you like to view it? (y/n)")
                if yn.lower() == "y":
                    for key , value in f.items():
                        print(key,'-',value)

                #     yn=input("Would you like me to append this to the end of your character's file?")
                #     if yn.lower()=="y":
                #         with open(race+name+"dict.txt",'w') as savefile:
                #             for key , value in f.items():
                #                 savefile.write(key,'-',value)
                # if yn.lower()=="n":
            if line =="":
                print("I couldn't find that race. Here's a list of races I have saved.")
                with open('monsters_list.txt','r') as monsters:
                    print(monsters)
    LvLtype=False
    EXPtype=False  
    Class=input("Enter Class: ")
    while LvLtype !=True:
        try:
            LvL=int(input("Level: "))
            LvLtype=True
        except ValueError:
            print("Incorrect value type. Please enter an integer.")
    Alin=input("Alignment: ")
    while EXPtype !=True:
        try:
            EXP=int(input("Experience Points: "))
            EXPtype=True
        except ValueError:
            print("Incorrect value type. Please enter an integer.")
    PN=input("Player Name: ")
    print("")
    Player={"Name":name,
            "Class":Class,
            "Level":LvL,
            "Race":race,
            "Alignment":Alin,
            "Exp":EXP,
            "Player Name":PN}
    printCharInfo.printCharInfo(Player)
    yn=input("Is this information correct? (yes/no): " )
    if yn=="yes":
        charToFile.charToFile(Player)
NPCChara("bob")