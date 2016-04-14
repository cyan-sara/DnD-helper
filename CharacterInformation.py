# Character Information
# Using file;Dictionaries 
# Goal is to turn all the sheets into files'
#Lower cases Key Values
#Would you like input the story of your character? (File input)


def main():
    D1={}    
    while True:
        yn=input("Would you like to create a character? (y/n) ")
        if yn=="n":
            break
        name=input("Enter Character Name: ")
        Class=input("Enter Class: ")
        LvL=int(input("Level: "))
        race=input("Race: ")
        Alin=input("Alignment: ")
        EXP=int(input("Experience Points: "))
        PN=input("Player Name: ")
        print("")
        
    print(D1)

main()

