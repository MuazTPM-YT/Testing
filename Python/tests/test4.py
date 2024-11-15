import random
import time

class RPS:
    def __init__(self):
        self.choices = [
            "rock",
            "paper",
            "scissors"
        ]

    def main(self):
        while True:  
            choice = input("What would you like to do? [Rock] [Paper] [Scissors]: ").lower()
            computer_choice_value = random.randint(0,2)
            computer_choice = self.choices[computer_choice_value]

            print(f"You chose: {choice}\nComputer chose: {computer_choice}")

            time.sleep(3)

            if choice == computer_choice:
                print("Draw!")

            elif choice == "rock" and computer_choice == "paper":
                print("You Lose!")

            elif choice == "rock" and computer_choice == "scissors":
                print("You Win!")

            elif choice == "paper" and computer_choice == "rock":
                print("You Win!")

            elif choice == "paper" and computer_choice == "scissors":
                print("You Lose!")
            
            elif choice == "scissors" and computer_choice == "rock":
                print("You Lose!")

            elif choice == "scissors" and computer_choice == "paper":
                print("You Win!")

            else:
                print("Invalid Option!")

RPS().main()