import customtkinter as ctk
import random as rn

class GuessAPP:
	def __init__(self):
		self.app = ctk.CTk()
		self.app.geometry("400x400")
		
		self.mainframe = ctk.CTkFrame(self.app)
		self.mainframe.pack(padx=35, pady=35, fill="both", expand=True)

		self.topframe = ctk.CTkFrame(self.mainframe, fg_color="#2B2B2B")
		self.topframe.pack(padx=20, pady=20, fill="both", expand=True)

		self.botframe = ctk.CTkFrame(self.mainframe, fg_color="#2B2B2B")
		self.botframe.pack(padx=20, pady=20, fill="both", expand=True)

		self.intro = ctk.CTkLabel(self.topframe, text="Guessing Game", font=("CalSans-SemiBold", 20))
		self.intro.pack()

		self.entry = ctk.CTkEntry(self.topframe, placeholder_text="Guess a number")
		self.entry.pack(pady=25)

		self.start_button = ctk.CTkButton(self.topframe, text="Start", command=self.system)
		self.start_button.pack()

		self.maintext = ctk.CTkLabel(self.botframe, text="Any number from 1-5", font=("CalSans-SemiBold", 20))
		self.maintext.pack()

		self.app.resizable(False, False)
		self.app.mainloop()

	def initiate(self):
		self.guess = int(self.entry.get())
		self.random_num = rn.randint(1,5)

	def system(self):
		self.initiate()

		if self.guess == self.random_num:
			self.maintext.configure(text=f"You Won!\nCorrect Number was {self.random_num}")

		else:
			self.maintext.configure(text=f"You Lost!\nCorrect Number was {self.random_num}")

if __name__ == "__main__":
	GuessAPP()