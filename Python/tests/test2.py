import time

class MathQuiz:
    def __init__(self):
        self.marks = 0
        self.correct_answers = [
            "B",
            "A",
            "D"
        ]
        self.questions = [
            "Fifteen years from now Ravi is four times his present age, find his present age." ,
            "Sum of 2 numbers is 95. If one exceeds another by 15, find the greater number." ,
            " The base of an isosceles triangle is 4/3 cm, if the perimeter is 62/15 cm. What is the lenght of the remaining sides."
        ]
        self.choices = [
            """
[A] 10
[B] 5
[C] 15
[D] 1       
            """ ,
            """
[A] 55
[B] 65
[C] 15
[D] 25      
            """ ,
            """
[A] 6.3
[B] 7.2
[C] 2.0
[D] 2.8     
            """
        ]

    def question1(self):
        print ("Welcome to the quiz!")
        time.sleep(2)
        print(f"{self.questions[0]}")
        time.sleep(2)
        print(f"{self.choices[0]}")

        answer1 = input("Answer: ").upper()

        if answer1 == self.correct_answers[0]:
            self.marks += 1
            print ("Correct!")

        else:
            print ("Incorrect!")

    def question2(self):
        print(f"{self.questions[1]}")
        time.sleep(2)
        print(f"{self.choices[1]}")

        answer2 = input("Answer: ").upper()

        if answer2 == self.correct_answers[1]:
            self.marks += 1
            print ("Correct")
        
        else:
            print ("Incorrect!")

    def question3(self):
        print(f"{self.questions[2]}")
        time.sleep(2)
        print(f"{self.choices[2]}")

        answer3 = input("Answer: ").upper()

        if answer3 == self.correct_answers[2]:
            self.marks += 1
            print ("Correct! ")
        else:
            print ("Incorrect!")

    def mark_system(self):
        print (" Calculating total marks, please wait...")
        time.sleep(3)
        print (f" Your Marks are, {self.marks} Out of 3 ")

    def retry_system(self):
        while self.marks <= 2:
                     
            freewill = input("Would you like to retry? [Yes] or [No]: ").lower()

            if freewill == "yes":
                print ("Restarting...")
                time.sleep(2)
                a = MathQuiz()
                a.question1()
                a.question2()
                a.question3()
                a.mark_system()
                a.retry_system()

            elif freewill == "no":               
                print ("Who put you incharge?")
                
                time.sleep(1)
                print (" . ")
                time.sleep(1)
                print (" . ")
                time.sleep(1)
                print (" . ")
                time.sleep(2)
                a = MathQuiz()
                a.question1()
                a.question2()
                a.question3()
                a.mark_system()
                a.retry_system()
                   
        else:
            while self.marks == 3:
                option = input("Would you like to try again? [yes] or [no]: ").lower()
                if option == "yes":
                    a = MathQuiz()
                    a.question1()
                    a.question2()
                    a.question3()
                    a.mark_system()
                    a.retry_system()

                elif option == "no":
                    print ("Since you have scored 100%, the quiz can now shutdown")
                    time.sleep(1)
                    print ("Shut down in:")
                    time.sleep(1)
                    print ("3")
                    time.sleep(1)
                    print ("2")
                    time.sleep(1)
                    print ("1")
                    time.sleep(0.5)
                    print ("Exiting...")
                    time.sleep(2)
                    exit()

                else:
                    print(f"{option} is not a valid option!")

if __name__ == "__main__":      
    a = MathQuiz()
    a.question1()
    a.question2()
    a.question3()
    a.mark_system()
    a.retry_system()