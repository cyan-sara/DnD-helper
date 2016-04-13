# I will be doing the main file, which includes: 
	#version picker,
	#turn tracker,
	#data retrieval on characters

import #Tanner
import #Sara
import #Bianca

def main():
	print("This program serves as a helper for Dungeons and Dragons DMs.")
	version = input("Please select your version number: ") #this will affect the books that we have. Might get tossed if we can't do books
	
	
def characterselect(): #selects characters to be used. Allows addition of new chars (executes Bianca's module)
	print("Enter the characters that are going on this encounter. Enter \"end\" to show the end of the list.")
	characters = []
	while True:
		x = input("")
		if x == "end":
			break
		characters.append(x)
	try: #use list "characters" to grab files/execute new char creator
	except IOError:
		print("Character \"", x, "\" not found. Would you like to add a new character?")
		
def turn_count(): #keeps track of turns for status effect purposes, etc
	yn = input("Are you ready to start the encounter? (y/n)")
	if yn == "y":
		count = int(input("Enter the turn number you wish to start on."))
