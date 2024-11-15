from sys import stdout
from random import randint
from time import sleep

class Projects:
    def __init__(self,name):
        self.name = name

    def prime_composite(self,n):
        if n>1:
            if n==2:
                print(f"{n} is a prime number")
            elif n%2==0:
                print(f"{n} is a composite number")
            else:
                print(f"{n} is a prime number")
        else:
            print(f"{n} is neither is a prime or a composite number")

    def vow_con_upp_low(self,text):
        vowels = ["a", "e", "i", "o", "u","A","E","I","O","U"]
        vowel_count = consonant_count = upper_count = lower_count = 0

        for i in text:
            if text.isalpha():
                if i in vowels:
                    vowel_count += 1
                if i not in vowels:
                    consonant_count += 1
                if i.isupper():
                    upper_count += 1
                if i.islower():
                    lower_count += 1
                else:
                    pass
            else:
                pass
        print(f"Vowels: {vowel_count}\nConsonants: {consonant_count}\nUppercase: {upper_count}\nLowecase: {lower_count}")

    def palindrome_detector(self,text):
        reversed_text = text[::-1]
        print(reversed_text)
        if reversed_text.lower() == text.lower():
            print(f"{text} is a palindrome")
        else:
            print(f"{text} is not a palindrome")

    def odd_even(self,num):
        if num%2==0:
            print(f"{num} is an even number")
        else:
            print(f"{num} is an odd number")

    def guessing_game(self,guess,limit):
        rn = randint(1,limit+1)
        if guess == rn:
            print(f"{self.name} Won!")
        else:
            print(f"{self.name} Lost! The number was {rn}")

    def system(self):
        while True:
            print("----------------------------------------")
            print(f"""Which project would you, {self.name}, like to access?

A. Prime and Composite Number Detector.
B. Vowels, Consonants, Upper and Lowecase Letters Counter.
C. Palindrome Detector.
D. Odd or Even number Detector.
E. Guessing Game.

Type `Exit` to the shut me down""")
            print("----------------------------------------")
            user = input("> ").upper()
            print("----------------------------------------")

            if user == "A":
                number=int(input("Enter a number: "))
                self.prime_composite(number)
                sleep(1)

            elif user == "B":
                text = input("Input a text to count: ")
                self.vow_con_upp_low(text)
                sleep(1)

            elif user == "C":
                text = input("Input a text to detect: ")
                self.palindrome_detector(text)
                sleep(1)

            elif user == "D":
                number=int(input("Enter a number: "))
                self.odd_even(number)
                sleep(1)

            elif user == "E":
                limit=5
                guess = int(input(f"Guess a number between 1 to {limit}: "))
                self.guessing_game(guess,limit)
                sleep(1)

            elif user == "EXIT":
                print()
                for i in range(5):
                    stdout.write('\rShutting Down |')
                    sleep(0.1)
                    stdout.write('\rShutting Down /')
                    sleep(0.1)
                    stdout.write('\rShutting Down -')
                    sleep(0.1)
                    stdout.write('\rShutting Down \\')
                    sleep(0.1)
                stdout.write('\rShut Down Successfully!               ')
                print()
                print()
                print("----------------------------------------")
                break
            else:
                print(f"Unfortunately {self.name}, that is not an option.")

if __name__ == "__main__":
    name = input("What is your name?: ").title()
    initiate_project = Projects(name)
    initiate_project.system()