import customtkinter as ctk
import mysql.connector as mysql

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def __str__(self):
        return f"\nBook Title: {self.title}\nBook Author: {self.author}\nAvailable: {self.available}"

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

class RegisterApp(ctk.CTkToplevel):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("800x800")
        self.title("Register Application")

        self.registerdb=mysql.connect(host="localhost",user="root",password="password",database="accountdatabase")
        self.registercur=self.registerdb.cursor()
        self.registercur.execute("CREATE TABLE IF NOT EXISTS user(Fname VARCHAR(30), Gender VARCHAR(20), Email VARCHAR(30), Phoneno VARCHAR(10), Username VARCHAR(30) UNIQUE, Password VARCHAR(30));")
        
        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.pack(padx=15, pady=15, fill="both", expand=True)

        self.label = ctk.CTkLabel(self.main_frame, text="Register Page", font=("CalSans-SemiBold", 30))
        self.label.place(x=285,y=67)

        self.valid = ctk.CTkLabel(self.main_frame, text="‎", font=("CalSans-SemiBold", 30))
        self.valid.pack(side="bottom",pady=55)

        self.fnameentry = ctk.CTkEntry(
            self.main_frame, 
            placeholder_text="First Name",
            font=("CalSans-SemiBold", 18),
            width=300,
            height=50
        )
        self.fnameentry.place(x=225, y=134)

        self.genderentry = ctk.CTkOptionMenu(
            self.main_frame,
            values=["Male", "Female","Prefer not to say"],
            font=("CalSans-SemiBold", 18),
            width=300,
            height=50
        )
        self.genderentry.place(x=225,y=201)

        self.emailentry = ctk.CTkEntry(
            self.main_frame, 
            placeholder_text="Email",
            font=("CalSans-SemiBold", 18),
            width=300,
            height=50
        )
        self.emailentry.place(x=225, y=268)

        self.phoneno = ctk.CTkEntry(
            self.main_frame, 
            placeholder_text="Phone No.",
            font=("CalSans-SemiBold", 18),
            width=300,
            height=50
        )
        self.phoneno.place(x=225, y=335)

        self.userentry = ctk.CTkEntry(
            self.main_frame, 
            placeholder_text="Username",
            font=("CalSans-SemiBold", 18),
            width=300,
            height=50
        )
        self.userentry.place(x=225, y=402)

        self.passentry = ctk.CTkEntry(
            self.main_frame, 
            placeholder_text="Password",
            font=("CalSans-SemiBold", 18),
            width=300,
            height=50,
            show="*"
        )
        self.passentry.place(x=225, y=469)

        self.confpassentry = ctk.CTkEntry(
            self.main_frame, 
            placeholder_text="Confirm Password",
            font=("CalSans-SemiBold", 18),
            width=300,
            height=50,
            show="*"
        )
        self.confpassentry.place(x=225, y=536)

        self.registerbutton = ctk.CTkButton(
            self.main_frame, text="Register",
            font=("CalSans-SemiBold", 20),
            width=300, height=50,
            border_width=0,
            corner_radius=8,
            fg_color="#484848",
            hover_color="#5F5F5F",
            anchor="center",
            command=self.register
        )
        self.registerbutton.place(x=225,y=603)

    def register(self):
        fname = self.fnameentry.get().strip()
        gender = self.genderentry.get().strip()
        email = self.emailentry.get().strip()
        phoneno = self.phoneno.get().strip()
        username = self.userentry.get().strip()
        password = self.passentry.get().strip()
        confpass = self.confpassentry.get().strip()

        if fname and email and username and password and confpass != "":
            if password==confpass:
                if email.endswith("@gmail.com"):
                    if len(phoneno) == 10:
                        try:
                            regquery=f"INSERT INTO user VALUES('{fname}','{gender}','{email}','{phoneno}','{username}','{password}');"

                            self.registercur.execute(regquery)
                            self.registerdb.commit()

                            self.valid.configure(text="Registered Successfully!")

                        except mysql.errors.IntegrityError:
                            self.valid.configure(text="Username is already taken!")

                        except:
                            self.valid.configure(text="Unexpected Error has Occurred!")
                    else:
                        self.valid.configure(text="Invalid Phone No.")

                else:
                    self.valid.configure(text="Invalid Email!")

            else:
                self.valid.configure(text="Passwords Do Not Match!")
        else:
            self.valid.configure(text="Please fill in the required fields!")

class LoginApp(ctk.CTk):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("800x800")
        self.title("Login Application")

        self.logindb=mysql.connect(host="localhost",user="root",password="password",database="accountdatabase")
        self.logincur=self.logindb.cursor()

        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.pack(padx=15, pady=15, fill="both", expand=True)

        self.label = ctk.CTkLabel(self.main_frame, text="Login Page", font=("CalSans-SemiBold", 30))
        self.label.place(x=300,y=240)

        self.valid = ctk.CTkLabel(self.main_frame, text="‎", font=("CalSans-SemiBold", 30))
        self.valid.pack(side="bottom",pady=225)

        self.userentry = ctk.CTkEntry(
            self.main_frame, 
            placeholder_text="Username",
            font=("CalSans-SemiBold", 18),
            width=300,
            height=50
        )
        self.userentry.place(x=225, y=300)

        self.passentry = ctk.CTkEntry(
            self.main_frame, 
            placeholder_text="Password",
            font=("CalSans-SemiBold", 18),
            width=300,
            height=50,
            show="*"
        )
        self.passentry.place(x=225, y=367)

        self.loginbutton = ctk.CTkButton(
            self.main_frame, text="Login",
            font=("CalSans-SemiBold", 20),
            width=300, height=50,
            border_width=0,
            corner_radius=8,
            fg_color="#484848",
            hover_color="#5F5F5F",
            anchor="center",
            command=self.login
        )
        self.loginbutton.place(x=225,y=434)

        self.createaccbutton = ctk.CTkButton(
            self.main_frame, text="Create Account",
            font=("CalSans-SemiBold", 20),
            width=300, height=50,
            border_width=0,
            anchor="center",
            corner_radius=8,
            fg_color="#484848",
            hover_color="#5F5F5F",
            command=self.createaccountwindow
        )
        self.createaccbutton.place(x=225,y=667)

        self.caw = None

    def createaccountwindow(self):
        if self.caw is None or not self.caw.winfo_exists():
            self.caw = RegisterApp(self)  
        else:
            self.caw.focus_force()

    def login(self):
        user = self.userentry.get().strip()
        passw = self.passentry.get().strip()

        if user and passw != "":
            self.logincur.execute("SELECT * FROM user;")
            data=self.logincur.fetchall()
            
            for i in data:
                if user == i[4] and passw == i[5]:
                    self.valid.configure(text="Successfully Logged in!")
                    LibraryApp()
                    break
            else:
                self.valid.configure(text="Invalid Credentials!")
        else:
            self.valid.configure(text="Please fill in the required fields!")


app = LoginApp()
app.mainloop()