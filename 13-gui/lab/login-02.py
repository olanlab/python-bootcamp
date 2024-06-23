import mysql.connector
from tkinter import Tk, Frame, Button, Label, Entry, END


connection = None
cursor = None

class SignIn(Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master

        self.label_username = Label(self, text='Username:')
        self.label_username.grid(row=1, column=0, pady=(20, 0))

        self.entry_username = Entry(self, width=30, justify="center")
        self.entry_username.grid(row=2, column=0)
        self.entry_username.insert(0, "olan")

        self.label_password = Label(self, text='Password:', )
        self.label_password.grid(row=3, column=0)

        self.entry_password = Entry(self, width=30, show='*', justify="center")
        self.entry_password.grid(row=4, column=0)
        self.entry_password.insert(0, "1234")

        self.warning_msg = Label(self, text="", foreground="red")
        self.warning_msg.grid(row=5, column=0)

        self.button = Button(self ,text="Log In", command=self.login)
        self.button.grid(row=6, column=0)

        self.label_or = Label(self, text='Or')
        self.label_or.grid(row=7, column=0, pady=10)

        self.button = Button(self ,text="Sign Up", command=self.signup)
        self.button.grid(row=8, column=0, pady=(0, 20))

    def login(self):
        # QUERY DATABASE
        try :
            connection = mysql.connector.connect(user='root', host='localhost', charset="utf8mb4",  database="python" )
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (self.entry_username.get(), self.entry_password.get()))
            row = cursor.fetchone()

            if row == None:
                self.show_error("Invalid username or password")
                return
            self.master.show(self.master.main)
      
        except Exception as err:
            self.show_error(err)
        finally:
            if cursor != None:
                cursor.close()
            if connection != None:
                connection.close()


    def show(self):
        self.master.title("Application : Log In")
        self.pack(padx=10, pady=10, expand=True)

    def signup(self):
        self.master.show(self.master.signup)

    def hide_error(self):
        self.warning_msg.configure(text="")

    def show_error(self, msg):
        self.warning_msg.configure(text=msg)

class SignUp(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master

        self.label_firstname = Label(self, text='Firstname:')
        self.label_firstname.grid(row=1, column=0, pady=(20, 0))

        self.entry_firstname = Entry(self, width=30, justify="center")
        self.entry_firstname.grid(row=2, column=0)

        self.label_lastname = Label(self, text='Lastname:')
        self.label_lastname.grid(row=3, column=0)

        self.entry_lastname = Entry(self, width=30, justify="center")
        self.entry_lastname.grid(row=4, column=0)

        self.label_username = Label(self, text='Username:')
        self.label_username.grid(row=5, column=0)

        self.entry_username = Entry(self, width=30, justify="center")
        self.entry_username.grid(row=6, column=0)

        self.label_email = Label(self, text='Email:')
        self.label_email.grid(row=7, column=0)

        self.entry_email = Entry(self, width=30, justify="center")
        self.entry_email.grid(row=8, column=0)

        self.label_password = Label(self, text='Password:')
        self.label_password.grid(row=9, column=0)

        self.entry_password = Entry(self, width=30, show="*", justify="center")
        self.entry_password.grid(row=10, column=0)

        self.warning_msg = Label(self, text="", foreground="red")
        self.warning_msg.grid(row=11, column=0)

        self.button = Button(self ,text="Sign Up", command=self.signup)
        self.button.grid(row=12, column=0, pady=(10, 0))

        self.label_or = Label(self, text='Or')
        self.label_or.grid(row=13, column=0, pady=10)

        self.button = Button(self ,text="Back", command=self.login)
        self.button.grid(row=14, column=0, pady=(0, 20))

        self.entry_list = [self.entry_firstname, self.entry_lastname, self.entry_username, self.entry_email, self.entry_password]

    
    def show(self):
        self.master.title("Application : Sign Up")
        self.pack(padx=10, pady=10, expand=True)
   
    def hide_error(self):
        self.warning_msg.configure(text="")

    def show_success(self, msg):
        self.warning_msg.configure(text=msg, foreground="green")

    def show_error(self, msg):
        self.warning_msg.configure(text=msg, foreground="red")

    def signup(self):
        # SAVE IN DATABASE
        try :
            firstname = self.entry_firstname.get()
            lastname = self.entry_lastname.get()
            username = self.entry_username.get()
            email = self.entry_email.get()
            password = self.entry_password.get()
            params = (firstname, lastname, username, email, password)

            connection = mysql.connector.connect(user='root', host='localhost', charset="utf8mb4",  database="python" )
            cursor = connection.cursor()
            cursor.execute("INSERT INTO users (firstname, lastname, username, email, password) VALUES (%s, %s, %s, %s, %s)", params)
            connection.commit()

            if(cursor.rowcount > 0):
                self.show_success( "Insert user data successfully.")
                self.clear_entries()
            else: 
                self.show_error( "Insert user data error.")
            
        except Exception as err:
            self.show_error(err)
        finally:
            if cursor != None:
                cursor.close()
            if connection != None:
                connection.close()

    def clear_entries(self):
        for entry in self.entry_list:
            entry.delete(0, END)
        

    def login(self):
        self.master.show(self.master.signin)

    
class Main(Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
    
    def show(self):
        self.master.title("Application")
        self.pack(padx=10, pady=10, expand=True)
        
class App(Tk):

    width = 500
    height = 600

    def __init__(self):
        super().__init__()
        self.title("Application")
        self.geometry(f"{self.width}x{self.height}")

        # FRAMES
        self.signin = SignIn(self)
        self.signup = SignUp(self)
        self.main = Main(self)
        self.frames = [self.signin, self.signup, self.main ]

        # SHOW LOGIN
        self.show(self.signin)

    def show(self, frame) :
        for f in self.frames:
            f.pack_forget()
        frame.show()


app = App()
app.mainloop()