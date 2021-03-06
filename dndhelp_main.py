# I will be doing the main file, which includes: 
#turn tracker,
#data retrieval on characters,
#calls for all functions

import dice #Tanner
import npc #Sara
import CharacterInformation #Bianca
import loadCharacter #Tanner
activeCharacter=[]

def main():
	print("This program serves as a helper for Dungeons and Dragons DMs (version 5, no homebrewing). Type 'help' for a list of commands.")
	char_creator()
	turncount = encount_begin()
	while True:
		x= input("\nWhat would you like to do next? ")
		x = x.lower().rstrip()
		if x=="end turn":
			turncount += 1
			print("Current turn:", turncount)
		elif x == "add character":
			char_creator()
		elif x == "roll dice":
			dice.diceroll()
		elif x == "end encounter":
			break
		elif x == "help":
			help()
		else:
			print("I don't understand", "'"+x+"'.", "Type 'help' for a list of commands. ")
	print("\nGoodbye!")

def char_creator():
	yn = input("\nWould you like to create a new character? (y/n) ")
	charx = ""
	if yn == "y":
		NPC = input("Is this character an NPC? (y/n) ")
		if NPC == "y":
			npc.NPCChara("bob")
		else:
			activeCharacter.append(CharacterInformation.main())
			
	else:
		exist = input("Would you like to load saved character(s)? (y/n) ")
		if exist == "y":
			charx = input("Enter the character(s) you would like to load. (Space between each) ")
	if charx != "":
		charx=charx.split()
		

		for value in charx:
			try:
				print()
				activeCharacter.append(loadCharacter.loadCharacter(value))
				print("Successfully activated character:", value)
				print()
		
	
			except IOError:
				restart = input("Character " + value + " not found. Would you like to create a new one? (y/n) ")
				if restart == "y":
					activeCharacter.append(CharacterInformation.main())
			
def encount_begin(): #keeps track of turns for status effect purposes, etc
	yn = input("\nAre you ready to start the encounter? (y/n) ")
	print()
	count = 0
	if yn == "y":
		if len(activeCharacter) != 0:
			print("Active Characters are:",end=" ")
			itemN=1
			for item in activeCharacter:
				charName=item["Name"]
				if itemN<len(activeCharacter):
					print(charName+",",end=" ")
					itemN+=1
				elif itemN==len(activeCharacter):
					print(charName+".")
				
				else:
					print("and",charName+".")

			print()
			print("Have fun storming the castle!")
		count += int(input("\nEnter the turn number you wish to start on. "))
	print("Current turn:", count)
	return count

def help():
	print()
	print("Type 'add character' to add or load a character.")
	print("Type 'roll dice' to roll a die.")
	print("Type 'end turn' to end the turn.")
	print("Type 'end encounter' to end this encounter.")

main()
