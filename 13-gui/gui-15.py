import tkinter as tk

class FrameSwitcher:
    def __init__(self, master):
        self.master = master
        self.frames = {}

    def add_frame(self, name, frame):
        self.frames[name] = frame
        frame.pack_forget()

    def switch_frame(self, name):
        for frame_name, frame in self.frames.items():
            if frame_name == name:
                frame.pack()
            else:
                frame.pack_forget()

class Frame1(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.create_widgets()

    def create_widgets(self):
        label = tk.Label(self, text="This is Frame 1")
        label.pack()

class Frame2(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.create_widgets()

    def create_widgets(self):
        label = tk.Label(self, text="This is Frame 2")
        label.pack()

class MyApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.frame_switcher = FrameSwitcher(self)
        self.create_widgets()

    def create_widgets(self):
        # create two frames and add them to the FrameSwitcher
        frame1 = Frame1(self)
        frame2 = Frame2(self)
        self.frame_switcher.add_frame("Frame 1", frame1)
        self.frame_switcher.add_frame("Frame 2", frame2)

        # create a menu with options to switch between frames
        menubar = tk.Menu(self)
        self.config(menu=menubar)

        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Switch to Frame 1",
                             command=lambda: self.frame_switcher.switch_frame("Frame 1"))
        filemenu.add_command(label="Switch to Frame 2",
                             command=lambda: self.frame_switcher.switch_frame("Frame 2"))
        filemenu.add_separator()
        filemenu.add_command(label="Quit", command=self.quit)

        menubar.add_cascade(label="File", menu=filemenu)

if __name__ == '__main__':
    app = MyApp()
    app.mainloop()
