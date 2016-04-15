# I will be doing the main file, which includes: 
	#version picker,
	#turn tracker,
	#data retrieval on characters

#Tanner
#Sara
#Bianca

def main():
	print("This program serves as a helper for Dungeons and Dragons (version 5, no homebrewing) DMs.")
	char_creator()
	turncount = encount_begin()
	while True:
		x= input("What would you like to do next? Add character, roll dice, end turn, end encounter. ")
		x = x.lower().rstrip()
		if x=="end turn":
			turncount += 1
			print("Current turn:", turncount)
		elif x == "add character":
			char_creator()
		elif x == "roll dice":
			print()
			#execute dice roller
		elif x == "end encounter":
			break
		else:
			print("Invalid command.")
	print("Goodbye!")

def char_creator():
	yn = input("Would you like to create a new character? (y/n) ")
	if yn == "y":
		print()
		#run character creator
	else:
		exist = input("Would you like to load saved character(s)? (y/n) ")
		if exist == "y":
			charx = input("Enter the character(s) you would like to load. (Tab between each) ")
			print(charx.split())
			
			
def encount_begin(): #keeps track of turns for status effect purposes, etc
	yn = input("Are you ready to start the encounter? (y/n)")
	count = 0
	if yn == "y":
		count += int(input("Enter the turn number you wish to start on."))
	print("Current turn:", count)
	return count
	
main()