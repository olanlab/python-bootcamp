import tkinter as tk

class View1(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.label = tk.Label(self, text="View 1")
        self.label.grid(row=0, column=0, padx=10, pady=10)
        self.button = tk.Button(self, text="Switch to View 2", command=self.switch_view)
        self.button.grid(row=1, column=0, padx=10, pady=10)

    def switch_view(self):
        self.parent.view2.tkraise()

class View2(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.label = tk.Label(self, text="View 2")
        self.label.grid(row=0, column=0, padx=10, pady=10)
        self.button = tk.Button(self, text="Switch to View 1", command=self.switch_view)
        self.button.grid(row=1, column=0, padx=10, pady=10)

    def switch_view(self):
        self.parent.view1.tkraise()

class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.view1 = View1(self)
        self.view2 = View2(self)
        self.view1.grid(row=0, column=0, sticky="nsew")
        self.view2.grid(row=0, column=0, sticky="nsew")
        self.view1.tkraise()

if __name__ == '__main__':
    app = App()
    app.mainloop()
