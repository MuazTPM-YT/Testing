import random

def dice():
    random_num = random.randint(1,6)
    return random_num

while True:
    user = input("Roll The Dice? (Yes or No): ").lower()
    
    if user == "yes":
        print("You rolled a:".dice())
        
    elif user == "no":
        print("Have a good day!")
        break

    else:
        print("Invalid Input!")