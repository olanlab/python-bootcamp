import tkinter as tk

from controllers.authen_controller import AuthenController
from controllers.dashboard_controller import DashboardController
from utils.window import getCenterPosition

class App(tk.Tk):

    width = 400
    height = 400

    def __init__(self):
        super().__init__()
        self.title("Mr. Budget")
        self.controller = None

        # Menu
        menu = tk.Menu(self)
        # Create a file menu
        file_menu = tk.Menu(menu, tearoff=False)
        file_menu.add_command(label="Exit", command=self.quit)
        menu.add_cascade(label="File", menu=file_menu)
        self.config(menu=menu)

        # Window position
        x, y = getCenterPosition(self, width=self.width, height=self.height)
        self.geometry(f"{self.width}x{self.height}+{x}+{y}")

        # LOGIN
        self.show_login()
        
    def show_login(self):
        self.controller = AuthenController(self)
        self.controller.show_login()


    def show_dashbord(self):
        self.controller = DashboardController(self)
        self.controller.show()
    

if __name__ == "__main__":
    app = App()
    app.mainloop()