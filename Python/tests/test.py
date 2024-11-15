import time

class MathQuiz:
    def __init__(self):
        self.marks = None
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

    def welcome(self):
        print ("Welcome to the Quiz!")

    def question1(self):
        print(f"{self.questions[0]}")
        print(f"{self.choices[0]}")

        answer1 = input("Answer: ").upper()

        if answer1 == self.correct_answers[0]:
            self.marks += 1
            print ("Correct!")

        else:
            print ("Incorrect!")

    def question2(self):
        print(f"{self.questions[1]}")
        print(f"{self.choices[1]}")

        answer2 = input("Answer: ").upper()

        if answer2 == self.correct_answers[1]:
            self.marks += 1
            print ("Correct")
        
        else:
            print ("Incorrect!")

    def question3(self):
        print(f"{self.questions[2]}")
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

    def thing(self):
        freewill = input("Would you like to retry? [Yes] or [No]: ").lower()

        if freewill == "yes":
            pass

        elif freewill == "no":                
            print ("Who put you incharge?")
            
            time.sleep(1)
            print (" . ")
            time.sleep(1)
            print (" . ")
            time.sleep(1)
            print (" . ")
            time.sleep(1)
            pass

        else:
            return print("Invalid Option")

    def functions(self):
        while True:
            math_quiz = MathQuiz()
            math_quiz.marks = 0
            math_quiz.welcome()
            math_quiz.question1()
            math_quiz.question2()
            math_quiz.question3()
            math_quiz.mark_system()

            if math_quiz.marks == 3:
                math_quiz.thing()

            else:
                while True:
                    math_quiz = MathQuiz()
                    math_quiz.marks = 0
                    math_quiz.welcome()
                    math_quiz.question1()
                    math_quiz.question2()
                    math_quiz.question3()
                    math_quiz.mark_system()

if __name__ == "__main__":
    MathQuiz().functions()