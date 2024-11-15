class Quiz:
    def __init__(self):
        self.questions = (
            "What does RAM stand for?",
            "Which programming language is Python coded in?",
            "What is the chemical formula of Water?",
            "What is √24?",
            "What is sin^2x + cos^2x?"
        )
        self.options = (
            ("A. Random Access Memory", "B. Readable Assembly Memory", "C. Rebootable Augmented Memory", "D. Refreshed Arithmetic Memory"),
            ("A. Java", "B. C++", "C. Assembly", "D. Javascript"),
            ("A. H2O", "B. HO2", "C. H2O2", "D. 2HO2"),
            ("A. 4.82", "B. 4.95", "C. 4.85", "D. 4.9"),
            ("A. √3", "B. 1/2", "C. 1", "D. √3/2")
        )
        self.answers = (
            "A",
            "B",
            "A",
            "D",
            "C"
        )

        self.guesses = []
        
        self.marks = 0
        self.question_num = 0

    def display_system(self):
        for question in self.questions:
            print("----------------------------------------------")
            print(question)

            for option in self.options[self.question_num]:
                print(option)

            self.input_system()

            self.question_num += 1
            
        print("----------------------------------------------")

    def input_system(self):
        guess = input("Answer the question (A,B,C,D): ").upper()

        if guess == self.answers[self.question_num]:
            self.marks += 1
            self.guesses.append(guess)
            print("Correct!")
            self.result_system()

        else:
            print("Incorrect!")
            self.result_system()

    def result_system(self):
        if self.question_num >= 4:
            print("----------------------------------------------")
            print("                   RESULTS                    ")
            print("----------------------------------------------")

            print(f"Answers: {list(self.answers)}")

            percentage = int((self.marks/len(self.questions)) * 100)

            print(f"Marks  : {percentage}%")

        else:
            pass

if __name__ == "__main__":
    quiz = Quiz()
    quiz.display_system()