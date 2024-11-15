from time import sleep
from sys import stdout

class Assignments:
    def __init__(self):
        print("----------------------------------------")
        self.name = input("Enter your name: ").title()

    def welcome(self):
        print("----------------------------------------")
        for i in range(5):
            stdout.write('\rLogging In |')
            sleep(0.1)
            stdout.write('\rLogging In /')
            sleep(0.1)
            stdout.write('\rLogging In -')
            sleep(0.1)
            stdout.write('\rLogging In \\')
            sleep(0.1)
        stdout.write(f'\rWelcome, {self.name}!                                                                                                                                   ')
        print("\n----------------------------------------")

    def inp_2num(self,x,y):
        if x>y:
            print(f"{x} is larger")
        elif y>x:
            print(f"{y} is larger")
        else:
            print(f"{x} and {y} are equal")

    def inp_3num(self,x,y,z):
        if x>y and x>z:
            print(f"{x} is the largest")
        elif y>x and y>z:
            print(f"{y} is the largest")
        elif z>x and z>y:
            print(f"{z} is the largest")
        else:
            print(f"{x}, {y} and {z} are equal")

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
        print(f"Reversed: {reversed_text}")
        if reversed_text.lower() == text.lower():
            print(f"{text} is a palindrome")
        else:
            print(f"{text} is not a palindrome")

    def small_large_list(self,num):
        num_list = []
        for x in range(0,num):
            try:
                element = int(input(f"Enter Element No.{x+1}: "))
                num_list.append(element)
            except ValueError:
                    print("----------------------------------------")
                    print("ERROR!\nYou must input an integer")
                    print("----------------------------------------")
        largest=max(num_list) 
        smallest=min(num_list)
        sum_of_list=sum(num_list)
        print(f"The List Of Numbers:\n\n{num_list}") 
        print()
        print(f"Largest number: {largest}") 
        print(f"Smallest number: {smallest}")
        print(f"Sum of the numbers: {sum_of_list}")

    def search_element(self,num):
        list1 = []
        repeated = 0
        for x in range(0,num):
            try:
                element = int(input(f"Enter Element No.{x+1}: "))
                list1.append(element)
            except ValueError:
                    print("----------------------------------------")
                    print("ERROR!\nYou must input an integer")
                    print("----------------------------------------")
        print()
        print(f"List:\n{list1}")
        print()
        search = int(input("Enter the element you want to find: "))
        for x in range(len(list1)):
            if search == list1[x]:
                repeated+=1
            else:
                pass
        if repeated > 0:
            print(f"{search} is present in the list, and is repeated {repeated} times")
        else:
            print(f"{search} is not present in the list")

    def armstrong_detector(self,num):
        sep_num = list(str(num))
        pow_num = []

        for x in sep_num:
            pow_num.append(int(x)**len(sep_num))
        
        if sum(pow_num) == num:
            print(f"{num} is an armstrong number.")
        else:
            print(f"{num} is not an armstrong number.")

    def perfect_detector(self,num):
        div_list = []

        for x in range(1,num):
            if num%x==0:
                div_list.append(x)

        if sum(div_list) == num:
            print(f"{num} is a perfect number.")
        else:
            print(f"{num} is not a perfect number.")

    def system(self):
        while True:
            print(f"""Which project would {self.name} like to access?

1. Input 2 numbers and display the larger/smaller number.
2. Input 3 numbers and display the larger/smaller number.
3. Prime and Composite Number Detector.
4. Vowels, Consonants, Upper and Lowecase Letters Counter.
5. Palindrome Detector.
6. Find the largest/smallest number in a list.
7. Search for an element in an inputted list.
8. Armstrong number Detector.
9. Perfect number Detector.

Type `Exit` to the shut me down""")
            print("----------------------------------------")
            self.user = input("> ").upper()
            print("----------------------------------------")

            if self.user == "1":
                try:
                    x = int(input("Enter X: "))
                    y = int(input("Enter Y: "))
                    self.inp_2num(x,y)
                    print("----------------------------------------")
                    sleep(1)
                except ValueError:
                    print("----------------------------------------")
                    print("ERROR!\nYou must input an integer")
                    print("----------------------------------------")

            elif self.user == "2":
                try:
                    x = int(input("Enter X: "))
                    y = int(input("Enter Y: "))
                    z = int(input("Enter Z: "))
                    self.inp_3num(x,y,z)
                    print("----------------------------------------")
                    sleep(1)
                except ValueError:
                    print("----------------------------------------")
                    print("ERROR!\nYou must input an integer")
                    print("----------------------------------------")

            elif self.user == "3":
                try:
                    num = int(input("Enter a number: "))
                    self.prime_composite(num)
                    print("----------------------------------------")
                    sleep(1)
                except ValueError:
                    print("----------------------------------------")
                    print("ERROR!\nYou must input an integer")
                    print("----------------------------------------")

            elif self.user == "4":
                text = input("Input the text to count: ")
                self.vow_con_upp_low(text)
                print("----------------------------------------")
                sleep(1)

            elif self.user == "5":
                text = input("Input a text to detect: ")
                self.palindrome_detector(text)
                print("----------------------------------------")
                sleep(1)

            elif self.user == "6":
                try:
                    num=int(input("Enter the number of elements in the list: "))
                    self.small_large_list(num)
                    print("----------------------------------------")
                    sleep(1)
                except ValueError:
                    print("----------------------------------------")
                    print("ERROR!\nYou must input an integer")
                    print("----------------------------------------")

            elif self.user == "7":
                try:
                    num=int(input("Enter the number of elements in the list: "))
                    self.search_element(num)
                    print("----------------------------------------")
                    sleep(1)
                except ValueError:
                    print("----------------------------------------")
                    print("ERROR!\nYou must input an integer")
                    print("----------------------------------------")
                
            elif self.user == "8":
                try:
                    num = int(input("Enter a number: "))
                    self.armstrong_detector(num)
                    print("----------------------------------------")
                    sleep(1)
                except ValueError:
                    print("----------------------------------------")
                    print("ERROR!\nYou must input an integer")
                    print("----------------------------------------")

            elif self.user == "9":
                try:
                    num = int(input("Enter a number: "))
                    self.perfect_detector(num)
                    print("----------------------------------------")
                    sleep(1)
                except ValueError:
                    print("----------------------------------------")
                    print("ERROR!\nYou must input an integer")
                    print("----------------------------------------")

            elif self.user == "EXIT":
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
                print("----------------------------------------")
                sleep(1)

if __name__ == "__main__":
    assign = Assignments()
    assign.welcome()
    assign.system()