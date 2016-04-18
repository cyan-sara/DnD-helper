import random

rollagain="yes"

while rollagain=="yes":
    dmax=int(input("How many sides? \n"))

    min=1
    max=dmax

    print("Rolling...")
    print(random.randint(min,max))

    rollagain=input("Roll again? (yes/no)")
    

