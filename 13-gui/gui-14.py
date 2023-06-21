import tkinter as tk

class ChildWindow(tk.Toplevel):
    def __init__(self, parent, title):
        super().__init__(parent)
        self.title(title)
        self.geometry("200x200")
        self.create_widgets()

    def create_widgets(self):
        label = tk.Label(self, text="This is a child window.")
        label.pack()

class MyApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.create_widgets()

    def create_widgets(self):
        # create a menu with options to open child windows
        menubar = tk.Menu(self)
        self.config(menu=menubar)

        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Open Window 1",
                             command=lambda: self.open_child_window("Window 1"))
        filemenu.add_command(label="Open Window 2",
                             command=lambda: self.open_child_window("Window 2"))
        filemenu.add_command(label="Open Window 3",
                             command=lambda: self.open_child_window("Window 3"))
        filemenu.add_separator()
        filemenu.add_command(label="Quit", command=self.quit)

        menubar.add_cascade(label="File", menu=filemenu)

    def open_child_window(self, title):
        # create a new ChildWindow instance
        child_window = ChildWindow(self, title)

if __name__ == '__main__':
    app = MyApp()
    app.mainloop()
