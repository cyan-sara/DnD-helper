# I will be doing the main file, which includes: 
	#version picker,
	#turn tracker,
	#data retrieval on characters

import #Tanner
import #Sara
import #Bianca

def main():
	print("This program serves as a helper for Dungeons and Dragons (version 5) DMs.")
	turncount = turn_begin()
			
def turn_begin(): #keeps track of turns for status effect purposes, etc
	yn = input("Are you ready to start the encounter? (y/n)")
	count = 0
	if yn == "y":
		count += int(input("Enter the turn number you wish to start on."))
	print("Current turn:", count)
	return count
	
main()