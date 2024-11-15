import customtkinter as ctk

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def __str__(self):
        return f"\nBook Title: {self.title}\nBook Author: {self.author}\nAvailable: {self.available}"

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

class LibraryApp(Book):
    books = []
    borrowed = False

    def __init__(self):
        self.app = ctk.CTk()
        self.app.geometry("1080x720")
        self.app.title("Library ~ Muaz")

        self.main_frame = ctk.CTkFrame(self.app)
        self.main_frame.pack(padx=15, pady=15, fill="both", expand=True)

        self.subframe1 = ctk.CTkFrame(self.main_frame)
        self.subframe1.pack(fill="both", expand=True)

        self.subframe2 = ctk.CTkFrame(self.main_frame)
        self.subframe2.pack(fill="both", expand=True)

        self.subframe3 = ctk.CTkFrame(self.main_frame)
        self.subframe3.pack(fill="both", expand=True)

        self.text = ctk.CTkLabel(self.subframe1, text="Welcome To Muaz's Library!", font=("CalSans-SemiBold", 30))
        self.text.pack(side="top", fill="both", expand=True)

        self.status = ctk.CTkLabel(self.subframe3, text="‎", font=("CalSans-SemiBold", 30))
        self.status.pack(side="bottom", fill="both", expand=True)

        self.addtitleentry = ctk.CTkEntry(self.subframe2, placeholder_text="Book Title")
        self.addtitleentry.pack(side="left", padx=30)

        self.addauthorentry = ctk.CTkEntry(self.subframe2, placeholder_text="Book Author")
        self.addauthorentry.pack(side="left")

        self.titleentry = ctk.CTkEntry(self.subframe2, placeholder_text="Book Title")
        self.titleentry.pack(side="right", padx=117)

        self.addbutton = ctk.CTkButton(
            self.subframe1, text="Add\nBook",
            font=("CalSans-SemiBold", 30),
            width=160, height=160,
            border_width=0,
            corner_radius=8,
            fg_color="#484848",
            hover_color="#5F5F5F",
            anchor="center",
            command=self.add_book
        )
        self.addbutton.pack(side="left", padx=107)

        self.borrowbutton = ctk.CTkButton(
            self.subframe1, text="Borrow\nBook",
            font=("CalSans-SemiBold", 30),
            width=160, height=160,
            border_width=0,
            corner_radius=8,
            fg_color="#484848",
            hover_color="#5F5F5F",
            anchor="center",
            command=self.borrow_book
        )
        self.borrowbutton.pack(side="right", padx=107)

        self.returnbutton = ctk.CTkButton(
            self.subframe3, text="Return\nBook",
            font=("CalSans-SemiBold", 30),
            width=160, height=160,
            border_width=0,
            corner_radius=8,
            fg_color="#484848",
            hover_color="#5F5F5F",
            anchor="center",
            command=self.return_book
        )
        self.returnbutton.pack(side="right", padx=107)

        self.viewbutton = ctk.CTkButton(
            self.subframe3, text="View\nBooks",
            font=("CalSans-SemiBold", 30),
            width=160, height=160,
            border_width=0,
            corner_radius=8,
            fg_color="#484848",
            hover_color="#5F5F5F",
            anchor="center",
            command=self.view_book
        )
        self.viewbutton.pack(side="left", padx=107)

        self.app.mainloop()
        return
    
    def add_book(self):
        title=self.addtitleentry.get()
        author=self.addauthorentry.get()
        lib = Book(title,author)
        book = [title,author,lib.available]
        self.books.append(book)
        self.status.configure(text=f"Added Book '{title}' Successfully!")

    def view_book(self):
        self.view_app = ctk.CTk()
        self.view_app.geometry("720x720")
        self.view_app.title("View Books - Muaz")

        self.main_frame = ctk.CTkScrollableFrame(self.view_app)
        self.main_frame.pack(padx=15, pady=15, fill="both", expand=True)
    
        for i in self.books:
            self.text = ctk.CTkLabel(self.main_frame, text=f"\nBook Title: {i[0]}\nBook Author: {i[1]}\nAvailable: {i[2]}", font=("CalSans-SemiBold", 30))
            self.text.pack(side="top", fill="both", expand=True)

        self.view_app.mainloop()

    def borrow_book(self):
        title=self.titleentry.get()
        for i in range(len(self.books)):
            if self.books[i][0]==title:
                if self.books[i][2]:
                    self.books[i][2]=False
                    self.borrowed=True
                    self.status.configure(text=f"You have borrowed {title}! Please return it!")
                    break
                else:
                    self.status.configure(text=f"{title} is not available! Please try again later!")

    def return_book(self):
        title=self.titleentry.get()
        for i in range(len(self.books)):
            if self.borrowed:
                if self.books[i][0]==title:
                    self.books[i][2]=True
                    self.borrowed=False
                    self.status.configure(text=f"You have successfully returned {title}!")
                    break
            else:
                self.status.configure(text=f"You have not borrowed any books, there's nothing to return.")
                break

LibraryApp()