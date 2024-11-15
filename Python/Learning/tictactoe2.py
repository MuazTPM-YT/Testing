import customtkinter as ctk
from PIL import Image

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

class TicTacToeAPP:
    def __init__(self):
        self.app = ctk.CTk()
        self.app.geometry("650x800")
        self.app.title("TicTacToe ~ Muaz")

        self.board = [["" for i in range(3)] for i in range(3)]

        self.main_frame = ctk.CTkFrame(self.app)
        self.main_frame.pack(padx=35, pady=35, fill="both", expand=True)

        self.entryframe = ctk.CTkFrame(self.main_frame, fg_color="#212121")
        self.entryframe.pack(padx=10, pady=10, fill="both", expand=True)

        self.entry1 = ctk.CTkEntry(self.entryframe, placeholder_text="Player 1")
        self.entry1.pack(side="left", padx=5, pady=5)

        self.entry2 = ctk.CTkEntry(self.entryframe, placeholder_text="Player 2")
        self.entry2.pack(side="left", padx=5, pady=5)

        self.blank = ctk.CTkImage(
            dark_image=Image.open("C:/Users/uncha/Desktop/Software/Testing/Python/Learning/assets/blankimage.png"),
            size=(30, 30))
        self.x = ctk.CTkImage(
            dark_image=Image.open("C:/Users/uncha/Desktop/Software/Testing/Python/Learning/assets/ximage.png"),
            size=(117, 100))
        self.o = ctk.CTkImage(
            dark_image=Image.open("C:/Users/uncha/Desktop/Software/Testing/Python/Learning/assets/oimage.png"),
            size=(123, 123))

        self.start_button = ctk.CTkButton(self.entryframe, text="Start", command=self.start_game)
        self.start_button.pack(side="right", padx=10, pady=10)

        self.labelframe = ctk.CTkFrame(self.main_frame, fg_color="#212121")
        self.labelframe.pack(padx=10, fill="both", expand=True)

        self.label = ctk.CTkLabel(self.labelframe, text="Welcome to TicTacToe", font=("CalSans-SemiBold", 30))
        self.label.pack(padx=10, pady=10)

        self.buttonframe = ctk.CTkFrame(self.main_frame, fg_color="#212121")
        self.buttonframe.pack(padx=10, pady=10, fill="both", expand=True)

        self.subframe1 = ctk.CTkFrame(self.buttonframe)
        self.subframe1.pack(fill="both", expand=True)

        self.subframe2 = ctk.CTkFrame(self.buttonframe)
        self.subframe2.pack(fill="both", expand=True)

        self.subframe3 = ctk.CTkFrame(self.buttonframe)
        self.subframe3.pack(fill="both", expand=True)

        self.button1 = ctk.CTkButton(
            self.subframe1, text="‎",
            width=180, height=180,
            border_width=0,
            corner_radius=8,
            fg_color="#484848",
            hover_color="#5F5F5F",
            command=self.nullifier,
            image=self.blank,
            anchor="center",
        )
        self.button1.pack(side="left", padx=5, pady=5, fill="both")

        self.button2 = ctk.CTkButton(
            self.subframe1, text="‎",
            width=180, height=180,
            border_width=0,
            corner_radius=8,
            fg_color="#484848",
            hover_color="#5F5F5F",
            command=self.nullifier,
            image=self.blank,
            anchor="center",
        )
        self.button2.pack(side="left", padx=5, pady=5, fill="both")

        self.button3 = ctk.CTkButton(
            self.subframe1, text="‎",
            width=180, height=180,
            border_width=0,
            corner_radius=8,
            fg_color="#484848",
            hover_color="#5F5F5F",
            command=self.nullifier,
            image=self.blank,
            anchor="center",
        )
        self.button3.pack(side="left", padx=5, pady=5, fill="both")

        self.button4 = ctk.CTkButton(
            self.subframe2, text="‎",
            width=180, height=180,
            border_width=0,
            corner_radius=8,
            fg_color="#484848",
            hover_color="#5F5F5F",
            command=self.nullifier,
            image=self.blank,
            anchor="center",
        )
        self.button4.pack(side="left", padx=5, pady=5, fill="both")

        self.button5 = ctk.CTkButton(
            self.subframe2, text="‎",
            width=180, height=180,
            border_width=0,
            corner_radius=8,
            fg_color="#484848",
            hover_color="#5F5F5F",
            command=self.nullifier,
            image=self.blank,
            anchor="center",
        )
        self.button5.pack(side="left", padx=5, pady=5, fill="both")

        self.button6 = ctk.CTkButton(
            self.subframe2, text="‎",
            width=180, height=180,
            border_width=0,
            corner_radius=8,
            fg_color="#484848",
            hover_color="#5F5F5F",
            command=self.nullifier,
            image=self.blank,
            anchor="center",
        )
        self.button6.pack(side="left", padx=5, pady=5, fill="both")

        self.button7 = ctk.CTkButton(
            self.subframe3, text="‎",
            width=180, height=180,
            border_width=0,
            corner_radius=8,
            fg_color="#484848",
            hover_color="#5F5F5F",
            command=self.nullifier,
            image=self.blank,
            anchor="center",
        )
        self.button7.pack(side="left", padx=5, pady=5, fill="both")

        self.button8 = ctk.CTkButton(
            self.subframe3, text="‎",
            width=180, height=180,
            border_width=0,
            corner_radius=8,
            fg_color="#484848",
            hover_color="#5F5F5F",
            command=self.nullifier,
            image=self.blank,
            anchor="center",
        )
        self.button8.pack(side="left", padx=5, pady=5, fill="both")

        self.button9 = ctk.CTkButton(
            self.subframe3, text="‎",
            width=180, height=180,
            border_width=0,
            corner_radius=8,
            fg_color="#484848",
            hover_color="#5F5F5F",
            command=self.nullifier,
            image=self.blank,
            anchor="center",
        )
        self.button9.pack(side="left", padx=5, pady=5, fill="both")

        self.app.resizable(False, False)
        self.app.mainloop()
        return

    def turn(self):
        self.player1 = self.entry1.get()
        self.player2 = self.entry2.get()

        self.turn = self.player1

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

    def button1_clicked(self):
        if self.turn == self.player1:
            self.turn = self.player2
            self.label.configure(text=f"It is {self.turn}'s Turn!")
            self.button1.configure(image=self.x, command=self.nullifier, anchor="center")
            self.board[0][0] = 'x'

        elif self.turn == self.player2:
            self.turn = self.player1
            self.label.configure(text=f"It is {self.turn}'s Turn!")
            self.button1.configure(image=self.o, command=self.nullifier, anchor="center")
            self.board[0][0] = 'o'

        else:
            self.label.configure(text="Error! Unknown Player!")

        if self.checkForWin():
            self.button1.configure(command=self.nullifier)
            self.button2.configure(command=self.nullifier)
            self.button3.configure(command=self.nullifier)
            self.button4.configure(command=self.nullifier)
            self.button5.configure(command=self.nullifier)
            self.button6.configure(command=self.nullifier)
            self.button7.configure(command=self.nullifier)
            self.button8.configure(command=self.nullifier)
            self.button9.configure(command=self.nullifier)

            return self.label.configure(text=f"{self.player1 if self.turn == self.player2 else self.player2} has Won!")

        elif self.checkForWin() == False:
            self.button1.configure(command=self.nullifier)
            self.button2.configure(command=self.nullifier)
            self.button3.configure(command=self.nullifier)
            self.button4.configure(command=self.nullifier)
            self.button5.configure(command=self.nullifier)
            self.button6.configure(command=self.nullifier)
            self.button7.configure(command=self.nullifier)
            self.button8.configure(command=self.nullifier)
            self.button9.configure(command=self.nullifier)

            return self.label.configure(text=f"It's A Tie!")

    def button2_clicked(self):
        if self.turn == self.player1:
            self.turn = self.player2
            self.label.configure(text=f"It is {self.turn}'s Turn!")
            self.button2.configure(image=self.x, command=self.nullifier, anchor="center")
            self.board[0][1] = 'x'

        elif self.turn == self.player2:
            self.turn = self.player1
            self.label.configure(text=f"It is {self.turn}'s Turn!")
            self.button2.configure(image=self.o, command=self.nullifier, anchor="center")
            self.board[0][1] = 'o'

        else:
            self.label.configure(text="Error! Unknown Player!")

        if self.checkForWin():
            self.button1.configure(command=self.nullifier)
            self.button2.configure(command=self.nullifier)
            self.button3.configure(command=self.nullifier)
            self.button4.configure(command=self.nullifier)
            self.button5.configure(command=self.nullifier)
            self.button6.configure(command=self.nullifier)
            self.button7.configure(command=self.nullifier)
            self.button8.configure(command=self.nullifier)
            self.button9.configure(command=self.nullifier)

            return self.label.configure(text=f"{self.player1 if self.turn == self.player2 else self.player2} has Won!")

        elif self.checkForWin() == False:
            self.button1.configure(command=self.nullifier)
            self.button2.configure(command=self.nullifier)
            self.button3.configure(command=self.nullifier)
            self.button4.configure(command=self.nullifier)
            self.button5.configure(command=self.nullifier)
            self.button6.configure(command=self.nullifier)
            self.button7.configure(command=self.nullifier)
            self.button8.configure(command=self.nullifier)
            self.button9.configure(command=self.nullifier)

            return self.label.configure(text=f"It's A Tie!")

    def button3_clicked(self):
        if self.turn == self.player1:
            self.turn = self.player2
            self.label.configure(text=f"It is {self.turn}'s Turn!")
            self.button3.configure(image=self.x, command=self.nullifier, anchor="center")
            self.board[0][2] = 'x'

        elif self.turn == self.player2:
            self.turn = self.player1
            self.label.configure(text=f"It is {self.turn}'s Turn!")
            self.button3.configure(image=self.o, command=self.nullifier, anchor="center")
            self.board[0][2] = 'o'

        else:
            self.label.configure(text="Error! Unknown Player!")

        if self.checkForWin():
            self.button1.configure(command=self.nullifier)
            self.button2.configure(command=self.nullifier)
            self.button3.configure(command=self.nullifier)
            self.button4.configure(command=self.nullifier)
            self.button5.configure(command=self.nullifier)
            self.button6.configure(command=self.nullifier)
            self.button7.configure(command=self.nullifier)
            self.button8.configure(command=self.nullifier)
            self.button9.configure(command=self.nullifier)

            return self.label.configure(text=f"{self.player1 if self.turn == self.player2 else self.player2} has Won!")

        elif self.checkForWin() == False:
            self.button1.configure(command=self.nullifier)
            self.button2.configure(command=self.nullifier)
            self.button3.configure(command=self.nullifier)
            self.button4.configure(command=self.nullifier)
            self.button5.configure(command=self.nullifier)
            self.button6.configure(command=self.nullifier)
            self.button7.configure(command=self.nullifier)
            self.button8.configure(command=self.nullifier)
            self.button9.configure(command=self.nullifier)

            return self.label.configure(text=f"It's A Tie!")

    def button4_clicked(self):
        if self.turn == self.player1:
            self.turn = self.player2
            self.label.configure(text=f"It is {self.turn}'s Turn!")
            self.button4.configure(image=self.x, command=self.nullifier, anchor="center")
            self.board[1][0] = 'x'

        elif self.turn == self.player2:
            self.turn = self.player1
            self.label.configure(text=f"It is {self.turn}'s Turn!")
            self.button4.configure(image=self.o, command=self.nullifier, anchor="center")
            self.board[1][0] = 'o'

        else:
            self.label.configure(text="Error! Unknown Player!")

        if self.checkForWin():
            self.button1.configure(command=self.nullifier)
            self.button2.configure(command=self.nullifier)
            self.button3.configure(command=self.nullifier)
            self.button4.configure(command=self.nullifier)
            self.button5.configure(command=self.nullifier)
            self.button6.configure(command=self.nullifier)
            self.button7.configure(command=self.nullifier)
            self.button8.configure(command=self.nullifier)
            self.button9.configure(command=self.nullifier)

            return self.label.configure(text=f"{self.player1 if self.turn == self.player2 else self.player2} has Won!")

        elif self.checkForWin() == False:
            self.button1.configure(command=self.nullifier)
            self.button2.configure(command=self.nullifier)
            self.button3.configure(command=self.nullifier)
            self.button4.configure(command=self.nullifier)
            self.button5.configure(command=self.nullifier)
            self.button6.configure(command=self.nullifier)
            self.button7.configure(command=self.nullifier)
            self.button8.configure(command=self.nullifier)
            self.button9.configure(command=self.nullifier)

            return self.label.configure(text=f"It's A Tie!")

    def button5_clicked(self):
        if self.turn == self.player1:
            self.turn = self.player2
            self.label.configure(text=f"It is {self.turn}'s Turn!")
            self.button5.configure(image=self.x, command=self.nullifier, anchor="center")
            self.board[1][1] = 'x'

        elif self.turn == self.player2:
            self.turn = self.player1
            self.label.configure(text=f"It is {self.turn}'s Turn!")
            self.button5.configure(image=self.o, command=self.nullifier, anchor="center")
            self.board[1][1] = 'o'

        else:
            self.label.configure(text="Error! Unknown Player!")

        if self.checkForWin():
            self.button1.configure(command=self.nullifier)
            self.button2.configure(command=self.nullifier)
            self.button3.configure(command=self.nullifier)
            self.button4.configure(command=self.nullifier)
            self.button5.configure(command=self.nullifier)
            self.button6.configure(command=self.nullifier)
            self.button7.configure(command=self.nullifier)
            self.button8.configure(command=self.nullifier)
            self.button9.configure(command=self.nullifier)

            return self.label.configure(text=f"{self.player1 if self.turn == self.player2 else self.player2} has Won!")

        elif self.checkForWin() == False:
            self.button1.configure(command=self.nullifier)
            self.button2.configure(command=self.nullifier)
            self.button3.configure(command=self.nullifier)
            self.button4.configure(command=self.nullifier)
            self.button5.configure(command=self.nullifier)
            self.button6.configure(command=self.nullifier)
            self.button7.configure(command=self.nullifier)
            self.button8.configure(command=self.nullifier)
            self.button9.configure(command=self.nullifier)

            return self.label.configure(text=f"It's A Tie!")

    def button6_clicked(self):
        if self.turn == self.player1:
            self.turn = self.player2
            self.label.configure(text=f"It is {self.turn}'s Turn!")
            self.button6.configure(image=self.x, command=self.nullifier, anchor="center")
            self.board[1][2] = 'x'

        elif self.turn == self.player2:
            self.turn = self.player1
            self.label.configure(text=f"It is {self.turn}'s Turn!")
            self.button6.configure(image=self.o, command=self.nullifier, anchor="center")
            self.board[1][2] = 'o'

        else:
            self.label.configure(text="Error! Unknown Player!")

        if self.checkForWin():
            self.button1.configure(command=self.nullifier)
            self.button2.configure(command=self.nullifier)
            self.button3.configure(command=self.nullifier)
            self.button4.configure(command=self.nullifier)
            self.button5.configure(command=self.nullifier)
            self.button6.configure(command=self.nullifier)
            self.button7.configure(command=self.nullifier)
            self.button8.configure(command=self.nullifier)
            self.button9.configure(command=self.nullifier)

            return self.label.configure(text=f"{self.player1 if self.turn == self.player2 else self.player2} has Won!")

        elif self.checkForWin() == False:
            self.button1.configure(command=self.nullifier)
            self.button2.configure(command=self.nullifier)
            self.button3.configure(command=self.nullifier)
            self.button4.configure(command=self.nullifier)
            self.button5.configure(command=self.nullifier)
            self.button6.configure(command=self.nullifier)
            self.button7.configure(command=self.nullifier)
            self.button8.configure(command=self.nullifier)
            self.button9.configure(command=self.nullifier)

            return self.label.configure(text=f"It's A Tie!")

    def button7_clicked(self):
        if self.turn == self.player1:
            self.turn = self.player2
            self.label.configure(text=f"It is {self.turn}'s Turn!")
            self.button7.configure(image=self.x, command=self.nullifier, anchor="center")
            self.board[2][0] = 'x'

        elif self.turn == self.player2:
            self.turn = self.player1
            self.label.configure(text=f"It is {self.turn}'s Turn!")
            self.button7.configure(image=self.o, command=self.nullifier, anchor="center")
            self.board[2][0] = 'o'

        else:
            self.label.configure(text="Error! Unknown Player!")

        if self.checkForWin():
            self.button1.configure(command=self.nullifier)
            self.button2.configure(command=self.nullifier)
            self.button3.configure(command=self.nullifier)
            self.button4.configure(command=self.nullifier)
            self.button5.configure(command=self.nullifier)
            self.button6.configure(command=self.nullifier)
            self.button7.configure(command=self.nullifier)
            self.button8.configure(command=self.nullifier)
            self.button9.configure(command=self.nullifier)

            return self.label.configure(text=f"{self.player1 if self.turn == self.player2 else self.player2} has Won!")

        elif self.checkForWin() == False:
            self.button1.configure(command=self.nullifier)
            self.button2.configure(command=self.nullifier)
            self.button3.configure(command=self.nullifier)
            self.button4.configure(command=self.nullifier)
            self.button5.configure(command=self.nullifier)
            self.button6.configure(command=self.nullifier)
            self.button7.configure(command=self.nullifier)
            self.button8.configure(command=self.nullifier)
            self.button9.configure(command=self.nullifier)

            return self.label.configure(text=f"It's A Tie!")

    def button8_clicked(self):
        if self.turn == self.player1:
            self.turn = self.player2
            self.label.configure(text=f"It is {self.turn}'s Turn!")
            self.button8.configure(image=self.x, command=self.nullifier, anchor="center")
            self.board[2][1] = 'x'

        elif self.turn == self.player2:
            self.turn = self.player1
            self.label.configure(text=f"It is {self.turn}'s Turn!")
            self.button8.configure(image=self.o, command=self.nullifier, anchor="center")
            self.board[2][1] = 'o'

        else:
            self.label.configure(text="Error! Unknown Player!")

        if self.checkForWin():
            self.button1.configure(command=self.nullifier)
            self.button2.configure(command=self.nullifier)
            self.button3.configure(command=self.nullifier)
            self.button4.configure(command=self.nullifier)
            self.button5.configure(command=self.nullifier)
            self.button6.configure(command=self.nullifier)
            self.button7.configure(command=self.nullifier)
            self.button8.configure(command=self.nullifier)
            self.button9.configure(command=self.nullifier)

            return self.label.configure(text=f"{self.player1 if self.turn == self.player2 else self.player2} has Won!")

        elif self.checkForWin() == False:
            self.button1.configure(command=self.nullifier)
            self.button2.configure(command=self.nullifier)
            self.button3.configure(command=self.nullifier)
            self.button4.configure(command=self.nullifier)
            self.button5.configure(command=self.nullifier)
            self.button6.configure(command=self.nullifier)
            self.button7.configure(command=self.nullifier)
            self.button8.configure(command=self.nullifier)
            self.button9.configure(command=self.nullifier)

            return self.label.configure(text=f"It's A Tie!")

    def button9_clicked(self):
        if self.turn == self.player1:
            self.turn = self.player2
            self.button9.configure(image=self.x, command=self.nullifier, anchor="center")
            self.board[2][2] = 'x'

        elif self.turn == self.player2:
            self.turn = self.player1
            self.button9.configure(image=self.o, command=self.nullifier, anchor="center")
            self.board[2][2] = 'o'

        else:
            self.label.configure(text="Error! Unknown Player!")

        if self.checkForWin():
            self.button1.configure(command=self.nullifier)
            self.button2.configure(command=self.nullifier)
            self.button3.configure(command=self.nullifier)
            self.button4.configure(command=self.nullifier)
            self.button5.configure(command=self.nullifier)
            self.button6.configure(command=self.nullifier)
            self.button7.configure(command=self.nullifier)
            self.button8.configure(command=self.nullifier)
            self.button9.configure(command=self.nullifier)

            return self.label.configure(text=f"{self.player1 if self.turn == self.player2 else self.player2} has Won!")

        elif self.checkForWin() == False:
            self.button1.configure(command=self.nullifier)
            self.button2.configure(command=self.nullifier)
            self.button3.configure(command=self.nullifier)
            self.button4.configure(command=self.nullifier)
            self.button5.configure(command=self.nullifier)
            self.button6.configure(command=self.nullifier)
            self.button7.configure(command=self.nullifier)
            self.button8.configure(command=self.nullifier)
            self.button9.configure(command=self.nullifier)

            return self.label.configure(text=f"It's A Tie!")

    def start_game(self):
        self.turn()

        self.label.configure(text=f"It is {self.turn}'s Turn!")

        self.button1.configure(command=self.button1_clicked)
        self.button2.configure(command=self.button2_clicked)
        self.button3.configure(command=self.button3_clicked)
        self.button4.configure(command=self.button4_clicked)
        self.button5.configure(command=self.button5_clicked)
        self.button6.configure(command=self.button6_clicked)
        self.button7.configure(command=self.button7_clicked)
        self.button8.configure(command=self.button8_clicked)
        self.button9.configure(command=self.button9_clicked)

    def nullifier(self):
        pass


if __name__ == "__main__":
    TicTacToeAPP()
