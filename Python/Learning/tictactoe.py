import tkinter as tk
from tkinter import ttk, LEFT, GROOVE, Button

class TicTacToeApp():
    def __init__(self, p1, p2):
        self.player1 = p1
        self.player2 = p2

        self.turn = self.player1

        self.board = [["" for i in range(3)] for i in range(3)]

        self.window = tk.Tk()
        self.window.geometry("400x600")
        self.window.title("TicTacToe ~ Muaz")

        self.mainframe = tk.Frame(self.window, background="white")
        self.mainframe.pack(fill="both", expand=True)

        self.subframe_one = tk.Frame(self.window, background="white")
        self.subframe_one.pack(fill="both", expand=True)

        self.subframe_two = tk.Frame(self.window, background="white")
        self.subframe_two.pack(fill="both", expand=True)

        self.subframe_three = tk.Frame(self.window, background="white")
        self.subframe_three.pack(fill="both", expand=True)

        self.text = ttk.Label(self.mainframe, text="TicTacToe!", background="white", font=("Brass Mono", 30))
        self.text.pack()

        self.button_one = Button(  
            self.subframe_one,  
            text="⬜",  
            font = ("Brass Mono", 30),  
            relief = GROOVE,  
            border = 5,  
            command = self.button_one_clicked,
            compound="center"
        )  

        self.button_one.pack(side=LEFT, expand=True, fill="both")  

        self.button_two = Button(  
            self.subframe_one,  
            text="⬜",  
            font = ("Brass Mono", 30),  
            relief = GROOVE,  
            border = 5,  
            command = self.button_two_clicked,
            compound="center"
        )  
        self.button_two.pack(side=LEFT, expand=True, fill="both")  

        self.button_three = Button(  
            self.subframe_one,  
            text="⬜",  
            font = ("Brass Mono", 30),  
            relief = GROOVE,  
            border = 5,  
            command = self.button_three_clicked,
            compound="center"
        )  
        self.button_three.pack(side=LEFT, expand=True, fill ="both")  

        self.button_four = Button(  
            self.subframe_two,  
            text="⬜",  
            font = ("Brass Mono", 30),  
            relief = GROOVE,  
            border = 5,  
            command = self.button_four_clicked,
            compound="center"
        )  
        self.button_four.pack(side=LEFT, expand=True, fill ="both")  

        self.button_five = Button(  
            self.subframe_two,  
            text="⬜",  
            font = ("Brass Mono", 30),  
            relief = GROOVE,  
            border = 5,  
            command = self.button_five_clicked,
            compound="center" 
        )  
        self.button_five.pack(side=LEFT, expand=True, fill ="both")  

        self.button_six = Button(  
            self.subframe_two,  
            text="⬜",  
            font = ("Brass Mono", 30),  
            relief = GROOVE,  
            border = 5,  
            command = self.button_six_clicked,
            compound="center"
        )  
        self.button_six.pack(side=LEFT, expand=True, fill ="both")  

        self.button_seven = Button(  
            self.subframe_three,  
            text="⬜",  
            font = ("Brass Mono", 30),  
            relief = GROOVE,  
            border = 5,  
            command = self.button_seven_clicked,
            compound="center"
        )
        self.button_seven.pack(side=LEFT, expand=True, fill ="both") 

        self.button_eight = Button(  
            self.subframe_three,  
            text="⬜",  
            font = ("Brass Mono", 30),  
            relief = GROOVE,  
            border = 5,  
            command = self.button_eight_clicked,
            compound="center" 
        )  
        self.button_eight.pack(side=LEFT, expand=True, fill ="both") 

        self.button_nine = Button(  
            self.subframe_three,  
            text="⬜",  
            font = ("Brass Mono", 30),  
            relief = GROOVE,  
            border = 5,  
            command = self.button_nine_clicked,
            compound="center"
        )  
        self.button_nine.pack(side=LEFT, expand=True, fill ="both") 

        self.window.mainloop()
        return

    def checkForWin(self):
        BLANK = ''
        board = self.board
        for i in range(3):
            if (board[i][0] == board[i][1] == board[i][2]) and board[i][0] != BLANK:
                return True

            if (board[0][i] == board[1][i] == board[2][i]) and board[0][i] != BLANK:
                return True

        if (board[0][0] == board[1][1] == board[2][2]) and board[0][0] != BLANK:
            return True

        if (board[0][2] == board[1][1] == board[2][0]) and board[0][2] != BLANK:
            return True

        if not sum([i.count(BLANK) for i in board]):
            return False

    def button_one_clicked(self):
        if self.turn == self.player1:
            self.turn = self.player2
            self.button_one.config(text="❎", command=self.nullifier, compound="center")
            self.board[0][0] = 'x'

        elif self.turn == self.player2:
            self.turn = self.player1
            self.button_one.config(text="⭕", command=self.nullifier, compound="center")
            self.board[0][0] = 'o'

        else:
            return self.text.config("Error! Unknown Player!")

        if self.checkForWin():
            self.button_one.config(command=self.nullifier)
            self.button_two.config(command=self.nullifier)
            self.button_three.config(command=self.nullifier)
            self.button_four.config(command=self.nullifier)
            self.button_five.config(command=self.nullifier)
            self.button_six.config(command=self.nullifier)
            self.button_seven.config(command=self.nullifier)
            self.button_eight.config(command=self.nullifier)
            self.button_nine.config(command=self.nullifier)
            
            return self.text.config(text=f"{self.player1 if self.turn == self.player2 else self.player2} has Won!")

        elif self.checkForWin() == False:
            self.button_one.config(command=self.nullifier)
            self.button_two.config(command=self.nullifier)
            self.button_three.config(command=self.nullifier)
            self.button_four.config(command=self.nullifier)
            self.button_five.config(command=self.nullifier)
            self.button_six.config(command=self.nullifier)
            self.button_seven.config(command=self.nullifier)
            self.button_eight.config(command=self.nullifier)
            self.button_nine.config(command=self.nullifier)
            
            return self.text.config(text=f"It's A Tie!")

    def button_two_clicked(self):
        if self.turn == self.player1:
            self.turn = self.player2
            self.button_two.config(text="❎", command=self.nullifier, compound="center")
            self.board[0][1] = 'x'

        elif self.turn == self.player2:
            self.turn = self.player1
            self.button_two.config(text="⭕", command=self.nullifier, compound="center")
            self.board[0][1] = 'o'

        else:
            return self.text.config("Error! Unknown Player!")

        if self.checkForWin():
            self.button_one.config(command=self.nullifier)
            self.button_two.config(command=self.nullifier)
            self.button_three.config(command=self.nullifier)
            self.button_four.config(command=self.nullifier)
            self.button_five.config(command=self.nullifier)
            self.button_six.config(command=self.nullifier)
            self.button_seven.config(command=self.nullifier)
            self.button_eight.config(command=self.nullifier)
            self.button_nine.config(command=self.nullifier)
            
            return self.text.config(text=f"{self.player1 if self.turn == self.player2 else self.player2} has Won!")

        elif self.checkForWin() == False:
            self.button_one.config(command=self.nullifier)
            self.button_two.config(command=self.nullifier)
            self.button_three.config(command=self.nullifier)
            self.button_four.config(command=self.nullifier)
            self.button_five.config(command=self.nullifier)
            self.button_six.config(command=self.nullifier)
            self.button_seven.config(command=self.nullifier)
            self.button_eight.config(command=self.nullifier)
            self.button_nine.config(command=self.nullifier)

            return self.text.config(text=f"It's A Tie!")

    def button_three_clicked(self):
        if self.turn == self.player1:
            self.turn = self.player2
            self.button_three.config(text="❎", command=self.nullifier, compound="center")
            self.board[0][2] = 'x'

        elif self.turn == self.player2:
            self.turn = self.player1
            self.button_three.config(text="⭕", command=self.nullifier, compound="center")
            self.board[0][2] = 'o'

        else:
            return self.text.config("Error! Unknown Player!")

        if self.checkForWin():
            self.button_one.config(command=self.nullifier)
            self.button_two.config(command=self.nullifier)
            self.button_three.config(command=self.nullifier)
            self.button_four.config(command=self.nullifier)
            self.button_five.config(command=self.nullifier)
            self.button_six.config(command=self.nullifier)
            self.button_seven.config(command=self.nullifier)
            self.button_eight.config(command=self.nullifier)
            self.button_nine.config(command=self.nullifier)
            
            return self.text.config(text=f"{self.player1 if self.turn == self.player2 else self.player2} has Won!")

        elif self.checkForWin() == False:
            self.button_one.config(command=self.nullifier)
            self.button_two.config(command=self.nullifier)
            self.button_three.config(command=self.nullifier)
            self.button_four.config(command=self.nullifier)
            self.button_five.config(command=self.nullifier)
            self.button_six.config(command=self.nullifier)
            self.button_seven.config(command=self.nullifier)
            self.button_eight.config(command=self.nullifier)
            self.button_nine.config(command=self.nullifier)

            return self.text.config(text=f"It's A Tie!")

    def button_four_clicked(self):
        if self.turn == self.player1:
            self.turn = self.player2
            self.button_four.config(text="❎", command=self.nullifier, compound="center")
            self.board[1][0] = 'x'

        elif self.turn == self.player2:
            self.turn = self.player1
            self.button_four.config(text="⭕", command=self.nullifier, compound="center")
            self.board[1][0] = 'o'

        else:
            return self.text.config("Error! Unknown Player!")

        if self.checkForWin():
            self.button_one.config(command=self.nullifier)
            self.button_two.config(command=self.nullifier)
            self.button_three.config(command=self.nullifier)
            self.button_four.config(command=self.nullifier)
            self.button_five.config(command=self.nullifier)
            self.button_six.config(command=self.nullifier)
            self.button_seven.config(command=self.nullifier)
            self.button_eight.config(command=self.nullifier)
            self.button_nine.config(command=self.nullifier)
            
            return self.text.config(text=f"{self.player1 if self.turn == self.player2 else self.player2} has Won!")

        elif self.checkForWin() == False:
            self.button_one.config(command=self.nullifier)
            self.button_two.config(command=self.nullifier)
            self.button_three.config(command=self.nullifier)
            self.button_four.config(command=self.nullifier)
            self.button_five.config(command=self.nullifier)
            self.button_six.config(command=self.nullifier)
            self.button_seven.config(command=self.nullifier)
            self.button_eight.config(command=self.nullifier)
            self.button_nine.config(command=self.nullifier)

            return self.text.config(text=f"It's A Tie!")

    def button_five_clicked(self):
        if self.turn == self.player1:
            self.turn = self.player2
            self.button_five.config(text="❎", command=self.nullifier, compound="center")
            self.board[1][1] = 'x'

        elif self.turn == self.player2:
            self.turn = self.player1
            self.button_five.config(text="⭕", command=self.nullifier, compound="center")
            self.board[1][1] = 'o'

        else:
            return self.text.config("Error! Unknown Player!")

        if self.checkForWin():
            self.button_one.config(command=self.nullifier)
            self.button_two.config(command=self.nullifier)
            self.button_three.config(command=self.nullifier)
            self.button_four.config(command=self.nullifier)
            self.button_five.config(command=self.nullifier)
            self.button_six.config(command=self.nullifier)
            self.button_seven.config(command=self.nullifier)
            self.button_eight.config(command=self.nullifier)
            self.button_nine.config(command=self.nullifier)
            
            return self.text.config(text=f"{self.player1 if self.turn == self.player2 else self.player2} has Won!")

        elif self.checkForWin() == False:
            self.button_one.config(command=self.nullifier)
            self.button_two.config(command=self.nullifier)
            self.button_three.config(command=self.nullifier)
            self.button_four.config(command=self.nullifier)
            self.button_five.config(command=self.nullifier)
            self.button_six.config(command=self.nullifier)
            self.button_seven.config(command=self.nullifier)
            self.button_eight.config(command=self.nullifier)
            self.button_nine.config(command=self.nullifier)
            
            return self.text.config(text=f"It's A Tie!")

    def button_six_clicked(self):
        if self.turn == self.player1:
            self.turn = self.player2
            self.button_six.config(text="❎", command=self.nullifier, compound="center")
            self.board[1][2] = 'x'

        elif self.turn == self.player2:
            self.turn = self.player1
            self.button_six.config(text="⭕", command=self.nullifier, compound="center")
            self.board[1][2] = 'o'

        else:
            return self.text.config("Error! Unknown Player!")

        if self.checkForWin():
            self.button_one.config(command=self.nullifier)
            self.button_two.config(command=self.nullifier)
            self.button_three.config(command=self.nullifier)
            self.button_four.config(command=self.nullifier)
            self.button_five.config(command=self.nullifier)
            self.button_six.config(command=self.nullifier)
            self.button_seven.config(command=self.nullifier)
            self.button_eight.config(command=self.nullifier)
            self.button_nine.config(command=self.nullifier)
            
            return self.text.config(text=f"{self.player1 if self.turn == self.player2 else self.player2} has Won!")

        elif self.checkForWin() == False:
            self.button_one.config(command=self.nullifier)
            self.button_two.config(command=self.nullifier)
            self.button_three.config(command=self.nullifier)
            self.button_four.config(command=self.nullifier)
            self.button_five.config(command=self.nullifier)
            self.button_six.config(command=self.nullifier)
            self.button_seven.config(command=self.nullifier)
            self.button_eight.config(command=self.nullifier)
            self.button_nine.config(command=self.nullifier)

            return self.text.config(text=f"It's A Tie!")

    def button_seven_clicked(self):
        if self.turn == self.player1:
            self.turn = self.player2
            self.button_seven.config(text="❎", command=self.nullifier, compound="center")
            self.board[2][0] = 'x'

        elif self.turn == self.player2:
            self.turn = self.player1
            self.button_seven.config(text="⭕", command=self.nullifier, compound="center")
            self.board[2][0] = 'o'

        else:
            return self.text.config("Error! Unknown Player!")

        if self.checkForWin():
            self.button_one.config(command=self.nullifier)
            self.button_two.config(command=self.nullifier)
            self.button_three.config(command=self.nullifier)
            self.button_four.config(command=self.nullifier)
            self.button_five.config(command=self.nullifier)
            self.button_six.config(command=self.nullifier)
            self.button_seven.config(command=self.nullifier)
            self.button_eight.config(command=self.nullifier)
            self.button_nine.config(command=self.nullifier)
            
            return self.text.config(text=f"{self.player1 if self.turn == self.player2 else self.player2} has Won!")

        elif self.checkForWin() == False:
            self.button_one.config(command=self.nullifier)
            self.button_two.config(command=self.nullifier)
            self.button_three.config(command=self.nullifier)
            self.button_four.config(command=self.nullifier)
            self.button_five.config(command=self.nullifier)
            self.button_six.config(command=self.nullifier)
            self.button_seven.config(command=self.nullifier)
            self.button_eight.config(command=self.nullifier)
            self.button_nine.config(command=self.nullifier)

            return self.text.config(text=f"It's A Tie!")

    def button_eight_clicked(self):
        if self.turn == self.player1:
            self.turn = self.player2
            self.button_eight.config(text="❎", command=self.nullifier, compound="center")
            self.board[2][1] = 'x'

        elif self.turn == self.player2:
            self.turn = self.player1
            self.button_eight.config(text="⭕", command=self.nullifier, compound="center")
            self.board[2][1] = 'o'

        else:
            return self.text.config("Error! Unknown Player!")

        if self.checkForWin():
            self.button_one.config(command=self.nullifier)
            self.button_two.config(command=self.nullifier)
            self.button_three.config(command=self.nullifier)
            self.button_four.config(command=self.nullifier)
            self.button_five.config(command=self.nullifier)
            self.button_six.config(command=self.nullifier)
            self.button_seven.config(command=self.nullifier)
            self.button_eight.config(command=self.nullifier)
            self.button_nine.config(command=self.nullifier)
            
            return self.text.config(text=f"{self.player1 if self.turn == self.player2 else self.player2} has Won!")

        elif self.checkForWin() == False:
            self.button_one.config(command=self.nullifier)
            self.button_two.config(command=self.nullifier)
            self.button_three.config(command=self.nullifier)
            self.button_four.config(command=self.nullifier)
            self.button_five.config(command=self.nullifier)
            self.button_six.config(command=self.nullifier)
            self.button_seven.config(command=self.nullifier)
            self.button_eight.config(command=self.nullifier)
            self.button_nine.config(command=self.nullifier)

            return self.text.config(text=f"It's A Tie!")

    def button_nine_clicked(self):
        if self.turn == self.player1:
            self.turn = self.player2
            self.button_nine.config(text="❎", command=self.nullifier, compound="center")
            self.board[2][2] = 'x'

        elif self.turn == self.player2:
            self.turn = self.player1
            self.button_nine.config(text="⭕", command=self.nullifier, compound="center")
            self.board[2][2] = 'o'

        else:
            return self.text.config("Error! Unknown Player!")

        if self.checkForWin():
            self.button_one.config(command=self.nullifier)
            self.button_two.config(command=self.nullifier)
            self.button_three.config(command=self.nullifier)
            self.button_four.config(command=self.nullifier)
            self.button_five.config(command=self.nullifier)
            self.button_six.config(command=self.nullifier)
            self.button_seven.config(command=self.nullifier)
            self.button_eight.config(command=self.nullifier)
            self.button_nine.config(command=self.nullifier)
            
            return self.text.config(text=f"{self.player1 if self.turn == self.player2 else self.player2} has Won!")

        elif self.checkForWin() == False:
            self.button_one.config(command=self.nullifier)
            self.button_two.config(command=self.nullifier)
            self.button_three.config(command=self.nullifier)
            self.button_four.config(command=self.nullifier)
            self.button_five.config(command=self.nullifier)
            self.button_six.config(command=self.nullifier)
            self.button_seven.config(command=self.nullifier)
            self.button_eight.config(command=self.nullifier)
            self.button_nine.config(command=self.nullifier)

            return self.text.config(text=f"It's A Tie!")

    def nullifier(self):
        pass
    
if __name__ == '__main__':
    p1_input = input("Enter your name (Player1): ")
    p2_input = input("Enter your name (Player2): ")

    TicTacToeApp(p1=p1_input, p2=p2_input)