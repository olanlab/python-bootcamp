import tkinter as tk

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        self.btn_show = tk.Button(self, text="Show Label", command=self.show_label)
        self.btn_show.pack()

        self.btn_hide = tk.Button(self, text="Hide Label", command=self.hide_label)
        self.btn_hide.pack()

        self.label = tk.Label(self, text="Hello World!")
        self.label.pack()

    def show_label(self):
        self.label.pack()

    def hide_label(self):
        self.label.pack_forget()

root = tk.Tk()
app = App(root)
app.pack()
root.mainloop()
