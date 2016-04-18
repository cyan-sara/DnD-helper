import random

def diceroll():
    rollagain="y"

    while rollagain=="y":
        dmax=int(input("How many sides? \n"))

        min=1
        max=dmax

        print("Rolling...")
        print(random.randint(min,max))

        rollagain=input("Roll again? (y/n)")
        

