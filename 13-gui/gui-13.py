import tkinter as tk

class MyApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.create_widgets()

    def create_widgets(self):
        # create a button to open a new window
        button = tk.Button(self, text="Open new window", command=self.open_window)
        button.pack()

    def open_window(self):
        # create a new Toplevel window
        new_window = tk.Toplevel(self)
        new_window.title("New Window")
        new_window.geometry("200x200")

        # add widgets to the new window
        label = tk.Label(new_window, text="This is a new window!")
        label.pack()

if __name__ == '__main__':
    app = MyApp()
    app.mainloop()
