#Takes the dictionary from the player creator and turns it into a file that
# be recalled by the main function.

def charToFile(Player):
    p0 = "Name"
    p0v = Player["Name"]
    p1 = "Class"
    p1v = Player["Class"]
    p2 = "Level"
    p2v = str(Player["Level"])
    p3 = "Race"
    p3v = Player["Race"]
    p4 = "Alignment"
    p4v = Player["Alignment"]
    p5 = "Exp"
    p5v = str(Player["Exp"])
    p6 = "Player Name"
    p6v = Player["Player Name"]

    
    fo = open(Player["Name"]+".txt", "w")
    fo.write(p0+"\n")
    fo.write(p0v+"\n")
    fo.write(p1+"\n")
    fo.write(p1v+"\n")
    fo.write(p2+"\n")
    fo.write(p2v+"\n")
    fo.write(p3+"\n")
    fo.write(p3v+"\n")
    fo.write(p4+"\n")
    fo.write(p4v+"\n")
    fo.write(p5+"\n")
    fo.write(p5v+"\n")
    fo.write(p6+"\n")
    fo.write(p6v+"\n")
    fo.close
    print("File Saved.")
