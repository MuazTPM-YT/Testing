import random

class Game:
    def __init__(self):
        self.random_num = random.randint(1,5)

    def system(self):
        guess = int(input("Guess a number: "))

        if guess == self.random_num:
            print("You Win!")

        else:
            print(f"You Lose! The number was {self.random_num}")

if __name__ == "__main__":
    game = Game()
    game.system()