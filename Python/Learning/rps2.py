import customtkinter as ctk
import random
from PIL import Image

#fg_color="#2B2B2B"

class RPSApp:
    def __init__(self):
        self.app = ctk.CTk()
        self.app.geometry("800x600")
        self.app.title("Rock Paper Scissors ~ Muaz")

        self.mainframe = ctk.CTkFrame(self.app)
        self.mainframe.pack(padx=35, pady=35, fill="both", expand=True)

        self.entryframe = ctk.CTkFrame(self.mainframe, fg_color="#2B2B2B")
        self.entryframe.pack(fill="both", expand=True)

        self.playerentry = ctk.CTkEntry(self.entryframe, placeholder_text="Player")
        self.playerentry.pack(pady=30)

        self.start_button = ctk.CTkButton(self.entryframe, text="Start", command=self.system)
        self.start_button.pack()

        self.label = ctk.CTkLabel(self.entryframe, text="Welcome to Rock Paper Scissors!", font=("CalSans-SemiBold", 30))
        self.label.pack(pady=30)

        self.buttonframe = ctk.CTkFrame(self.mainframe, fg_color="#2B2B2B")
        self.buttonframe.pack(padx=10, pady=10, fill="both", expand=True)

        self.rockimage = ctk.CTkImage(dark_image=Image.open("C:/Users/uncha/Desktop/Software/Testing/Python/Learning/assets/rock.png"), size=(100,100))
        self.paperimage = ctk.CTkImage(dark_image=Image.open("C:/Users/uncha/Desktop/Software/Testing/Python/Learning/assets/paper.png"), size=(100,100))
        self.scissorimage = ctk.CTkImage(dark_image=Image.open("C:/Users/uncha/Desktop/Software/Testing/Python/Learning/assets/scissors.png"), size=(100,100))

        self.choices = ["rock", "paper", "scissors"]

        self.rockbutton = ctk.CTkButton(
            self.buttonframe, text="‎", 
            width=215, height=215,
            fg_color="#484848", 
            hover_color="#5F5F5F",
            image=self.rockimage,
            command=self.nullifier
        )
        self.rockbutton.pack(side="left", padx=10, pady=10, fill="both")

        self.paperbutton = ctk.CTkButton(
            self.buttonframe, text="‎", 
            width=215, height=215,
            fg_color="#484848", 
            hover_color="#5F5F5F",
            image=self.paperimage,
            command=self.nullifier
        )
        self.paperbutton.pack(side="left", padx=10, pady=10, fill="both")

        self.scissorsbutton = ctk.CTkButton(
            self.buttonframe, text="‎", 
            width=215, height=215,
            fg_color="#484848", 
            hover_color="#5F5F5F",
            image=self.scissorimage,
            command=self.nullifier
        )
        self.scissorsbutton.pack(side="left", padx=10, pady=10, fill="both")

        self.app.resizable(False, False)
        self.app.mainloop()

    def initiate(self):
        self.player = self.playerentry.get()
        self.computer = random.choice(self.choices)

    def system(self):
        self.initiate()

        self.label.configure(text=f"{self.player}! Please click the buttons below!")

        self.rockbutton.configure(command=self.rockclick)
        self.paperbutton.configure(command=self.paperclick)
        self.scissorsbutton.configure(command=self.scissorsclick)

    def rockclick(self):
        self.system()

        if self.computer == "rock":
            self.label.configure(text=f"It's A Tie! CPU chose Rock")

        elif self.computer == "paper":
            self.label.configure(text=f"{self.player} Loses! CPU chose Paper")

        elif self.computer == "scissors":
            self.label.configure(text=f"{self.player} Wins! CPU chose Scissors")

        else:
            self.label.configure(text=f"ERROR!")

    def paperclick(self):
        self.system()

        if self.computer == "rock":
            self.label.configure(text=f"{self.player} Wins! CPU chose Rock")

        elif self.computer == "paper":
            self.label.configure(text=f"It's A Tie! CPU chose Paper")

        elif self.computer == "scissors":
            self.label.configure(text=f"{self.player} Loses! CPU chose Scissors")

        else:
            self.label.configure(text=f"ERROR!")

    def scissorsclick(self):
        self.system()

        if self.computer == "rock":
            self.label.configure(text=f"{self.player} Loses! CPU chose Rock")

        elif self.computer == "paper":
            self.label.configure(text=f"{self.player} Wins! CPU chose Paper")

        elif self.computer == "scissors":
            self.label.configure(text=f"It's A Tie! CPU chose Scissors")

        else:
            self.label.configure(text=f"ERROR!")

    def nullifier(self):
        pass


if __name__ == "__main__":
    RPSApp()