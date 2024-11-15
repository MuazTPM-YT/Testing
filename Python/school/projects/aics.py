import customtkinter as ctk

class VotingSystem:
    def __init__(self):
        self.window = ctk.CTk()
        self.window.title("EMF Calculator")
        self.window.geometry("1280x720")

        self.mainframe = ctk.CTkFrame(self.window)
        self.mainframe.pack(padx=15, pady=15, fill="both", expand=True)

        self.name_entry = ctk.CTkEntry(self.mainframe, width=500, height=50, corner_radius=15, placeholder_text="RPM", font=("Calibri", 25))
        self.name_entry.pack(padx=15, pady=15)

        self.entry_button = ctk.CTkButton(self.mainframe, width=100, height=50, corner_radius=15, text="Vote", font=("Calibri", 25))
        self.entry_button.pack(padx=15)

        self.voteframe = ctk.CTkFrame(self.mainframe)
        self.voteframe.pack(padx=15, pady=15, fill="both", expand=True)

        self.window.resizable(True, True)
        self.window.mainloop()

if __name__ == "__main__":
    VotingSystem()