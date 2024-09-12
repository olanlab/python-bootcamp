import tkinter as tk

class MyApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.frame1 = tk.Frame(self)
        self.frame2 = tk.Frame(self)
        self.create_widgets()

    def create_widgets(self):
        # create widgets for frame 1
        label1 = tk.Label(self.frame1, text="This is frame 1")
        button1 = tk.Button(self.frame1, text="Go to frame 2",
                            command=self.show_frame2)
        label1.pack()
        button1.pack()

        # create widgets for frame 2
        label2 = tk.Label(self.frame2, text="This is frame 2")
        button2 = tk.Button(self.frame2, text="Go to frame 1",
                            command=self.show_frame1)
        label2.pack()
        button2.pack()

        # show the initial frame
        self.frame1.pack()

    def show_frame1(self):
        # hide frame 2 and show frame 1
        self.frame2.pack_forget()
        self.frame1.pack()

    def show_frame2(self):
        # hide frame 1 and show frame 2
        self.frame1.pack_forget()
        self.frame2.pack()

if __name__ == '__main__':
    app = MyApp()
    app.mainloop()
