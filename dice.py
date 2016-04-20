import random

def diceroll():
    rollagain="y"

    while rollagain=="y":
        dmax=0
        while dmax==0:
            try:
                dmax=int(input("How many sides? \n"))
            except ValueError:
                print("Incorrect value detected. Please enter a positive integer.")

        min=1
        max=dmax

        print("Rolling...")
        print(random.randint(min,max))

        rollagain=input("Roll again? (y/n)")
        

diceroll()
