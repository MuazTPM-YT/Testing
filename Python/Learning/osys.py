import random
from time import sleep

def calculator(x,y,symbol):
    if symbol == "+":
        print(x+y)

    elif symbol == "-":
        print(x-y)

    elif symbol == "*":
        print(x*y)

    elif symbol == "/":
        if x == 0:
            print("Division by 0 is not possible")
        elif y == 0:
            print("Division by 0 is not possible")
        else:
            print(x/y)

    else:
        print("Invalid Option!")

    sleep(3)

def game(guess):
    random_num = random.randint(1,5)
    if guess == random_num:
        print("You Won!")
    else:
        print("You Lost!")

    sleep(3)

def rps(player):
    choices = ("Rock", "Paper", "Scissors")
    computer = random.choice(choices)

    if player.capitalize() == computer:
        print("-----IT'S A TIE!-----")
    
    elif player.capitalize() == "Rock" and computer == "Paper":
        print("------YOU LOST!------")

    elif player.capitalize() == "Rock" and computer == "Scissors":
        print("------YOU WON!------")

    elif player.capitalize() == "Paper" and computer == "Rock":
        print("------YOU WON!------")

    elif player.capitalize() == "Paper" and computer == "Scissors":
        print("------YOU LOST!------")

    elif player.capitalize() == "Scissors" and computer == "Rock":
        print("------YOU LOST!------")

    elif player.capitalize() == "Scissors" and computer == "Paper":
        print("------YOU WON!------")

    else:
        return print("Invalid Input!")

    print(f"Your Choice: {player}")
    print(f"CPU's Choice: {computer}")

    sleep(3)

def operating_system():
    print("""
What task would you like to do?
A. Calculator
B. Guessing Game
C. Rock, Paper, Scissors
""")
    user = input("> ").upper()

    if user == "A":
        num1=int(input("Enter first number: "))
        symbol = input("Enter a symbol (+ - * /): ")
        num2=int(input("Enter second number: "))

        calculator(num1,num2,symbol)

    elif user == "B":
        guess = int(input("Guess: ").lower())

        game(guess)

    elif user == "C":
        player_choice = input("Choose (Rock, Paper, Scissors): ").lower()

        rps(player_choice)

    else:
        print("We don't have such instructions yet.")

while True:
    operating_system()