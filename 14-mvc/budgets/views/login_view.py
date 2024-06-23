from tkinter import ttk


class LoginView(ttk.Frame):
    def __init__(self, controller, app):
        super().__init__(app)
        self.controller = controller
        
        self.label_username = ttk.Label(self, text='Username:')
        self.label_username.grid(row=1, column=0, pady=(20, 0))

        self.entry_username = ttk.Entry(self, width=30, justify="center")
        self.entry_username.grid(row=2, column=0)
        self.entry_username.insert(0, "olan")

        self.label_password = ttk.Label(self, text='Password:', )
        self.label_password.grid(row=3, column=0)

        self.entry_password = ttk.Entry(self, width=30, show='*', justify="center")
        self.entry_password.grid(row=4, column=0)
        self.entry_password.insert(0, "1234")

        self.warning_msg = ttk.Label(self, text="", foreground="red")
        self.warning_msg.grid(row=5, column=0)

        self.button = ttk.Button(self ,text="Log In", command=self.login)
        self.button.grid(row=6, column=0)

        self.label_or = ttk.Label(self, text='Or')
        self.label_or.grid(row=7, column=0, pady=10)

        self.button = ttk.Button(self ,text="Sign Up", command=self.signup)
        self.button.grid(row=8, column=0, pady=(0, 20))
        

    def login(self):
        self.controller.authenticate(self.entry_username.get(), self.entry_password.get())

    def signup(self):
        self.controller.show_signup()

    def hide_error(self):
        self.warning_msg.configure(text="")

    def show_error(self):
        self.warning_msg.configure(text="Invalid username or password")






    


    




        

    




    

    



        


