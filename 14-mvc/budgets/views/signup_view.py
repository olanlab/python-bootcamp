from tkinter import ttk, END
from tkinter import messagebox


class SignUpView(ttk.Frame):
    def __init__(self, controller, app):
        super().__init__(app)
        self.controller = controller
        
        self.label_firstname = ttk.Label(self, text='Firstname:')
        self.label_firstname.grid(row=1, column=0, pady=(20, 0))

        self.entry_firstname = ttk.Entry(self, width=30, justify="center")
        self.entry_firstname.grid(row=2, column=0)

        self.label_lastname = ttk.Label(self, text='Lastname:')
        self.label_lastname.grid(row=3, column=0)

        self.entry_lastname = ttk.Entry(self, width=30, justify="center")
        self.entry_lastname.grid(row=4, column=0)

        self.label_username = ttk.Label(self, text='Username:')
        self.label_username.grid(row=5, column=0)

        self.entry_username = ttk.Entry(self, width=30, justify="center")
        self.entry_username.grid(row=6, column=0)

        self.label_email = ttk.Label(self, text='Email:')
        self.label_email.grid(row=7, column=0)

        self.entry_email = ttk.Entry(self, width=30, justify="center")
        self.entry_email.grid(row=8, column=0)

        self.label_password = ttk.Label(self, text='Password:')
        self.label_password.grid(row=9, column=0)

        self.entry_password = ttk.Entry(self, width=30, show="*", justify="center")
        self.entry_password.grid(row=10, column=0)

        self.warning_msg = ttk.Label(self, text="", foreground="red")
        self.warning_msg.grid(row=11, column=0)

        self.button = ttk.Button(self ,text="Sign Up", command=self.signup)
        self.button.grid(row=12, column=0, pady=(10, 0))

        self.label_or = ttk.Label(self, text='Or')
        self.label_or.grid(row=13, column=0, pady=10)

        self.button = ttk.Button(self ,text="Back", command=self.login)
        self.button.grid(row=14, column=0, pady=(0, 20))

        self.entry_list = [self.entry_firstname, self.entry_lastname, self.entry_username, self.entry_email, self.entry_password]

    def clear_entries(self):
        for entry in self.entry_list:
            entry.delete(0, END)
    
    def hide_error(self):
        self.warning_msg.configure(text="")

    def show_error(self, msg):
        self.warning_msg.configure(text=msg)

    def signup(self):
        self.controller.signup(self.entry_firstname.get(), self.entry_lastname.get(), self.entry_username.get() ,self.entry_email.get(), self.entry_password.get())

    def login(self):
        self.controller.show_login()

    def show_massagebox(self, msg):
        messagebox.showinfo("Information", msg)

