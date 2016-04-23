# The purpose of this module is to recall the character info as a dicitonary
# so that it could be used by the main module.

def loadCharacter(charName):
    
    d={}
    keyValue=0
    with open(charName+".txt", "r") as fo:
        for line in fo:
            splitline=line.strip()
            if keyValue == 0:
                key=splitline
                keyValue+=1
            elif keyValue == 1:
                value=splitline
                keyValue-=1
                d[key]=value

    upperName=charName.upper()
    print("Character",upperName,"successfully loaded.") 
    print("Name:",d["Name"])
    print("Class:",d["Class"])
    print("Level:",d["Level"])
    print("Race:",d["Race"])
    print("Alignment:",d["Alignment"])
    print("Exp:",d["Exp"])
    print("Player Name:",d["Player Name"])
    
    return d

