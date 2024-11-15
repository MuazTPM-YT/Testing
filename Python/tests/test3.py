import random
import time
import math

class RandomNumberGenerator():
    def __init__ (self):
        self.Guess = int()
        self.Retry = 1
        self.parameter = 2

    def Game_File(self):
        while True:
            self.Guess = int(input(" Enter your guess here: "))

            rng_system = random.randint(1 , self.parameter)

            if self.Guess == rng_system:
                print("Wow you guessed it!")
                self.parameter *= 2

            else:
                self.Retry = 0
                print (f"HA!, you lose.\nThe number was {rng_system}")

                while self.Retry == 0:
                    Retry = input("Would you like to try again? [yes] or [no]: ")

                    if Retry == "yes":
                        print ("Restarting...")
                    #time.sleep here
                        a = RandomNumberGenerator()
                        a.Game_File()

                    elif Retry == "no":
                        exit()

                    else:
                        print("Invalid Option")       
            
if __name__ == "__main__":
    a = RandomNumberGenerator()
    a.Game_File()