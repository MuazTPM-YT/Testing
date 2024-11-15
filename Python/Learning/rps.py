import random

class RockPaperScissors:
    def __init__(self):
        self.options = ("Rock", "Paper", "Scissors")
        self.computer = random.choice(self.options)

    def system(self):
        while True:
            self.choice = input("Choose (Rock, Paper, Scissors): ").capitalize()

            if self.choice == self.computer:
                print("---------------------")
                print("-----IT'S A TIE!-----")
                print("---------------------")
                self.results()
                break

            elif self.choice == "Rock" and self.computer == "Paper":
                print("---------------------")
                print("------YOU LOST!------")
                print("---------------------")
                self.results()
                break

            elif self.choice == "Rock" and self.computer == "Scissors":
                print("--------------------")
                print("------YOU WON!------")
                print("--------------------")
                self.results()
                break

            elif self.choice == "Paper" and self.computer == "Rock":
                print("--------------------")
                print("------YOU WON!------")
                print("--------------------")
                self.results()
                break

            elif self.choice == "Paper" and self.computer == "Scissors":
                self.results()
                print("---------------------")
                print("------YOU LOST!------")
                print("---------------------")
                self.results()
                break

            elif self.choice == "Scissors" and self.computer == "Rock":
                print("---------------------")
                print("------YOU LOST!------")
                print("---------------------")
                self.results()
                break

            elif self.choice == "Scissors" and self.computer == "Paper":
                print("--------------------")
                print("------YOU WON!------")
                print("--------------------")
                self.results()
                break

            else:
                print("Invalid Option!")

    def results(self):
        print(f"Your Choice: {self.choice}")
        print(f"CPU's Choice: {self.computer}")
        print("---------------------")

if __name__ == "__main__":
    rps = RockPaperScissors()
    rps.system()