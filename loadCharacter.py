# The purpose of this module is to recall the character info as a dicitonary
# so that it could be used by the main module.

def loadCharacter(charName):
    
    d={}
    keyValue=0
    with open(charName+".txt", "r") as fo:
        for line in fo:
            if keyValue == 0:
                print(line)


charName="Tanner"
loadCharacter(charName)
